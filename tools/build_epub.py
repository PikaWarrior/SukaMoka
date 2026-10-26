#!/usr/bin/env python3
"""Build a reflowable EPUB 3 sample from translated Markdown chunks."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import posixpath
import re
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET

import markdown

MIMETYPE = "application/epub+zip"
OPF = "http://www.idpf.org/2007/opf"
DC = "http://purl.org/dc/elements/1.1/"
XHTML = "http://www.w3.org/1999/xhtml"
CONTAINER = "urn:oasis:names:tc:opendocument:xmlns:container"
EPUB = "http://www.idpf.org/2007/ops"
ET.register_namespace("", XHTML)
ET.register_namespace("epub", EPUB)
ET.register_namespace("dc", DC)

MARKER_RE = re.compile(
    r"^\[\[EPUB_IMAGE:v(?P<volume>\d+):xhtml/(?P<source>[^:\]]+):"
    r"(?P<resource>[^:\]]+)(?::occ-(?P<occ>\d+))?\]\]$"
)
CITATION_RE = re.compile(r"\[cite:\s*[\d,\s]+\]")
FN_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:\s*(.*)$")
FN_REF_RE = re.compile(r"\[\^([^\]]+)\](?!:)")
HEADING_RE = re.compile(r"^(#{2,3})\s+(.+?)\s*$")
ID_ATTR_RE = re.compile(r"\s*\{#([A-Za-z][A-Za-z0-9_-]*)\}\s*$")


def natural_key(path: Path) -> tuple[int, str]:
    match = re.search(r"chunk_(\d+)", path.name, re.I)
    return (int(match.group(1)) if match else 10**9, path.name.lower())


def take_footnotes(text: str) -> tuple[str, dict[str, str]]:
    lines, body, defs = text.splitlines(), [], {}
    i = 0
    while i < len(lines):
        m = FN_DEF_RE.match(lines[i])
        if not m:
            body.append(lines[i])
            i += 1
            continue
        local_id = m.group(1)
        if local_id in defs:
            raise ValueError(f"Duplicate footnote definition [^{local_id}].")
        parts = [m.group(2).strip()]
        i += 1
        while i < len(lines):
            if lines[i].startswith(("    ", "\t")):
                parts.append(lines[i].strip())
                i += 1
            elif not lines[i].strip() and i + 1 < len(lines) and lines[i + 1].startswith(("    ", "\t")):
                i += 1
            else:
                break
        defs[local_id] = "\n\n".join(p for p in parts if p)
    return "\n".join(body), defs


def clean_chunk(path: Path, volume: int, report: str, state: dict) -> str:
    text = path.read_text(encoding="utf-8-sig")
    # Strip an optional Markdown wrapper without embedding literal backtick delimiters in this script.
    text = re.sub(r"^\s*\x60{3}(?:markdown|md)?\s*\n", "", text, count=1, flags=re.I)
    text = re.sub(r"\n\x60{3}\s*$", "", text, count=1)
    text = re.sub(r"(?m)^(?:#{1,6}\s*)?В глоссарий\s*:?\s*\n[\s\S]*$", "", text).rstrip()
    citations = CITATION_RE.findall(text)
    state["citation_tags_removed"] += len(citations)
    text = CITATION_RE.sub("", text)

    if "[пауза]" in text:
        raise ValueError(f"{path.name}: unresolved [пауза] marker; resolve it before building.")
    if re.search(r"〔[^〕]*〕", text):
        raise ValueError(f"{path.name}: Japanese ruby brackets 〔…〕 remain in Russian text.")

    text, defs = take_footnotes(text)
    refs = [m.group(1) for m in FN_REF_RE.finditer(text)]
    if set(refs) - set(defs):
        raise ValueError(f"{path.name}: undefined footnote(s): {sorted(set(refs)-set(defs))}")
    if set(defs) - set(refs):
        raise ValueError(f"{path.name}: unused footnote definition(s): {sorted(set(defs)-set(refs))}")

    local_map = {}
    for local_id, definition in defs.items():
        state["next_fn"] += 1
        uid = f"fn-{state['next_fn']:04d}"
        local_map[local_id] = {
            "uid": uid,
            "display": str(state["next_fn"]),
            "definition": definition,
            "source_chunk": path.name,
        }
        state["definitions"][uid] = local_map[local_id]

    def replace_ref(match: re.Match) -> str:
        local_id = match.group(1)
        state["next_ref"] += 1
        token = f"XFNREF{state['next_ref']:06d}X"
        info = dict(local_map[local_id])
        info["ref_id"] = f"ref-{state['next_ref']:04d}"
        info["token"] = token
        state["refs"][token] = info
        return token

    text = FN_REF_RE.sub(replace_ref, text)

    converted, last_scene = [], False
    for line_no, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        marker = MARKER_RE.fullmatch(s) if "[[EPUB_IMAGE:" in s else None
        if "[[EPUB_IMAGE:" in s and marker is None:
            raise ValueError(f"{path.name}:{line_no}: malformed or inline EPUB_IMAGE marker.")

        if marker:
            if int(marker.group("volume")) != volume:
                raise ValueError(f"{path.name}:{line_no}: marker volume doesn't match v{volume}.")
            if s not in report:
                raise ValueError(f"{path.name}:{line_no}: marker absent from volume report: {s}")
            resource = marker.group("resource")
            if "gaiji-cid776" in resource:
                if last_scene:
                    continue
                state["next_scene"] += 1
                token = f"XSCENE{state['next_scene']:06d}X"
                state["scene_tokens"].add(token)
                state["scene_count"] += 1
                converted.append(token)
                last_scene = True
                continue

            if resource.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                asset = Path("raw") / str(volume) / "item" / "image" / resource
                if not asset.is_file():
                    raise FileNotFoundError(f"{path.name}:{line_no}: missing image file {asset}")
                state["images"][resource] = asset
                state["image_markers"].append({
                    "marker": s,
                    "resource": resource,
                    "source_xhtml": "xhtml/" + marker.group("source"),
                    "source_chunk": path.name,
                })
                state["next_image"] += 1
                token = f"XIMAGE{state['next_image']:06d}X"
                state["image_tokens"][token] = resource
                converted.append(token)
                last_scene = False
                continue
            raise ValueError(f"{path.name}:{line_no}: unresolved marker resource {resource}")

        if s == "* * *":
            if last_scene:
                continue
            state["next_scene"] += 1
            token = f"XSCENE{state['next_scene']:06d}X"
            state["scene_tokens"].add(token)
            state["scene_count"] += 1
            converted.append(token)
            last_scene = True
            continue

        converted.append(line)
        if s:
            last_scene = False

    result = "\n".join(converted).strip()
    if "[[EPUB_IMAGE:" in result:
        raise ValueError(f"{path.name}: unresolved image marker remains.")
    return result


def add_heading_ids(text: str, records: list[dict], state: dict, chunk_name: str) -> str:
    out = []
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if not m:
            out.append(line)
            continue
        hashes, title = m.groups()
        title = ID_ATTR_RE.sub("", title).strip()
        state["next_heading"] += 1
        ident = f"heading-{state['next_heading']:04d}"
        records.append({"id": ident, "level": len(hashes), "title": title, "source_chunk": chunk_name})
        out.append(f"{hashes} {title} {{#{ident}}}")
    return "\n".join(out)


def split_by_h2(text: str) -> list[str]:
    sections, current = [], []
    for line in text.splitlines():
        if line.startswith("## ") and any(x.strip() for x in current):
            part = "\n".join(current).strip()
            if part:
                sections.append(part)
            current = [line]
        else:
            current.append(line)
    part = "\n".join(current).strip()
    if part:
        sections.append(part)
    return sections


def xhtml_doc(title: str, body: str) -> bytes:
    document = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        f'<html xmlns="{XHTML}" xmlns:epub="{EPUB}" lang="ru" xml:lang="ru">'
        '<head><meta charset="utf-8" />'
        f'<title>{html.escape(title)}</title>'
        '<link rel="stylesheet" type="text/css" href="../styles/book.css" />'
        '</head><body>' + body + '</body></html>\n'
    )
    ET.fromstring(document.encode("utf-8"))
    return document.encode("utf-8")


def validate_epub(path: Path, expected: dict) -> dict:
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        if not names or names[0] != "mimetype":
            raise ValueError("mimetype is not the first ZIP entry.")
        if zf.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            raise ValueError("mimetype is not stored without compression.")
        if zf.read("mimetype").decode("ascii") != MIMETYPE:
            raise ValueError("Invalid mimetype content.")
        files = set(names)
        roots, ids = {}, {}
        for name in names:
            if name.endswith((".xhtml", ".opf", ".xml")):
                root = ET.fromstring(zf.read(name))
                roots[name] = root
                ids[name] = set()
                for node in root.iter():
                    ident = node.attrib.get("id")
                    if ident:
                        if ident in ids[name]:
                            raise ValueError(f"Duplicate id {ident} in {name}.")
                        ids[name].add(ident)

        opf_name = "OEBPS/content.opf"
        if opf_name not in roots:
            raise ValueError("Missing OEBPS/content.opf.")
        ns = {"opf": OPF}
        package = roots[opf_name]
        manifest = package.findall("./opf:manifest/opf:item", ns)
        manifest_ids = {item.attrib["id"] for item in manifest}
        for item in manifest:
            target = posixpath.normpath(posixpath.join("OEBPS", item.attrib["href"]))
            if target not in files:
                raise ValueError(f"Manifest resource missing from archive: {target}")
        for itemref in package.findall("./opf:spine/opf:itemref", ns):
            if itemref.attrib.get("idref") not in manifest_ids:
                raise ValueError(f"Spine reference lacks manifest item: {itemref.attrib.get('idref')}")

        for name, root in roots.items():
            if not name.endswith(".xhtml"):
                continue
            for node in root.iter():
                for attr in ("href", "src"):
                    value = node.attrib.get(attr)
                    if not value:
                        continue
                    parsed = urlsplit(value)
                    if parsed.scheme or parsed.netloc:
                        continue
                    target = name
                    if parsed.path:
                        target = posixpath.normpath(posixpath.join(posixpath.dirname(name), parsed.path))
                        if target not in files:
                            raise ValueError(f"Broken local link in {name}: {value}")
                    if parsed.fragment and parsed.fragment not in ids.get(target, set()):
                        raise ValueError(f"Broken fragment link in {name}: {value}")

        visible, scene_count, fn_count, image_count = [], 0, 0, 0
        for name, root in roots.items():
            if not name.startswith("OEBPS/text/") or not name.endswith(".xhtml") or name.endswith("titlepage.xhtml"):
                continue
            visible.append("".join(root.itertext()))
            scene_count += len(root.findall(f".//{{{XHTML}}}p[@class='scene-break']"))
            fn_count += len(root.findall(f".//{{{XHTML}}}aside[@{{{EPUB}}}type='footnote']"))
            image_count += len(root.findall(f".//{{{XHTML}}}img"))
            for main in root.findall(f".//{{{XHTML}}}main"):
                previous_break = False
                for child in list(main):
                    is_break = child.tag == f"{{{XHTML}}}p" and child.attrib.get("class") == "scene-break"
                    if is_break and previous_break:
                        raise ValueError(f"Consecutive scene breaks in {name}.")
                    previous_break = is_break

        visible_text = "\n".join(visible)
        if re.search(r"\[\[EPUB_IMAGE:|〔[^〕]*〕|\[пауза\]|\[cite:|\bВ глоссарий\b|XSCENE\d{6}X|XIMAGE\d{6}X|XFNREF\d{6}X", visible_text):
            raise ValueError("A technical marker remains in visible book text.")
        if scene_count != expected["scene_count"]:
            raise ValueError(f"Scene-break count mismatch: expected {expected['scene_count']}, found {scene_count}.")
        if fn_count != expected["footnote_count"]:
            raise ValueError(f"Footnote count mismatch: expected {expected['footnote_count']}, found {fn_count}.")
        if image_count != expected["image_count"]:
            raise ValueError(f"Image count mismatch: expected {expected['image_count']}, found {image_count}.")

        return {
            "checks": {
                "mimetype_first_and_uncompressed": True,
                "xml_well_formed": True,
                "manifest_and_spine_resolve": True,
                "local_links_and_fragments_resolve": True,
                "no_duplicate_ids_within_documents": True,
                "no_visible_technical_markers": True,
                "no_consecutive_scene_breaks": True,
            },
            "chapter_xhtml_files": sum(1 for n in names if n.startswith("OEBPS/text/part-") and n.endswith(".xhtml")),
            "scene_breaks": scene_count,
            "footnotes": fn_count,
            "illustrations": image_count,
            "zip_entries": len(names),
            "epub_size_bytes": path.stat().st_size,
        }


def build(args: argparse.Namespace) -> dict:
    chunk_dir = Path(args.chunk_dir).resolve()
    report_path = Path(args.report).resolve()
    output_dir = Path(args.output_dir).resolve()
    if not chunk_dir.is_dir():
        raise FileNotFoundError(f"Chunk directory not found: {chunk_dir}")
    if not report_path.is_file():
        raise FileNotFoundError(f"Volume report not found: {report_path}")
    chunks = sorted([p for p in chunk_dir.glob("chunk_*rus.md") if p.is_file()], key=natural_key)
    if not chunks:
        chunks = sorted([p for p in chunk_dir.glob("chunk_*.md") if p.is_file() and not p.name.startswith("_")], key=natural_key)
    if not chunks:
        raise FileNotFoundError(f"No translated chunks found in {chunk_dir}")
    numbers = [natural_key(p)[0] for p in chunks]
    if len(numbers) != len(set(numbers)):
        raise ValueError("Duplicate chunk numbers in input directory.")

    report = report_path.read_text(encoding="utf-8-sig")
    state = {
        "citation_tags_removed": 0, "next_fn": 0, "next_ref": 0, "next_scene": 0,
        "next_image": 0, "next_heading": 0, "scene_count": 0,
        "definitions": {}, "refs": {}, "scene_tokens": set(), "image_tokens": {},
        "images": {}, "image_markers": [],
    }
    headings: list[dict] = []
    cleaned_chunks, source_hashes = [], {}
    for path in chunks:
        source_hashes[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
        clean = clean_chunk(path, args.volume, report, state)
        cleaned_chunks.append(add_heading_ids(clean, headings, state, path.name))

    sections = split_by_h2("\n\n".join(cleaned_chunks))
    if not sections:
        raise ValueError("No content after cleanup.")

    parts = []
    for i, section in enumerate(sections, 1):
        filename = f"text/part-{i:03d}.xhtml"
        heading_ids = set(re.findall(r"\{#(heading-\d{4})\}", section))
        for h in headings:
            if h["id"] in heading_ids:
                h["href"] = f"{filename}#{h['id']}"
        h2 = next((h for h in headings if h["id"] in heading_ids and h["level"] == 2), None)
        parts.append({
            "path": "OEBPS/" + filename,
            "title": h2["title"] if h2 else f"Продолжение — том {args.volume} (пробный фрагмент)",
            "text": section,
        })
    for h in headings:
        if "href" not in h:
            raise ValueError(f"Heading not assigned to XHTML: {h['title']}")

    md = markdown.Markdown(extensions=["extra", "sane_lists"], output_format="xhtml")
    entries: dict[str, bytes] = {}
    entries["META-INF/container.xml"] = (
        '<?xml version="1.0" encoding="utf-8"?>'
        f'<container xmlns="{CONTAINER}" version="1.0"><rootfiles>'
        '<rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml" />'
        '</rootfiles></container>'
    ).encode()
    entries["OEBPS/styles/book.css"] = (
        "html { writing-mode: horizontal-tb; }\n"
        "body { margin: 1em; hyphens: none; }\n"
        "p { margin: 0 0 0.7em 0; text-indent: 0; }\n"
        "h1 { font-size: 1.55em; text-align: center; margin: 2em 0 1em; }\n"
        "h2 { font-size: 1.3em; font-weight: 700; }\n"
        "h3 { font-size: 1.15em; font-weight: 700; margin-top: 1.1em; }\n"
        "h1 + p, h2 + p, h3 + p { margin-top: 0.6em; }\n"
        ".scene-break { text-align: center; margin: 1.2em 0; text-indent: 0; }\n"
        "figure.illustration { margin: 1em 0; padding: 0; text-align: center; page-break-inside: avoid; }\n"
        "figure.illustration img { max-width: 100%; height: auto; display: block; margin: 0 auto; }\n"
        ".footnotes { margin-top: 2em; border-top: 1px solid currentColor; padding-top: 0.8em; }\n"
        ".footnotes aside { font-size: 0.9em; margin: 0.8em 0; }\n"
        ".footnotes a { text-decoration: none; }\n"
        ".level-3 { margin-left: 1.2em; }\n"
        ".title-page { text-align: center; margin-top: 20%; }\n"
        ".title-page .subtitle { font-size: 1.2em; }\n"
        ".title-page .scope-note { font-size: 0.9em; margin-top: 2em; }\n"
    ).encode()

    chunk_label = ", ".join(p.stem.replace("rus", "") for p in chunks)
    titlepage_body = (
        '<main class="title-page"><h1>SukaSuka / SukaMoca</h1>'
        f'<p class="subtitle">Том {args.volume} — пробный фрагмент</p>'
        f'<p>Переведённые чанки: {html.escape(chunk_label)}</p>'
        '<p class="scope-note">Это не полный том. Включены только переведённые фрагменты из доступных чанков.</p></main>'
    )
    entries["OEBPS/text/titlepage.xhtml"] = xhtml_doc(
        f"SukaMoca — Том {args.volume} (пробный фрагмент)", titlepage_body
    )

    for part in parts:
        section = part["text"]
        rendered = md.reset().convert(section)
        for token in state["scene_tokens"]:
            rendered = rendered.replace(f"<p>{token}</p>", '<p class="scene-break">* * *</p>')
        for token, resource in state["image_tokens"].items():
            if token in section:
                rendered = rendered.replace(
                    f"<p>{token}</p>",
                    '<figure class="illustration"><img src="../images/'
                    + html.escape(resource, quote=True)
                    + '" alt="Иллюстрация из оригинального издания" /></figure>',
                )

        local_refs = [token for token in state["refs"] if token in section]
        for token in local_refs:
            info = state["refs"][token]
            # Notes live in a separate XHTML document. This gives readers a real,
            # visible destination even when they do not implement popup footnotes.
            info["source_href"] = f'{Path(part["path"]).name}#{info["ref_id"]}'
            rendered = rendered.replace(
                token,
                f'<a epub:type="noteref" role="doc-noteref" id="{info["ref_id"]}" '
                f'href="notes.xhtml#{info["uid"]}">{info["display"]}</a>',
            )

        if any(t in rendered for t in state["scene_tokens"] | set(state["image_tokens"]) | set(state["refs"])):
            raise ValueError(f"Unresolved placeholder remains in {part['path']}.")
        entries[part["path"]] = xhtml_doc(part["title"], rendered)

    if state["definitions"]:
        note_asides = []
        for uid, fn in state["definitions"].items():
            note_html = markdown.markdown(fn["definition"], extensions=["extra"])
            references = [
                info for info in state["refs"].values()
                if info["uid"] == uid and "source_href" in info
            ]
            backlinks = " ".join(
                f'<a epub:type="backlink" role="doc-backlink" '
                f'href="{html.escape(info["source_href"], quote=True)}">↩</a>'
                for info in references
            )
            if "</p>" in note_html:
                note_html = note_html.replace("</p>", f" {backlinks}</p>", 1)
            else:
                note_html += f"<p>{backlinks}</p>"
            note_asides.append(
                f'<aside epub:type="footnote" role="doc-footnote" id="{uid}">{note_html}</aside>'
            )
        notes_body = (
            '<main><section class="footnotes" epub:type="endnotes" role="doc-endnotes">'
            '<h1>Примечания</h1>' + "".join(note_asides) + '</section></main>'
        )
        entries["OEBPS/text/notes.xhtml"] = xhtml_doc("Примечания", notes_body)

    for resource, source_path in state["images"].items():
        entries[f"OEBPS/images/{resource}"] = source_path.read_bytes()

    toc_items = []
    for h in headings:
        level_class = "level-3" if h["level"] == 3 else "level-2"
        toc_items.append(
            f'<li class="{level_class}"><a href="{html.escape(h["href"], quote=True)}">'
            f'{html.escape(h["title"])}</a></li>'
        )
    if state["definitions"]:
        toc_items.append('<li><a href="text/notes.xhtml">Примечания</a></li>')
    nav = (
        '<?xml version="1.0" encoding="utf-8"?>'
        f'<html xmlns="{XHTML}" xmlns:epub="{EPUB}" lang="ru" xml:lang="ru">'
        '<head><meta charset="utf-8" /><title>Содержание</title>'
        '<link rel="stylesheet" type="text/css" href="styles/book.css" /></head>'
        '<body><nav epub:type="toc" id="toc"><h1>Содержание</h1><ol>'
        + "".join(toc_items) + '</ol></nav></body></html>'
    )
    ET.fromstring(nav.encode("utf-8"))
    entries["OEBPS/nav.xhtml"] = nav.encode("utf-8")

    digest = hashlib.sha256("".join(source_hashes[n] for n in sorted(source_hashes)).encode("ascii")).hexdigest()
    identifier = f"urn:uuid:{uuid.UUID(digest[:32])}"
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest = [
        ('nav', 'nav.xhtml', 'application/xhtml+xml', 'nav'),
        ('css', 'styles/book.css', 'text/css', None),
        ('titlepage', 'text/titlepage.xhtml', 'application/xhtml+xml', None),
    ]
    manifest += [
        (f"part{i:03d}", part["path"].replace("OEBPS/", ""), "application/xhtml+xml", None)
        for i, part in enumerate(parts, 1)
    ]
    if state["definitions"]:
        manifest.append(("notes", "text/notes.xhtml", "application/xhtml+xml", None))
    for i, resource in enumerate(sorted(state["images"]), 1):
        ext = Path(resource).suffix.lower()
        media = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}.get(ext)
        if not media:
            raise ValueError(f"Unsupported image format: {resource}")
        manifest.append((f"image{i:03d}", f"images/{resource}", media, None))
    manifest_xml = "".join(
        f'<item id="{ident}" href="{html.escape(href, quote=True)}" media-type="{media}"'
        + (f' properties="{props}"' if props else "") + " />"
        for ident, href, media, props in manifest
    )
    spine_xml = (
        '<itemref idref="titlepage" />'
        + "".join(f'<itemref idref="part{i:03d}" />' for i in range(1, len(parts) + 1))
        + ('<itemref idref="notes" />' if state["definitions"] else "")
    )
    opf = (
        '<?xml version="1.0" encoding="utf-8"?>'
        f'<package xmlns="{OPF}" xmlns:dc="{DC}" version="3.0" unique-identifier="pub-id" '
        'xml:lang="ru" prefix="dcterms: http://purl.org/dc/terms/">'
        '<metadata>'
        f'<dc:identifier id="pub-id">{identifier}</dc:identifier>'
        f'<dc:title>SukaSuka / SukaMoca — Том {args.volume} (пробный фрагмент)</dc:title>'
        '<dc:language>ru</dc:language><dc:creator>枯野 瑛</dc:creator>'
        f'<meta property="dcterms:modified">{modified}</meta>'
        '</metadata><manifest>' + manifest_xml + '</manifest><spine>' + spine_xml + '</spine></package>'
    )
    ET.fromstring(opf.encode("utf-8"))
    entries["OEBPS/content.opf"] = opf.encode("utf-8")

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    epub_path = output_dir / f"SukaMoca_v{args.volume}_ru_sample.epub"
    with zipfile.ZipFile(epub_path, "w") as zf:
        zf.writestr("mimetype", MIMETYPE, compress_type=zipfile.ZIP_STORED)
        for name in sorted(entries):
            zf.writestr(name, entries[name], compress_type=zipfile.ZIP_DEFLATED)

    check = validate_epub(epub_path, {
        "scene_count": state["scene_count"],
        "footnote_count": len(state["definitions"]),
        "image_count": len(state["images"]),
    })
    result = {
        "title": f"SukaSuka / SukaMoca — том {args.volume}, пробный фрагмент",
        "scope": "partial_sample_not_full_volume",
        "input_chunks": [p.name for p in chunks],
        "input_sha256": source_hashes,
        "chat_citation_tags_removed": state["citation_tags_removed"],
        "scene_breaks": state["scene_count"],
        "illustration_resources": sorted(state["images"]),
        "image_markers": list(state["image_markers"].values()) if isinstance(state["image_markers"], dict) else state["image_markers"],
        "footnotes": [
            {"id": info["uid"], "source_chunk": info["source_chunk"], "text": info["definition"]}
            for info in state["definitions"].values()
        ],
        "headings": headings,
        "note": "Only translated chunks present in the input folder are included; missing chapters are not fabricated.",
        **check,
    }
    (output_dir / "SukaMoca_v4_ru_sample_report.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"\nEPUB created: {epub_path}")


def validate_epub(path: Path, expected: dict) -> dict:
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        if not names or names[0] != "mimetype":
            raise ValueError("mimetype is not the first ZIP entry.")
        if zf.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            raise ValueError("mimetype is compressed.")
        if zf.read("mimetype").decode("ascii") != MIMETYPE:
            raise ValueError("Bad mimetype payload.")
        entries = set(names)
        roots, ids = {}, {}
        for name in names:
            if name.endswith((".xhtml", ".opf", ".xml")):
                root = ET.fromstring(zf.read(name))
                roots[name] = root
                ids[name] = set()
                for node in root.iter():
                    ident = node.attrib.get("id")
                    if ident:
                        if ident in ids[name]:
                            raise ValueError(f"Duplicate id {ident} in {name}.")
                        ids[name].add(ident)

        package = roots.get("OEBPS/content.opf")
        if package is None:
            raise ValueError("Missing content.opf.")
        ns = {"opf": OPF}
        manifest = package.findall("./opf:manifest/opf:item", ns)
        manifest_ids = {item.attrib["id"] for item in manifest}
        for item in manifest:
            target = posixpath.normpath(posixpath.join("OEBPS", item.attrib["href"]))
            if target not in entries:
                raise ValueError(f"Missing manifest resource: {target}")
        for ref in package.findall("./opf:spine/opf:itemref", ns):
            if ref.attrib.get("idref") not in manifest_ids:
                raise ValueError(f"Unknown spine idref: {ref.attrib.get('idref')}")

        for name, root in roots.items():
            if not name.endswith(".xhtml"):
                continue
            for node in root.iter():
                for attr in ("href", "src"):
                    value = node.attrib.get(attr)
                    if not value:
                        continue
                    parsed = urlsplit(value)
                    if parsed.scheme or parsed.netloc:
                        continue
                    target = name
                    if parsed.path:
                        target = posixpath.normpath(posixpath.join(posixpath.dirname(name), parsed.path))
                        if target not in entries:
                            raise ValueError(f"Broken local link in {name}: {value}")
                    if parsed.fragment and parsed.fragment not in ids.get(target, set()):
                        raise ValueError(f"Broken fragment in {name}: {value}")

        visible, scenes, footnotes, images = [], 0, 0, 0
        for name, root in roots.items():
            if not name.startswith("OEBPS/text/") or not name.endswith(".xhtml") or name.endswith("titlepage.xhtml"):
                continue
            visible.append("".join(root.itertext()))
            scenes += len(root.findall(f".//{{{XHTML}}}p[@class='scene-break']"))
            footnotes += len(root.findall(f".//{{{XHTML}}}aside[@{{{EPUB}}}type='footnote']"))
            images += len(root.findall(f".//{{{XHTML}}}img"))
            for body in root.findall(f".//{{{XHTML}}}body"):
                prev = False
                for child in list(body):
                    now = child.tag == f"{{{XHTML}}}p" and child.attrib.get("class") == "scene-break"
                    if now and prev:
                        raise ValueError(f"Adjacent scene breaks in {name}.")
                    prev = now
        text = "\n".join(visible)
        if re.search(r"\[\[EPUB_IMAGE:|〔[^〕]*〕|\[пауза\]|\[cite:|\bВ глоссарий\b|XSCENE\d{6}X|XIMAGE\d{6}X|XFNREF\d{6}X", text):
            raise ValueError("Technical marker remains in visible text.")
        for label, actual, want in (
            ("scene breaks", scenes, expected["scene_count"]),
            ("footnotes", footnotes, expected["footnote_count"]),
            ("illustrations", images, expected["image_count"]),
        ):
            if actual != want:
                raise ValueError(f"{label} mismatch: expected {want}, found {actual}.")
        return {
            "checks": {
                "mimetype_first_and_uncompressed": True,
                "xml_well_formed": True,
                "manifest_and_spine_resolve": True,
                "local_links_and_fragments_resolve": True,
                "no_duplicate_ids_within_documents": True,
                "no_visible_technical_markers": True,
                "no_adjacent_scene_breaks": True,
            },
            "chapter_xhtml_files": sum(1 for n in names if n.startswith("OEBPS/text/part-") and n.endswith(".xhtml")),
            "scene_breaks": scenes,
            "footnotes": footnotes,
            "illustrations": images,
            "zip_entries": len(names),
            "epub_size_bytes": path.stat().st_size,
        }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build and validate a reflowable EPUB 3 sample.")
    parser.add_argument("--volume", type=int, default=4)
    parser.add_argument("--chunk-dir", default="translated chunks")
    parser.add_argument("--report", default="completed_volumes/volume4_report.md")
    parser.add_argument("--output-dir", default="dist")
    build(parser.parse_args())


if __name__ == "__main__":
    main()
