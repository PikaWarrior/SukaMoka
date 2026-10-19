import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.extract_epub import Extractor


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class ExtractorIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        item = self.root / "raw" / "99" / "item"
        write(item / "standard.opf", """<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf"
         xmlns:dc="http://purl.org/dc/elements/1.1/" version="3.0">
  <metadata><dc:title>Test Book</dc:title><dc:language>ja</dc:language></metadata>
  <manifest>
    <item id="nav" href="navigation-documents.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="style" href="style/book.css" media-type="text/css"/>
    <item id="p-second" href="xhtml/p-second.xhtml" media-type="application/xhtml+xml"/>
    <item id="p-first" href="xhtml/p-first.xhtml" media-type="application/xhtml+xml"/>
    <item id="diagram" href="image/diagram.png" media-type="image/png"/>
  </manifest>
  <spine>
    <itemref idref="p-second"/>
    <itemref idref="p-first"/>
  </spine>
</package>
""")
        write(item / "navigation-documents.xhtml", """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
  <body><nav epub:type="toc"><ol>
    <li><a href="xhtml/p-second.xhtml#part-second">Second Part</a></li>
    <li><a href="xhtml/p-first.xhtml#part-first">First Part</a></li>
  </ol></nav></body>
</html>
""")
        write(item / "xhtml" / "p-second.xhtml", """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja"><head><title>Test Book</title></head>
<body><div class="main"><p id="part-second" title="Second Part">Second paragraph.</p>TAIL_AFTER_SECOND</div></body></html>
""")
        write(item / "xhtml" / "p-first.xhtml", """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja"><head><title>Test Book</title></head>
<body><div class="main">
<p id="part-first" title="First Part">記<ruby>記<rp>(</rp><rt>き</rt><rp>)</rp>憶<rt>おく</rt></ruby>。<span class="em-sesame">強調</span> <img src="../image/diagram.png" alt="glyph|pipe"/>. <a href="#footnote-1">脚注</a><span id="footnote-1">注</span></p>
<h2 id="heading-break">見出し1<br/>見出し2</h2>
<p>*literal* _literal_ ~~strike~~ &lt;tag&gt; &amp; entity</p>
<p># literal heading</p>
<p>1. literal numbered paragraph</p>
<p>===</p>
<p><ruby>外<ruby>内<rt>うち</rt></ruby><rt>そと</rt></ruby></p>
<p><br/></p>
<!-- comment text is omitted, but this tail must survive -->COMMENT_TAIL_VISIBLE
</div></body></html>
""")
        write(item / "style" / "book.css", "body { background-image: url('../image/diagram.png'); }\n")
        (item / "image").mkdir(parents=True, exist_ok=True)
        (item / "image" / "diagram.png").write_bytes(b"fixture, not a real image")

    def tearDown(self):
        self.temp.cleanup()

    def test_spine_order_ruby_emphasis_pauses_and_images(self):
        out = self.root / "output"
        extractor = Extractor(99, self.root, out)
        summary = extractor.run(dry_run=True)
        markdown = extractor.main_markdown()
        report = extractor.make_report()

        self.assertLess(markdown.index("Second paragraph."), markdown.index("記〔き〕憶〔おく〕"))
        self.assertIn("TAIL" + chr(92) + "_AFTER" + chr(92) + "_SECOND", markdown)
        self.assertIn("COMMENT" + chr(92) + "_TAIL" + chr(92) + "_VISIBLE", markdown)
        self.assertIn("[脚注](#footnote-1)", markdown)
        self.assertIn("<em>強調</em>", markdown)
        self.assertIn("[пауза]", markdown)
        self.assertIn("[[EPUB_IMAGE:v99:xhtml/p-first.xhtml:diagram.png:occ-01]]", markdown)
        self.assertIn("## 見出し1 見出し2", markdown)
        self.assertIn(r"\*literal\* \_literal\_", markdown)
        self.assertIn(r"\~\~strike\~\~ &lt;tag&gt; &amp; entity", markdown)
        self.assertIn(r"\===", markdown)
        self.assertIn(r"\# literal heading", markdown)
        self.assertIn(r"1\. literal numbered paragraph", markdown)
        self.assertIn("<ruby>外<ruby>内<rt>うち</rt></ruby><rt>そと</rt></ruby>", markdown)
        self.assertNotIn("記(〔き〕)", markdown)
        self.assertIn("Second Part", report)
        self.assertIn("style/book.css", report)
        self.assertIn("image/diagram.png", report)
        self.assertIn("alt", report)
        self.assertIn("em-sesame", report)
        self.assertEqual(summary["text_mismatches"], 0)
        self.assertEqual(summary["reading_mismatches"], 0)
        self.assertEqual(summary["ruby_warnings"], 1)  # nested ruby is deliberately flagged
        self.assertEqual(summary["parse_errors"], 0)
        self.assertEqual(summary["broken_links"], 0)
        self.assertEqual(summary["image_occurrences"], 1)

    def test_missing_fragment_is_reported(self):
        item = self.root / "raw" / "99" / "item"
        first = item / "xhtml" / "p-first.xhtml"
        source = first.read_text(encoding="utf-8")
        source = source.replace('href="#footnote-1"', 'href="#missing-anchor"')
        first.write_text(source, encoding="utf-8")
        extractor = Extractor(99, self.root, self.root / "output")
        summary = extractor.run(dry_run=True)
        self.assertEqual(summary["broken_links"], 1)
        self.assertIn("missing fragment id", extractor.make_report())

    def test_epub2_ncx_navigation(self):
        item = self.root / "raw" / "99" / "item"
        opf_path = item / "standard.opf"
        opf = opf_path.read_text(encoding="utf-8")
        opf = opf.replace(
            '<item id="nav" href="navigation-documents.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
            '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        )
        opf = opf.replace("<spine>", '<spine toc="ncx">')
        opf_path.write_text(opf, encoding="utf-8")
        write(item / "toc.ncx", """<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <navMap>
    <navPoint id="nav-1"><navLabel><text>Second Part</text></navLabel><content src="xhtml/p-second.xhtml#part-second"/></navPoint>
    <navPoint id="nav-2"><navLabel><text>First Part</text></navLabel><content src="xhtml/p-first.xhtml#part-first"/></navPoint>
  </navMap>
</ncx>
""")
        extractor = Extractor(99, self.root, self.root / "output")
        summary = extractor.run(dry_run=True)
        report = extractor.make_report()
        self.assertEqual(summary["text_mismatches"], 0)
        self.assertEqual(summary["broken_links"], 0)
        self.assertIn("First Part", report)
        self.assertIn("EPUB2 NCX", report)
        self.assertIn("toc.ncx", report)

    def test_no_overwrite_without_flag(self):
        out = self.root / "output"
        out.mkdir()
        (out / "volume99.md").write_text("keep this", encoding="utf-8")
        extractor = Extractor(99, self.root, out)
        with self.assertRaisesRegex(RuntimeError, "Refusing to overwrite"):
            extractor.run()

    def test_missing_manifest_file_fails_closed(self):
        item = self.root / "raw" / "99" / "item"
        (item / "image" / "diagram.png").unlink()
        extractor = Extractor(99, self.root, self.root / "out")
        with self.assertRaisesRegex(RuntimeError, "Manifest file missing"):
            extractor.run(dry_run=True)


if __name__ == "__main__":
    unittest.main()
