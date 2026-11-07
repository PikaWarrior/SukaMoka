#!/usr/bin/env python3
"""Extract English WorldEnd2 EPUB volumes into ordered Markdown for reference.

Preserves source wording, OPF spine order, headings, emphasis and image occurrences.
Does not translate, OCR images, or copy publisher CSS.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import posixpath
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from lxml import etree

OPF = "http://www.idpf.org/2007/opf"
DC = "http://purl.org/dc/elements/1.1/"
NS = {"opf": OPF, "dc": DC}
SKIP_DOCS = {"toc.xhtml", "nav.xhtml"}
BLOCK_TAGS = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "ul", "ol", "li", "hr"}
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data"}
BT = chr(96)


def md_code(value) -> str:
    return BT + str(value).replace(BT, "\\" + BT) + BT


def local_name(node) -> str:
    if not isinstance(getattr(node, "tag", None), str):
        return ""
    return etree.QName(node).localname.lower()


def parse_xml(path: Path):
    parser = etree.XMLParser(
        resolve_entities=False,
        load_dtd=False,
        no_network=True,
        recover=False,
        remove_comments=False,
    )
    return etree.parse(str(path), parser)


class EnglishExtractor:
    def __init__(self, volume: int, repo_root: Path, output_dir: Path):
        self.volume = volume
        self.repo_root = repo_root.resolve()
        self.source_dir = (self.repo_root / "raw" / "english-raw" / f"WorldEnd2-v{volume:02d}").resolve()
        self.oebps = self.source_dir / "OEBPS"
        self.output_dir = output_dir.resolve()
        self.manifest = []
        self.spine = []
        self.images = []
        self.warnings = []
        self.errors = []
        self.headings = []
        self.paragraph_count = 0
        self.language_values = set()
        self.title = ""
        self.authors = []
        self.links = []

    def resolve_href(self, base_dir: Path, href: str) -> Path | None:
        parsed = urlsplit(href)
        if parsed.scheme.lower() in EXTERNAL_SCHEMES or href.startswith("//"):
            return None
        if not parsed.path:
            return None
        target = (base_dir / unquote(parsed.path)).resolve()
        try:
            target.relative_to(self.source_dir)
        except ValueError:
            self.warnings.append(f"Local path escapes source root: {href}")
            return None
        return target

    def rel_source(self, path: Path) -> str:
        return path.resolve().relative_to(self.source_dir).as_posix()

    def load_package(self):
        opf_path = self.oebps / "package.opf"
        if not opf_path.is_file():
            raise RuntimeError(f"Missing English EPUB package: {opf_path}")
        tree = parse_xml(opf_path)

        titles = tree.xpath(".//dc:title", namespaces=NS)
        self.title = "".join(titles[0].itertext()).strip() if titles else f"WorldEnd2 Vol. {self.volume}"
        self.authors = [
            "".join(node.itertext()).strip()
            for node in tree.xpath(".//dc:creator", namespaces=NS)
            if "".join(node.itertext()).strip()
        ]
        languages = [x.strip() for x in tree.xpath(".//dc:language/text()", namespaces=NS) if x.strip()]
        if languages and not any(x.lower().startswith("en") for x in languages):
            self.warnings.append(f"OPF language metadata is {languages!r}, expected English.")

        by_id = {}
        for item in tree.xpath("./opf:manifest/opf:item", namespaces=NS):
            href = item.get("href", "")
            path = self.resolve_href(self.oebps, href)
            rec = {
                "id": item.get("id", ""),
                "href": href,
                "media_type": item.get("media-type", ""),
                "properties": item.get("properties", ""),
                "path": path,
                "exists": bool(path and path.is_file()),
            }
            self.manifest.append(rec)
            by_id[rec["id"]] = rec

        for itemref in tree.xpath("./opf:spine/opf:itemref", namespaces=NS):
            ident = itemref.get("idref", "")
            rec = by_id.get(ident)
            if not rec:
                self.errors.append(f"Spine idref has no manifest item: {ident}")
                continue
            self.spine.append(rec)

        if not self.spine:
            raise RuntimeError("English EPUB spine is empty or could not be resolved.")

        for rec in self.manifest:
            if not rec["exists"]:
                self.errors.append(f"Manifest resource missing: {rec['href']}")

        if not any("nav" in (item["properties"] or "").split() for item in self.manifest):
            self.warnings.append("EPUB3 navigation item is not declared in the manifest.")

    def image_marker(self, node, source_rel: str) -> str:
        src = node.get("src") or node.get("href") or node.get("{http://www.w3.org/1999/xlink}href") or ""
        if not src:
            self.warnings.append(f"Image without src in {source_rel}")
            return "[[EN_EPUB_IMAGE:missing-source]]"
        target = self.resolve_href((self.source_dir / source_rel).parent, src)
        if target is None:
            self.warnings.append(f"Unresolved image path in {source_rel}: {src}")
            return "[[EN_EPUB_IMAGE:unresolved]]"
        target_rel = self.rel_source(target)
        if not target.is_file():
            self.errors.append(f"Image file missing: {source_rel} -> {src}")
        occurrence = len(self.images) + 1
        marker = (
            f"[[EN_EPUB_IMAGE:v{self.volume:02d}:"
            f"{source_rel}:{target_rel}:occ-{occurrence:04d}]]"
        )
        self.images.append({
            "marker": marker,
            "source_xhtml": source_rel,
            "resource": target_rel,
            "alt": node.get("alt", ""),
            "exists": target.is_file(),
        })
        return marker

    def inline(self, node, source_rel: str) -> str:
        tag = local_name(node)
        if tag in {"script", "style", "nav"}:
            return ""
        if tag in {"img", "image"}:
            return self.image_marker(node, source_rel)
        if tag == "br":
            return "  \n"
        text = node.text or ""
        for child in node:
            child_tag = local_name(child)
            if child_tag == "a":
                href = child.get("href", "")
                if href:
                    self.links.append({"source": source_rel, "href": href})
            text += self.inline(child, source_rel)
            if child.tail:
                text += child.tail
        if tag in {"em", "i"} and text.strip():
            return "*" + text + "*"
        if tag in {"strong", "b"} and text.strip():
            return "**" + text + "**"
        if tag == "code" and text.strip():
            return BT + text.replace(BT, "\\" + BT) + BT
        if tag == "sup" and text.strip():
            return "<sup>" + text + "</sup>"
        if tag == "sub" and text.strip():
            return "<sub>" + text + "</sub>"
        return text

    def render_blocks(self, node, source_rel: str) -> list[str]:
        tag = local_name(node)
        if tag in {"script", "style", "nav"}:
            return []
        if tag in {"img", "image"}:
            return [self.image_marker(node, source_rel)]
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            value = re.sub(r"\s+", " ", self.inline(node, source_rel)).strip()
            if not value:
                return []
            level = 2 if tag == "h1" else min(6, int(tag[1]) + 1)
            self.headings.append({"file": source_rel, "level": level, "title": value})
            return ["#" * level + " " + value]
        if tag == "p":
            value = self.inline(node, source_rel).strip()
            if value:
                self.paragraph_count += 1
                return [value]
            return []
        if tag == "hr":
            return ["---"]

        output: list[str] = []
        pending: list[str] = []

        def flush():
            value = "".join(pending).strip()
            pending.clear()
            if value:
                output.append(value)

        if node.text:
            pending.append(node.text)
        for child in node:
            child_tag = local_name(child)
            if child_tag in BLOCK_TAGS or child_tag in {"img", "image"}:
                flush()
                output.extend(self.render_blocks(child, source_rel))
            else:
                if child_tag == "a":
                    href = child.get("href", "")
                    if href:
                        self.links.append({"source": source_rel, "href": href})
                pending.append(self.inline(child, source_rel))
            if child.tail:
                pending.append(child.tail)
        flush()

        if tag == "li":
            return ["- " + item for item in output]
        if tag == "blockquote":
            return ["> " + item.replace("\n", "\n> ") for item in output]
        return output

    def extract_document(self, rec) -> list[str]:
        path = rec["path"]
        if path is None or not path.is_file():
            return []
        source_rel = self.rel_source(path)
        try:
            tree = parse_xml(path)
        except etree.XMLSyntaxError as exc:
            self.errors.append(f"XHTML parse error in {source_rel}: {exc}")
            return []
        html_root = tree.getroot()
        lang = html_root.get("lang") or html_root.get("{http://www.w3.org/XML/1998/namespace}lang")
        if lang:
            self.language_values.add(lang)
            if not lang.lower().startswith("en"):
                warning = f"XHTML language attribute is {lang!r} in {source_rel}, while the OPF declares English."
                if warning not in self.warnings:
                    self.warnings.append(warning)
        bodies = tree.xpath("//*[local-name()='body']")
        if not bodies:
            self.warnings.append(f"No body element in {source_rel}")
            return []
        return self.render_blocks(bodies[0], source_rel)

    def build_markdown(self) -> str:
        blocks = [
            f"<!-- English source extracted from {self.source_dir.name}; wording is unedited. -->",
            f"# {self.title}",
            "",
            f"<!-- Authors: {', '.join(self.authors) if self.authors else 'not declared'} -->",
        ]
        story_started = False
        for rec in self.spine:
            href = (rec.get("href") or "").replace("\\", "/")
            basename = posixpath.basename(href)
            if basename in SKIP_DOCS:
                self.warnings.append(f"Navigation/contents XHTML excluded from main text to avoid duplicating chapter titles: {href}")
                continue
            if rec["media_type"] != "application/xhtml+xml":
                continue
            if basename.startswith("chapter") and not story_started:
                blocks.append("<!-- p-toc-english-frontmatter-end -->")
                story_started = True
            content = self.extract_document(rec)
            if content:
                blocks.extend(content)
        if not story_started:
            self.warnings.append("No chapter*.xhtml spine item found; frontmatter boundary marker was not placed.")
        return "\n\n".join(x for x in blocks if x is not None).strip() + "\n"

    def build_report(self, markdown_text: str) -> str:
        inventory = []
        for path in sorted(x for x in self.source_dir.rglob("*") if x.is_file()):
            rel = path.relative_to(self.source_dir).as_posix()
            data = path.read_bytes()
            inventory.append((rel, len(data), hashlib.sha256(data).hexdigest()))

        referenced = {x["resource"] for x in self.images}
        image_manifest = {
            self.rel_source(rec["path"])
            for rec in self.manifest
            if rec["path"] is not None and (rec["media_type"] or "").startswith("image/")
        }
        unreferenced_images = sorted(image_manifest - referenced)
        language_status = ", ".join(sorted(self.language_values)) or "none"
        rows = [
            f"# English EPUB extraction report — volume {self.volume}",
            "",
            "## Method and limits",
            "",
            "XHTML was parsed as XML in OPF spine order. Source wording was not translated, paraphrased, or normalized.",
            "The navigation/contents XHTML files are excluded from the main Markdown to avoid duplicating chapter titles. Cover, insert, title-page, chapter-art and in-text images are preserved as explicit markers.",
            "Text contained only inside raster images is not OCR-extracted and must be checked visually when relevant.",
            "",
            "## Metadata",
            "",
            f"- Title: {self.title}",
            f"- Authors: {', '.join(self.authors) if self.authors else 'not declared'}",
            "- OPF language metadata is checked for English.",
            f"- XHTML lang values found: {language_status}",
            f"- Main Markdown characters: {len(markdown_text):,}",
            f"- Text paragraphs: {self.paragraph_count:,}",
            f"- Headings: {len(self.headings):,}",
            f"- Image occurrences: {len(self.images):,}",
            "",
            "## Spine order",
            "",
            "| # | Manifest id | XHTML/resource | Media type | Status |",
            "|---:|---|---|---|---|",
        ]
        for i, rec in enumerate(self.spine, 1):
            path = self.rel_source(rec["path"]) if rec["path"] is not None else "(unresolved)"
            status = "present" if rec["exists"] else "MISSING"
            rows.append(f"| {i} | {md_code(rec['id'])} | {md_code(path)} | {rec['media_type']} | {status} |")
        rows += ["", "## Extracted headings", ""]
        rows += [
            f"- {md_code(item['file'])}: {'#' * item['level']} {item['title']}"
            for item in self.headings
        ] or ["No structural headings found."]
        rows += [
            "",
            "## Image occurrence map",
            "",
            "| # | Marker | Source XHTML | Image resource | Alt text | Exists |",
            "|---:|---|---|---|---|---|",
        ]
        for i, item in enumerate(self.images, 1):
            alt = item["alt"].replace("|", "\\|")
            rows.append(
                f"| {i} | {md_code(item['marker'])} | {md_code(item['source_xhtml'])} | "
                f"{md_code(item['resource'])} | {alt} | {'yes' if item['exists'] else 'NO'} |"
            )
        rows += ["", "## Manifest image resources without body markers", ""]
        rows += [f"- {md_code(item)}" for item in unreferenced_images] or ["None."]
        rows += [
            "",
            "## Internal and external links",
            "",
            "| Source XHTML | href |",
            "|---|---|",
        ]
        rows += [f"| {md_code(x['source'])} | {md_code(x['href'])} |" for x in self.links] or ["No links found in extracted body."]
        rows += [
            "",
            "## Source file inventory",
            "",
            "| Path | Bytes | SHA-256 |",
            "|---|---:|---|",
        ]
        rows += [f"| {md_code(path)} | {size} | {md_code(sha)} |" for path, size, sha in inventory]
        parse_errors = sum("XHTML parse error" in x for x in self.errors)
        rows += [
            "",
            "## Validation",
            "",
            f"- XHTML parse errors: {parse_errors}.",
            f"- Missing manifest/resources or images: {len(self.errors) - parse_errors}.",
            f"- Warnings: {len(self.warnings)}.",
            "",
            "### Errors",
            "",
        ]
        rows += [f"- {item}" for item in self.errors] or ["None."]
        rows += ["", "### Warnings", ""]
        rows += [f"- {item}" for item in self.warnings] or ["None."]
        return "\n".join(rows) + "\n"

    def run(self, overwrite: bool = False) -> dict:
        if not self.source_dir.is_dir():
            raise RuntimeError(f"English source folder not found: {self.source_dir}")
        self.load_package()
        markdown_text = self.build_markdown()
        report = self.build_report(markdown_text)

        markdown_path = self.output_dir / f"volume{self.volume}.md"
        report_path = self.output_dir / f"volume{self.volume}_report.md"
        if not overwrite:
            existing = [str(x) for x in (markdown_path, report_path) if x.exists()]
            if existing:
                raise RuntimeError("Refusing to overwrite: " + ", ".join(existing))

        self.output_dir.mkdir(parents=True, exist_ok=True)
        markdown_path.write_text(markdown_text, encoding="utf-8", newline="\n")
        report_path.write_text(report, encoding="utf-8", newline="\n")
        return {
            "volume": self.volume,
            "markdown_path": str(markdown_path),
            "report_path": str(report_path),
            "markdown_chars": len(markdown_text),
            "report_chars": len(report),
            "spine_items": len(self.spine),
            "paragraphs": self.paragraph_count,
            "headings": len(self.headings),
            "image_occurrences": len(self.images),
            "errors": len(self.errors),
            "warnings": len(self.warnings),
        }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Extract English WorldEnd2 EPUB XHTML into Markdown.")
    parser.add_argument("--volume", type=int, required=True, choices=(1, 2, 3))
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)
    if sys.version_info < (3, 10):
        print("Python 3.10+ is required.", file=sys.stderr)
        return 2
    output = args.output_dir or (args.repo_root / "completed_volumes" / "english")
    try:
        result = EnglishExtractor(args.volume, args.repo_root, output).run(args.overwrite)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if result["errors"]:
            return 1
        return 0
    except (RuntimeError, OSError, etree.XMLSyntaxError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
