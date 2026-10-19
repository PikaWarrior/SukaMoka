#!/usr/bin/env python3
"""Lxml-based extractor for Japanese EPUB XHTML.

Install: python -m pip install -r tools/requirements.txt
Run: python tools/extract_epub.py --volume 5
Existing outputs are not replaced without --overwrite.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit
from lxml import etree

OPF = "http://www.idpf.org/2007/opf"
DC = "http://purl.org/dc/elements/1.1/"
NS = {"opf": OPF, "dc": DC}
BT = chr(96)
INDENT = re.compile(r"^[ \t\u3000]+")
CSS_URL = re.compile(r"""url\(\s*(['"]?)(.*?)\1\s*\)""", re.I)
SEMANTIC = {"b":"strong","strong":"strong","i":"em","em":"em","sup":"sup","sub":"sub","del":"del","s":"s","u":"u","code":"code","mark":"mark"}
WRAPPERS = set("html head title meta link body div section article main p span a br ruby rb rp rt img image svg g text path rect circle line polyline polygon defs use desc switch foreignObject tspan strong b em i sup sub del s u code mark".split())
EXTERNAL = {"http","https","data","mailto","tel","javascript"}

def kind(node):
    if isinstance(node, etree._Comment): return "#comment"
    if isinstance(node, etree._ProcessingInstruction): return "#pi"
    if isinstance(node, etree._Entity): return "#entity"
    if not isinstance(getattr(node, "tag", None), str): return "#other"
    return etree.QName(node).localname

def walk(node):
    yield node
    for child in node:
        yield from walk(child)

def parse(path):
    parser = etree.XMLParser(resolve_entities=False, load_dtd=False, no_network=True, recover=False,
                             remove_comments=False, remove_pis=False, strip_cdata=False)
    return etree.parse(str(path), parser)

def text_of(node):
    out = getattr(node, "text", None) or ""
    for child in node:
        if kind(child) not in {"#comment", "#pi"}: out += text_of(child)
        if child.tail: out += child.tail
    return out

def base_of(node, in_ruby=False):
    t = kind(node)
    if t in {"#comment", "#pi"}: return ""
    if t == "#entity": return str(node)
    current = in_ruby or t == "ruby"
    if t == "rt" and current: return ""
    if t in {"img","image"}: return ""
    out = "\n" if t == "br" else (getattr(node,"text",None) or "")
    for child in node:
        out += base_of(child,current)
        if child.tail: out += child.tail
    return out

def unindent(text):
    return INDENT.sub("", text, count=1)

def code(text):
    return BT + str(text).replace(BT, "\\" + BT) + BT

def table(text):
    return str(text if text is not None else "").replace("|",r"\|").replace("\r"," ").replace("\n"," ")

class Extractor:
    def __init__(self, volume, root, output_dir, allow_partial=False):
        self.volume = volume
        self.root = root.resolve()
        self.item = (self.root / "raw" / str(volume) / "item").resolve()
        self.output_dir = output_dir.resolve()
        self.allow_partial = allow_partial
        self.manifest, self.by_id, self.spine = [], {}, []
        self.docs, self.errors, self.warnings = {}, {}, []
        self.nav_path, self.nav_links = None, []
        self.nav_by_page = defaultdict(list)
        self.images, self.image_counts = [], Counter()
        self.references, self.css_refs, self.comments, self.pis = [], [], [], []
        self.unknown, self.ruby_issues, self.text_mismatches = [], [], []
        self.main_blocks, self.stats, self.inventory = [], {}, []
        self.p_count = self.empty_p = self.br_count = self.em_count = 0
        self.indent_removed = 0
        self.literal_brackets = 0
        self.left, self.right = "〔", "〕"
        self.title = ""

    def issue(self, message):
        if not self.allow_partial: raise RuntimeError(message)
        self.warnings.append(message)

    def rel(self, path):
        try: return path.resolve().relative_to(self.item).as_posix()
        except ValueError: return str(path)

    def resolve(self, base, href):
        if not href: return None
        u = urlsplit(href)
        if u.scheme.lower() in EXTERNAL or href.startswith("//"): return None
        if not u.path: return None
        target = (base / unquote(u.path)).resolve()
        try: target.relative_to(self.item)
        except ValueError:
            self.warnings.append("Local href escapes item root: " + href)
            return None
        return target

    def note_tree(self, rel, tree):
        for node in walk(tree.getroot()):
            if kind(node) == "#comment": self.comments.append((rel, tree.getpath(node), node.text or ""))
            elif kind(node) == "#pi": self.pis.append((rel, tree.getpath(node), str(node)))
            elif kind(node) == "#entity": self.warnings.append("Unresolved XML entity: " + rel + " " + str(node))

    def load_opf(self):
        path = self.item / "standard.opf"
        if not path.is_file(): raise RuntimeError("standard.opf missing: " + str(path))
        tree = parse(path)
        for node in tree.xpath("./opf:manifest/opf:item", namespaces=NS):
            href = node.get("href","")
            target = self.resolve(self.item,href)
            rec = dict(node.attrib)
            rec.update(path=target, relative=self.rel(target) if target else "", exists=bool(target and target.is_file()), referenced=False)
            if rec.get("id") in self.by_id: self.warnings.append("Duplicate manifest id: " + str(rec.get("id")))
            self.manifest.append(rec)
            self.by_id[rec.get("id")] = rec
        for node in tree.xpath("./opf:spine/opf:itemref", namespaces=NS):
            idref = node.get("idref","")
            rec = self.by_id.get(idref)
            if not rec: self.issue("spine idref lacks manifest entry: " + idref)
            self.spine.append({"idref":idref,"record":rec,"relative":rec.get("relative") if rec else None,"linear":node.get("linear","yes")})
        titles = tree.xpath(".//dc:title", namespaces=NS)
        self.title = text_of(titles[0]).strip() if titles else ""
        nav = [x for x in self.manifest if "nav" in x.get("properties","").split()]
        self.nav_path = nav[0].get("path") if nav else None
        if not self.nav_path and (self.item/"navigation-documents.xhtml").is_file():
            self.nav_path = self.item/"navigation-documents.xhtml"
            self.warnings.append("Navigation document found by conventional filename, not manifest nav property.")
        self.note_tree("standard.opf",tree)

    def load_nav(self):
        if not self.nav_path or not self.nav_path.is_file():
            self.warnings.append("Navigation document missing.")
            return
        rel = self.rel(self.nav_path)
        try: tree = parse(self.nav_path)
        except etree.XMLSyntaxError as exc:
            self.issue("Cannot parse nav document: " + str(exc)); return
        self.docs[rel] = tree
        self.note_tree(rel,tree)
        for a in tree.xpath("//*[local-name()='nav']//*[local-name()='a'][@href]"):
            href = a.get("href","")
            target = self.resolve(self.nav_path.parent,href)
            rec = {"source":rel,"href":href,"label":text_of(a).strip(),"target":self.rel(target) if target else "","fragment":urlsplit(href).fragment}
            self.nav_links.append(rec)
            if target: self.nav_by_page[rec["target"]].append(rec)

    def load_xhtml(self):
        spine_paths = {x["relative"] for x in self.spine if x["relative"]}
        nav_rel = self.rel(self.nav_path) if self.nav_path else ""
        for rec in [x for x in self.manifest if x.get("media-type")=="application/xhtml+xml"]:
            path = rec.get("path")
            if not path or not path.is_file():
                self.issue("Manifest XHTML missing: " + str(rec.get("href"))); continue
            rel = self.rel(path)
            try:
                was_loaded = rel in self.docs
                tree = self.docs[rel] if was_loaded else parse(path)
            except etree.XMLSyntaxError as exc:
                self.issue("Cannot parse XHTML " + rel + ": " + str(exc)); self.errors[rel]=str(exc); continue
            self.docs[rel] = tree
            if not was_loaded:
                self.note_tree(rel,tree)
        for item in self.spine:
            rel=item["relative"]
            if not rel: continue
            path=self.item/rel
            if not path.is_file():
                self.issue("Spine XHTML missing: " + rel); continue
            if rel not in self.docs:
                try: self.docs[rel]=parse(path);self.note_tree(rel,self.docs[rel])
                except etree.XMLSyntaxError as exc:
                    self.issue("Cannot parse spine XHTML " + rel + ": " + str(exc));self.errors[rel]=str(exc)
        self.extra_xhtml = [x for x in self.manifest if x.get("media-type")=="application/xhtml+xml" and x.get("relative") not in spine_paths and x.get("relative") != nav_rel]

    def scan_refs(self):
        for rec in self.manifest:
            if not rec["exists"]: self.issue("Manifest file missing: " + str(rec.get("href")))
        for rel,tree in self.docs.items():
            base=(self.item/rel).parent
            for n in walk(tree.getroot()):
                if not isinstance(getattr(n,"tag",None),str): continue
                for attr,val in n.attrib.items():
                    if etree.QName(attr).localname.lower() not in {"src","href","poster","data"}: continue
                    target=self.resolve(base,val)
                    if target is None: continue
                    item={"source":rel,"element":kind(n),"attribute":etree.QName(attr).localname,"href":val,"target":self.rel(target),"exists":target.is_file()}
                    self.references.append(item);self.mark_ref(item["target"])
                    if not item["exists"]:
                        self.issue("Referenced local resource missing: " + rel + " " + item["attribute"] + "=" + val + " -> " + item["target"])
        for rec in self.manifest:
            if rec.get("media-type")!="text/css" or not rec.get("path") or not rec["path"].is_file(): continue
            try: css=rec["path"].read_text(encoding="utf-8-sig")
            except UnicodeDecodeError:
                css=rec["path"].read_text(encoding="utf-8",errors="replace")
                self.warnings.append("CSS had replacement decoding: "+rec["relative"])
            for match in CSS_URL.finditer(css):
                href=match.group(2).strip();target=self.resolve(rec["path"].parent,href)
                if target is None: continue
                item={"source":rec["relative"],"href":href,"target":self.rel(target),"exists":target.is_file()}
                self.css_refs.append(item);self.mark_ref(item["target"])

    def mark_ref(self,path):
        for rec in self.manifest:
            if rec["relative"]==path:rec["referenced"]=True

    def add_image(self,node,page,pnum):
        href=node.get("src") or node.get("href") or node.get("{http://www.w3.org/1999/xlink}href") or node.get("xlink:href") or ""
        target=self.resolve((self.item/page).parent,href)
        res=self.rel(target) if target else (href or "(missing-href)")
        self.image_counts[page]+=1;occ=self.image_counts[page]
        marker="[[EPUB_IMAGE:v"+str(self.volume)+":xhtml/"+Path(page).name+":"+res+":occ-"+str(occ).zfill(2)+"]]"
        attrs={etree.QName(k).localname:v for k,v in node.attrib.items()}
        rec={"marker":marker,"source":page,"resource":res,"href":href,"occ":occ,"element":kind(node),"attributes":attrs,"classes":attrs.get("class","").split(),"before":"","after":"","paragraph":pnum}
        self.images.append(rec)
        return marker,rec

    def has_rt(self,node):
        return any(kind(x)=="rt" for x in walk(node))

    def render_text(self,text,state):
        if state.get("leading",True):
            cut=unindent(text);self.indent_removed+=len(text)-len(cut);text=cut
            if text:state["leading"]=False
        return {"md":text,"plain":text,"readings":[],"images":[]}

    def ruby_tokens(self,node):
        if node.text is not None:yield ("text",node.text)
        for child in node:
            if kind(child)=="rt":yield ("rt",child)
            elif self.has_rt(child):yield from self.ruby_tokens(child)
            else:yield ("node",child)
            if child.tail is not None:yield ("text",child.tail)

    def render_buffer(self,buffer,page,state,pnum):
        out={"md":"","plain":"","readings":[],"images":[]}
        for typ,obj in buffer:
            val=self.render_text(obj,state) if typ=="text" else self.render_node(obj,page,state,pnum,True)
            off=len(out["plain"]);out["md"]+=val["md"];out["plain"]+=val["plain"];out["readings"]+=val["readings"]
            out["images"] += [(im,off+pos) for im,pos in val["images"]]
        return out

    def render_node(self,node,page,state,pnum=None,in_ruby=False):
        t=kind(node)
        if t in {"#comment","#pi"}:return {"md":"","plain":"","readings":[],"images":[]}
        if t=="#entity":
            val=str(node);self.warnings.append("Unresolved entity rendered literally: "+page+" "+val)
            return {"md":val,"plain":val,"readings":[],"images":[]}
        if t=="rt" and not in_ruby:
            val=text_of(node);self.ruby_issues.append({"file":page,"path":node.getroottree().getpath(node),"issue":"rt outside ruby","text":val})
            return {"md":"<rt>"+val+"</rt>","plain":val,"readings":[],"images":[]}
        if t in {"img","image"}:
            marker,rec=self.add_image(node,page,pnum)
            return {"md":marker,"plain":"","readings":[],"images":[(rec,0)]}
        if t=="br":
            self.br_count+=1;return {"md":"  \n","plain":"\n","readings":[],"images":[]}
        if t=="ruby":
            out={"md":"","plain":"","readings":[],"images":[]};buffer=[];seen=0
            for typ,obj in self.ruby_tokens(node):
                if typ!="rt":buffer.append((typ,obj));continue
                base=self.render_buffer(buffer,page,state,pnum);reading=text_of(obj)
                if not base["plain"] and not base["md"]:self.ruby_issues.append({"file":page,"path":obj.getroottree().getpath(obj),"issue":"rt without preceding base","text":reading})
                off=len(out["plain"]);out["md"]+=base["md"]+self.left+reading+self.right;out["plain"]+=base["plain"]
                out["readings"]+=base["readings"]+[reading];out["images"] += [(im,off+pos) for im,pos in base["images"]]
                buffer=[];seen+=1
            if buffer:
                base=self.render_buffer(buffer,page,state,pnum)
                if seen and (base["plain"] or base["md"]):self.ruby_issues.append({"file":page,"path":node.getroottree().getpath(node),"issue":"base after final rt","text":base["plain"]})
                off=len(out["plain"]);out["md"]+=base["md"];out["plain"]+=base["plain"];out["readings"]+=base["readings"]
                out["images"] += [(im,off+pos) for im,pos in base["images"]]
            return out
        out={"md":"","plain":"","readings":[],"images":[]}
        if getattr(node,"text",None):
            a=self.render_text(node.text,state);out["md"]+=a["md"];out["plain"]+=a["plain"]
        for child in node:
            off=len(out["plain"]);piece=self.render_node(child,page,state,pnum,False)
            out["md"]+=piece["md"];out["plain"]+=piece["plain"];out["readings"]+=piece["readings"]
            out["images"] += [(im,off+pos) for im,pos in piece["images"]]
            if child.tail:
                tail=self.render_text(child.tail,state);off=len(out["plain"]);out["md"]+=tail["md"];out["plain"]+=tail["plain"]
                out["images"] += [(im,off+pos) for im,pos in tail["images"]]
        classes=set((node.get("class") or "").split())
        if t=="span" and "em-sesame" in classes:
            self.em_count+=1;out["md"]="<em>"+out["md"]+"</em>"
        elif t in SEMANTIC:
            tag=SEMANTIC[t];out["md"]="<"+tag+">"+out["md"]+"</"+tag+">"
        elif t=="a" and node.get("href"):
            out["md"]="["+out["md"]+"]("+node.get("href")+")"
        elif t not in WRAPPERS and not t.startswith("#"):
            self.unknown.append({"file":page,"path":node.getroottree().getpath(node),"tag":t,"attributes":dict(node.attrib),"text":out["plain"][:160]})
        return out

    def render_p(self,node,page,pnum):
        r=self.render_node(node,page,{"leading":True},pnum)
        expected=unindent(base_of(node))
        if r["plain"]!=expected:self.text_mismatches.append({"file":page,"p":pnum,"source":expected[:160],"rendered":r["plain"][:160]})
        for im,off in r["images"]:
            im["paragraph"]=pnum;im["before"]=r["plain"][max(0,off-60):off].replace("\n"," ");im["after"]=r["plain"][off:off+60].replace("\n"," ")
        empty=not r["plain"].strip() and not r["md"].strip()
        classes=set((node.get("class") or "").split())
        result="[пауза]" if empty else r["md"]
        if empty:self.empty_p+=1
        elif "font-1em30" in classes:result="## "+result
        elif "font-1em10" in classes:result="### "+result
        elif Path(page).stem in {"p-titlepage","titlepage"} and r["plain"].strip()==self.title:result="# "+result
        self.p_count+=1
        return result

    def audit_inline(self,node,in_ruby=False):
        t=kind(node)
        if t in {"#comment","#pi"}:return ""
        if t=="#entity":return str(node)
        if t=="rt" and in_ruby:return ""
        if t in {"img","image"}:
            href=node.get("src") or node.get("href") or node.get("{http://www.w3.org/1999/xlink}href") or ""
            return "[image: "+(unquote(urlsplit(href).path).split("/")[-1] or "missing-href")+"]"
        if t=="br":return "\n"
        if t=="ruby":
            out="";buf=[]
            for typ,obj in self.ruby_tokens(node):
                if typ=="rt":
                    base="".join(v if k=="text" else self.audit_inline(v,True) for k,v in buf)
                    out+=base+self.left+text_of(obj)+self.right;buf=[]
                else:buf.append((typ,obj))
            out+="".join(v if k=="text" else self.audit_inline(v,True) for k,v in buf)
            return out
        out=getattr(node,"text",None) or ""
        for child in node:
            out+=self.audit_inline(child,in_ruby or t=="ruby")
            if child.tail:out+=child.tail
        classes=set((node.get("class") or "").split())
        if t=="span" and "em-sesame" in classes:return "<em>"+out+"</em>"
        if t in SEMANTIC:
            tag=SEMANTIC[t];return "<"+tag+">"+out+"</"+tag+">"
        if t=="a" and node.get("href"):return "["+out+"]("+node.get("href")+")"
        return out

    def audit_body(self,tree):
        bodies=tree.xpath("//*[local-name()='body']")
        if not bodies:return "[body missing]"
        out=[]
        def visit(node):
            t=kind(node)
            if t in {"#comment","#pi"}:return
            if t in {"p","h1","h2","h3","h4","h5","h6"}:
                val=self.audit_inline(node);out.append(val if val.strip() else "[empty paragraph]");return
            if t in {"img","image","svg"}:
                val=self.audit_inline(node)
                if val:out.append(val)
                return
            if getattr(node,"text",None) and node.text.strip():out.append(node.text)
            for child in node:
                visit(child)
                if child.tail and child.tail.strip():out.append(child.tail)
        visit(bodies[0])
        return "\n\n".join(out)

    def is_duplicate_toc(self,tree,rel):
        if not any(x in Path(rel).stem.lower() for x in ("toc","contents")):return False
        bodies=tree.xpath("//*[local-name()='body']")
        if not bodies:return False
        targets=set()
        for a in bodies[0].xpath(".//*[local-name()='a'][@href]"):
            target=self.resolve((self.item/rel).parent,a.get("href",""))
            if target and target.suffix.lower() in {".xhtml",".html",".htm"}:targets.add(self.rel(target))
        return len(targets)>=2

    def nav_heading(self,rel,tree):
        for rec in self.nav_by_page.get(rel,[]):
            frag=rec["fragment"]
            if frag:
                found=tree.xpath("//*[@id=$frag]",frag=frag)
                if not found:self.warnings.append("Navigation target missing: "+rel+"#"+frag);continue
                target=found[0];title=target.get("title")
                if title and not unindent(base_of(target)).strip():return title
            elif "colophon" in Path(rel).stem.lower() and rec["label"]=="奥付":return rec["label"]
        return None

    def render_spine(self):
        for item in self.spine:
            rel=item.get("relative");tree=self.docs.get(rel) if rel else None
            if tree is None:
                self.main_blocks.append("<!-- SOURCE NOT PARSED: "+str(rel or item["idref"])+"; see report -->");continue
            if self.is_duplicate_toc(tree,rel):
                self.main_blocks.append("<!-- "+rel+" is a repeated TOC; its text and link targets are retained in the report. -->");continue
            heading=self.nav_heading(rel,tree)
            if heading:self.main_blocks.append("## "+heading)
            bodies=tree.xpath("//*[local-name()='body']")
            if not bodies:
                self.warnings.append("Body element missing: "+rel);self.main_blocks.append("<!-- SOURCE HAS NO BODY: "+rel+" -->");continue
            blocks=[];pnum=[0]
            def visit(container):
                t=kind(container)
                if t in {"#comment","#pi"}:return
                if t in {"p","h1","h2","h3","h4","h5","h6"}:
                    pnum[0]+=1;blocks.append(self.render_p(container,rel,pnum[0]));return
                if t in {"img","image","svg"}:
                    result=self.render_node(container,rel,{"leading":True})
                    if result["md"]:blocks.append(result["md"])
                    return
                if getattr(container,"text",None) and container.text.strip():
                    blocks.append(self.render_text(container.text,{"leading":True})["md"])
                for child in container:
                    if any(kind(x) in {"p","h1","h2","h3","h4","h5","h6"} for x in walk(child)):
                        visit(child)
                    else:
                        result=self.render_node(child,rel,{"leading":True})
                        if result["md"].strip():blocks.append(result["md"])
                    # Element tails belong to the parent's mixed content, even when recursion was used.
                    if not isinstance(child,etree._Comment) and child.tail and child.tail.strip():
                        blocks.append(self.render_text(child.tail,{"leading":True})["md"])
            visit(bodies[0])
            self.stats[rel]={"p":len(bodies[0].xpath(".//*[local-name()='p']")),
                "ruby":len(bodies[0].xpath(".//*[local-name()='ruby']")),"rt":len(bodies[0].xpath(".//*[local-name()='rt']")),
                "images":len(bodies[0].xpath(".//*[local-name()='img' or local-name()='image']")),
                "br":len(bodies[0].xpath(".//*[local-name()='br']"))}
            self.main_blocks.extend(blocks)

    def inventory_files(self):
        result=[]
        for p in sorted(x for x in self.item.rglob("*") if x.is_file()):
            data=p.read_bytes()
            result.append({"path":self.rel(p),"bytes":len(data),"sha":hashlib.sha256(data).hexdigest()})
        self.inventory=result;disk={x["path"] for x in result}
        for rec in self.manifest:
            if rec["relative"] not in disk:rec["exists"]=False

    def main_markdown(self):
        intro="Служебное пояснение, не часть книги: запись X"+self.left+"Y"+self.right+" передаёт основное написание X и авторское чтение Y. Учитывать оба слоя; это не два последовательных слова. <em>…</em> обозначает авторское выделение."
        note="<!-- Японский исходник не переведён и не редактировался. EPUB_IMAGE и [пауза] — технические маркеры; полная карта и журнал исключений находятся в volume"+str(self.volume)+"_report.md. -->"
        return "\n\n".join([intro,note]+[x for x in self.main_blocks if x is not None and x!=""])+"\n"

    def make_report(self):
        disk={x["path"] for x in self.inventory}
        spine_paths={x["relative"] for x in self.spine if x["relative"]}
        nav_rel=self.rel(self.nav_path) if self.nav_path else ""
        extra=[x for x in self.manifest if x.get("media-type")=="application/xhtml+xml" and x["relative"] not in spine_paths]
        unused=[x for x in self.manifest if not x["referenced"]]
        marked={x["resource"] for x in self.images}
        img_manifest={x["relative"] for x in self.manifest if str(x.get("media-type","")).startswith("image/")}
        unmarked=sorted(img_manifest-marked)
        non_manifest=sorted(x for x in disk if x not in {r["relative"] for r in self.manifest} and x!="standard.opf")
        rows=["# Отчёт об извлечении японского исходника — том "+str(self.volume),"",
            "## Метод и ограничения","",
            "Извлечение выполнено lxml/XML-парсером; внешние сущности и сетевой доступ отключены, автоматическое восстановление malformed XML запрещено. Японский текст не переводится и Unicode-нормализация не применяется.",
            "XML-разбор не заменяет проверку готового EPUB. Значение иллюстраций и gaiji автоматически не угадывается; непроверенное изображение отмечено как таковое.", "",
            "## Все файлы item/","",
            "| Путь | Байты | SHA-256 |","|---|---:|---|"]
        rows += ["| "+code(x["path"])+" | "+str(x["bytes"])+" | "+code(x["sha"])+" |" for x in self.inventory]
        rows += ["","## Полный manifest","",
            "| id | href | media-type | Файл найден | Локальная ссылка |","|---|---|---|---|---|"]
        rows += ["| "+table(x.get("id"))+" | "+code(x.get("href",""))+" | "+table(x.get("media-type"))+" | "+("да" if x["exists"] else "НЕТ")+" | "+("да" if x["referenced"] else "ссылка не найдена")+" |" for x in self.manifest]
        rows += ["","## Spine","",
            "| № | idref | XHTML | Статус | p | ruby | rt | img/image |","|---:|---|---|---|---:|---:|---:|---:|"]
        for i,x in enumerate(self.spine,1):
            rel=x.get("relative") or "(no manifest match)";st=self.stats.get(rel,{})
            status="XML error" if rel in self.errors else ("not parsed" if rel not in self.docs else ("TOC logged below, not repeated" if self.is_duplicate_toc(self.docs[rel],rel) else "parsed"))
            rows.append("| "+str(i)+" | "+code(x["idref"])+" | "+code(rel)+" | "+table(status)+" | "+str(st.get("p",0))+" | "+str(st.get("ruby",0))+" | "+str(st.get("rt",0))+" | "+str(st.get("images",0))+" |")
        rows += ["","## Навигационные ссылки","",
            "| Текст | href | Целевой файл |","|---|---|---|"]
        rows += ["| "+table(x["label"])+" | "+code(x["href"])+" | "+code(x["target"])+" |" for x in self.nav_links]
        rows += ["","## Проверки","",
            "- XHTML parse errors: "+str(len(self.errors))+".",
            "- Spine items: "+str(len(self.spine))+"; сопоставлены с manifest: "+str(sum(bool(x["record"]) for x in self.spine))+".",
            "- Абзацы p в основном потоке: "+str(self.p_count)+"; пустых p, отмеченных [пауза]: "+str(self.empty_p)+".",
            "- br-элементов: "+str(self.br_count)+"; em-sesame: "+str(self.em_count)+".",
            "- Маркеров изображений: "+str(len(self.images))+"; уникальных ресурсов в маркерах: "+str(len(marked))+".",
            "- Изображений manifest без маркера в spine XHTML: "+str(len(unmarked))+".",
            "- Расхождений текстового слоя абзацев: "+str(len(self.text_mismatches))+"; ruby warnings: "+str(len(self.ruby_issues))+".",
            "- Неизвестных элементов: "+str(len(self.unknown))+"; XML-комментариев: "+str(len(self.comments))+"; processing instructions: "+str(len(self.pis))+".",
            "- Литеральных символов 〔〕 вне rt: "+str(self.literal_brackets)+"; предупреждений: "+str(len(self.warnings))+".",
            "","### Расхождения текстового слоя",""]
        rows += ["- "+code(x["file"])+" p#"+str(x["p"])+": source="+table(x["source"])+"; rendered="+table(x["rendered"]) for x in self.text_mismatches] or ["Не обнаружены."]
        rows += ["","### Ruby warnings",""]
        rows += ["- "+code(x["file"])+" "+x["path"]+": "+table(x["issue"])+"; "+table(x["text"]) for x in self.ruby_issues] or ["Не обнаружены."]
        rows += ["","### Неизвестные элементы",""]
        rows += ["- "+code(x["file"])+" "+x["path"]+" <"+x["tag"]+"> attrs="+code(json.dumps(x["attributes"],ensure_ascii=False))+" text="+table(x["text"]) for x in self.unknown] or ["Не обнаружены."]
        rows += ["","### XML-комментарии и processing instructions",""]
        rows += ["- "+code(a)+" "+b+": "+table(c) for a,b,c in self.comments] or ["Комментарии не найдены."]
        rows += ["- PI "+code(a)+" "+b+": "+table(c) for a,b,c in self.pis]
        rows += ["","### CSS url() references",""]
        rows += ["- "+code(x["source"])+" url("+code(x["href"])+") -> "+code(x["target"])+("" if x["exists"] else " [missing]") for x in self.css_refs] or ["Локальные CSS-ссылки url() не найдены."]
        rows += ["","## Проверка локальных ссылок","",
            "| XHTML/CSS source | Href | Resolved path | Status |","|---|---|---|---|"]
        all_refs = self.references + self.css_refs
        if not all_refs:
            rows.append("Локальных ссылок на ресурсы не найдено.")
        for ref in all_refs:
            rows.append("| "+code(ref["source"])+" | "+code(ref["href"])+" | "+code(ref["target"])+" | "+("OK" if ref["exists"] else "MISSING")+" |")
        rows += ["","## Карта размещений изображений","",
            "Каждый маркер относится к отдельному occurrence. Ресурс восстанавливается из пути в таблице, позиция — по маркеру и исходному XHTML. Текст внутри изображений этим скриптом не распознаётся.", "",
            "| № | Маркер | Ресурс | XHTML-источник | Тип/статус | Контекст | Атрибуты |","|---:|---|---|---|---|---|---|"]
        for i,im in enumerate(self.images,1):
            clas="gaiji (класс XHTML; глиф не проверен)" if "gaiji" in im["classes"] else "изображение, визуально не проверено"
            rp="raw/"+str(self.volume)+"/item/"+im["resource"];xp="raw/"+str(self.volume)+"/item/"+im["source"]
            ctx=(im["before"]+" [IMAGE] "+im["after"]).strip()
            rows.append("| "+str(i)+" | "+code(im["marker"])+" | ["+code(rp)+"](https://github.com/PikaWarrior/SukaMoka/blob/main/"+rp+") | ["+code(xp)+"](https://github.com/PikaWarrior/SukaMoka/blob/main/"+xp+") | "+clas+" | "+table(ctx)+" | "+code(json.dumps(im["attributes"],ensure_ascii=False))+" |")
        rows += ["","## XHTML из manifest вне spine",""]
        if not extra:rows.append("Других XHTML, кроме navigation-документа, вне spine не найдено.")
        for rec in extra:
            rel=rec["relative"];rows += ["### "+code(rel),"","Причина: файл объявлен в manifest, но отсутствует в spine."]
            if rel==nav_rel:rows.append("Navigation document: ссылки отражены выше, названия использованы при восстановлении заголовков.")
            elif rel in self.docs:rows += ["","Читаемое тело для аудита:","","~~~text",self.audit_body(self.docs[rel]),"~~~"]
        rows += ["","## XHTML spine, не повторённый в основном потоке",""]
        excluded=[x for x in self.spine if x["relative"] in self.docs and self.is_duplicate_toc(self.docs[x["relative"]],x["relative"])]
        if not excluded:rows.append("Повторное текстовое оглавление с несколькими XHTML-ссылками не обнаружено.")
        for x in excluded:
            rel=x["relative"];rows += ["### "+code(rel),"","Причина: документ ссылается на несколько XHTML и дублирует заголовки. Полное читаемое содержимое сохранено ниже.","","~~~text",self.audit_body(self.docs[rel]),"~~~"]
        rows += ["","## Журнал пропусков и нерешённых элементов","",
            "| Категория | Число | Где описано |","|---|---:|---|",
            "| Manifest files missing | "+str(sum(not x["exists"] for x in self.manifest))+" | Manifest table/warnings |",
            "| Spine ids without manifest mapping | "+str(sum(not x["record"] for x in self.spine))+" | Spine table |",
            "| XHTML outside spine | "+str(len(extra))+" | Section above |",
            "| Manifest items without local reference | "+str(len(unused))+" | Manifest table |",
            "| Image resources without main-flow marker | "+str(len(unmarked))+" | Image map/resource audit |",
            "| Unmanifested files on disk | "+str(len(non_manifest))+" | "+(", ".join(non_manifest) if non_manifest else "none")+" |",
            "| Text-layer mismatches | "+str(len(self.text_mismatches))+" | Full list above |",
            "| Ruby warnings | "+str(len(self.ruby_issues))+" | Full list above |",
            "| Parse/resource warnings | "+str(len(self.warnings))+" | Full list below |",
            "","### Полный список предупреждений",""]
        rows += ["- "+table(x) for x in self.warnings] or ["Не обнаружены."]
        rows += ["","## Для будущей сборки EPUB","",
            "Не переносить старый CSS/fixed-layout/шрифты. Собрать reflowable EPUB по instructions/pasport proekta.md, восстановить ресурсы по EPUB_IMAGE-маркерам и выполнить EPUBCheck после упаковки."]
        return "\n".join(rows)+"\n"

    def run(self,overwrite=False,dry_run=False):
        if not self.item.is_dir():raise RuntimeError("Source folder missing: "+str(self.item))
        self.load_opf();self.load_nav();self.load_xhtml();self.scan_refs();self.inventory_files()
        for item in self.spine:
            rel=item["relative"]
            if rel and rel in self.docs:
                bodies=self.docs[rel].xpath("//*[local-name()='body']")
                if bodies:self.literal_brackets+=len(re.findall(r"[〔〕]",base_of(bodies[0])))
        if self.literal_brackets:
            visible="".join(base_of(self.docs[x["relative"]].xpath("//*[local-name()='body']")[0]) for x in self.spine if x["relative"] in self.docs and self.docs[x["relative"]].xpath("//*[local-name()='body']"))
            if "⟦" not in visible and "⟧" not in visible:self.left,self.right="⟦","⟧"
            else:self.warnings.append("Default and alternate ruby delimiters occur literally; ambiguous cases require HTML ruby.")
        self.render_spine()
        md=self.main_markdown();report=self.make_report()
        md_path=self.output_dir/("volume"+str(self.volume)+".md")
        report_path=self.output_dir/("volume"+str(self.volume)+"_report.md")
        if not dry_run:
            present=[x for x in (md_path,report_path) if x.exists()]
            if present and not overwrite:raise RuntimeError("Refusing to overwrite existing output(s): "+", ".join(map(str,present))+". Use --overwrite or --output-dir.")
            self.output_dir.mkdir(parents=True,exist_ok=True)
            md_path.write_text(md,encoding="utf-8",newline="\n");report_path.write_text(report,encoding="utf-8",newline="\n")
        return {"volume":self.volume,"output_markdown":str(md_path),"output_report":str(report_path),
            "markdown_chars":len(md),"report_chars":len(report),"spine_items":len(self.spine),
            "paragraphs":self.p_count,"empty_paragraphs":self.empty_p,"text_mismatches":len(self.text_mismatches),
            "ruby_warnings":len(self.ruby_issues),"image_occurrences":len(self.images),
            "parse_errors":len(self.errors),"warnings":len(self.warnings),"dry_run":dry_run}

def main(argv=None):
    ap=argparse.ArgumentParser(description="Extract Japanese EPUB XHTML in OPF spine order.")
    ap.add_argument("--volume",type=int,required=True,help="Volume number, e.g. 4 or 5.")
    ap.add_argument("--repo-root",type=Path,default=Path.cwd(),help="Repository root containing raw/<volume>/item.")
    ap.add_argument("--output-dir",type=Path,default=None,help="Output directory; defaults to repository root.")
    ap.add_argument("--allow-partial",action="store_true",help="Continue despite missing/unparseable files; record every issue.")
    ap.add_argument("--overwrite",action="store_true",help="Allow replacing existing output files.")
    ap.add_argument("--dry-run",action="store_true",help="Run checks without writing files.")
    args=ap.parse_args(argv);root=args.repo_root.resolve();out=(args.output_dir or root).resolve()
    try:result=Extractor(args.volume,root,out,args.allow_partial).run(args.overwrite,args.dry_run)
    except (RuntimeError,etree.XMLSyntaxError,OSError) as exc:
        print("ERROR: "+str(exc),file=sys.stderr);return 2
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if result["text_mismatches"] or result["ruby_warnings"] or result["parse_errors"]:
        print("WARNING: validation issues exist; inspect the report.",file=sys.stderr);return 1
    return 0

if __name__=="__main__":
    raise SystemExit(main())
