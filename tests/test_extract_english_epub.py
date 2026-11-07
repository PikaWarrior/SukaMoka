import tempfile
import unittest
from pathlib import Path

from tools.extract_english_epub import EnglishExtractor


class EnglishExtractorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.repo_root = Path(self.temp.name)
        self.source = self.repo_root / "raw" / "english-raw" / "WorldEnd2-v01" / "OEBPS"
        self.source.mkdir(parents=True)
        (self.source / "images").mkdir()
        (self.source / "images" / "cover.jpg").write_bytes(b"cover-image")
        (self.source / "images" / "chapter.jpg").write_bytes(b"chapter-image")

        (self.source / "package.opf").write_text(
            """<?xml version="1.0" encoding="utf-8"?>
            <package xmlns="http://www.idpf.org/2007/opf" version="3.0">
              <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
                <dc:title>English test volume</dc:title>
                <dc:creator>Test Author</dc:creator>
                <dc:language>en</dc:language>
              </metadata>
              <manifest>
                <item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>
                <item id="toc" href="toc.xhtml" media-type="application/xhtml+xml"/>
                <item id="chapter-art" href="chapter001.xhtml" media-type="application/xhtml+xml"/>
                <item id="chapter-text" href="chapter001a.xhtml" media-type="application/xhtml+xml"/>
                <item id="cover-image" href="images/cover.jpg" media-type="image/jpeg"/>
                <item id="chapter-image" href="images/chapter.jpg" media-type="image/jpeg"/>
              </manifest>
              <spine>
                <itemref idref="cover"/>
                <itemref idref="toc"/>
                <itemref idref="chapter-art"/>
                <itemref idref="chapter-text"/>
              </spine>
            </package>""",
            encoding="utf-8",
        )
        (self.source / "cover.xhtml").write_text(
            """<html xmlns="http://www.w3.org/1999/xhtml" lang="en"><body>
            <img src="images/cover.jpg" alt="Cover"/>
            </body></html>""",
            encoding="utf-8",
        )
        (self.source / "toc.xhtml").write_text(
            """<html xmlns="http://www.w3.org/1999/xhtml" lang="en"><body>
            <h1>Duplicate contents heading</h1><p>Duplicate table of contents text.</p>
            </body></html>""",
            encoding="utf-8",
        )
        (self.source / "chapter001.xhtml").write_text(
            """<html xmlns="http://www.w3.org/1999/xhtml" lang="en"><body>
            <img src="images/chapter.jpg" alt="Chapter illustration"/>
            </body></html>""",
            encoding="utf-8",
        )
        (self.source / "chapter001a.xhtml").write_text(
            """<html xmlns="http://www.w3.org/1999/xhtml" lang="en"><body>
            <h1>First Chapter</h1><h2>-chapter subtitle-</h2>
            <p>He <em>spoke</em> with <strong>care</strong>.</p>
            </body></html>""",
            encoding="utf-8",
        )
        self.output = self.repo_root / "completed_volumes" / "english"

    def tearDown(self):
        self.temp.cleanup()

    def test_uses_spine_order_and_preserves_images_and_emphasis(self):
        result = EnglishExtractor(1, self.repo_root, self.output).run()
        text = (self.output / "volume1.md").read_text(encoding="utf-8")
        report = (self.output / "volume1_report.md").read_text(encoding="utf-8")

        self.assertEqual(result["errors"], 0)
        self.assertEqual(result["image_occurrences"], 2)
        self.assertIn("[[EN_EPUB_IMAGE:v01:OEBPS/cover.xhtml:OEBPS/images/cover.jpg:occ-0001]]", text)
        self.assertIn("[[EN_EPUB_IMAGE:v01:OEBPS/chapter001.xhtml:OEBPS/images/chapter.jpg:occ-0002]]", text)
        self.assertIn("## First Chapter", text)
        self.assertIn("### -chapter subtitle-", text)
        self.assertIn("He *spoke* with **care**.", text)
        self.assertNotIn("Duplicate contents heading", text)
        self.assertLess(text.index("chapter001.xhtml"), text.index("## First Chapter"))
        self.assertIn("Image occurrence map", report)
        self.assertIn("XHTML lang values found: en", report)

    def test_reports_non_english_xhtml_lang_as_metadata_warning(self):
        path = self.source / "chapter001a.xhtml"
        path.write_text(
            path.read_text(encoding="utf-8").replace('lang="en"', 'lang="fr"'),
            encoding="utf-8",
        )
        extractor = EnglishExtractor(1, self.repo_root, self.output)
        extractor.run()
        self.assertTrue(any("XHTML language attribute is 'fr'" in x for x in extractor.warnings))


if __name__ == "__main__":
    unittest.main()
