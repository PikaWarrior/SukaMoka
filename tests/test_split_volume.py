import unittest

from tools import split_volume as splitter


class MarkerRegexTests(unittest.TestCase):
    def test_pause_regex_matches_the_literal_marker_only(self):
        self.assertIsNotNone(splitter.PAUSE_BREAK_RE.search("left\n\n[пауза]\n\nright"))
        self.assertIsNone(splitter.PAUSE_BREAK_RE.search("left\n\nа\n\nright"))
        self.assertIsNone(splitter.PAUSE_BREAK_RE.search("left\n\nпаузa\n\nright"))

    def test_scene_regex_matches_gaiji_image_markers(self):
        text = "before\n\n[[EPUB_IMAGE:v4:xhtml/p-002.xhtml:gaiji-cid776-m-v.png:occ-01]]\n\nafter"
        self.assertIsNotNone(splitter.SCENE_BREAK_RE.search(text))

    def test_paragraph_fallback_skips_separator_before_pause_marker(self):
        self.assertIsNotNone(splitter.PARAGRAPH_BREAK_RE.search("left\n\nright"))
        text = "left\n\n[пауза]\n\nright"
        match = splitter.PARAGRAPH_BREAK_RE.search(text)
        self.assertIsNotNone(match)
        # The fallback skips the separator before [пауза], but may match the separator after it.
        self.assertEqual(
            match.start(),
            text.index("\n\n", text.index("[пауза]") + len("[пауза]")),
        )


class TextLengthTests(unittest.TestCase):
    def test_removes_ruby_image_pause_and_em_markup(self):
        text = "日本〔にほん〕語[пауза][[EPUB_IMAGE:v4:xhtml/p-001.xhtml:gaiji.png:occ-01]]<em>本文</em>"
        self.assertEqual(splitter.pure_jp_len(text), len("日本語本文"))

    def test_removes_editorial_brackets_and_heading_prefix(self):
        self.assertEqual(splitter.pure_jp_len("## 日本⟦editorial note⟧語"), len("日本語"))


class WrapperStrippingTests(unittest.TestCase):
    def test_strips_a_terminal_colophon_heading_and_keeps_epilogue(self):
        text = (
            "<!-- xhtml/p-toc-002.xhtml repeated -->\n\n"
            "## Story\n\nStory text\n\n## あとがき\n\nEpilogue\n\n"
            "## 奥付\n\nPublisher\n\nBookWalker promo"
        )
        _, body = splitter.strip_wrappers(text)
        self.assertEqual(body, "## Story\n\nStory text\n\n## あとがき\n\nEpilogue")
        _, kept = splitter.strip_wrappers(text, keep_colophon=True)
        self.assertIn("## 奥付", kept)
        self.assertIn("BookWalker promo", kept)

    def test_preserves_colophon_heading_if_another_heading_follows(self):
        text = "## Story\n\nStory\n\n## 奥付\n\nPublisher\n\n## Bonus\n\nBonus story"
        _, body = splitter.strip_wrappers(text)
        self.assertEqual(body, text)

    def test_does_not_cut_on_a_prose_mention_of_okuzuke(self):
        text = "## Story\n\nThe word 奥付 is mentioned here as ordinary prose."
        _, body = splitter.strip_wrappers(text)
        self.assertEqual(body, text)

    def test_legacy_credit_marker_must_be_a_standalone_line(self):
        text = "## Story\n\nProse mentions 本作品のイラストは in a sentence."
        _, body = splitter.strip_wrappers(text)
        self.assertEqual(body, text)
        text += "\n\n本作品のイラストは illustrator credit"
        _, body = splitter.strip_wrappers(text)
        self.assertEqual(body, "## Story\n\nProse mentions 本作品のイラストは in a sentence.")


class SplitIntegrityTests(unittest.TestCase):
    def test_both_modes_reconstruct_body_without_dropping_markers(self):
        paragraphs = [f"日本語の本文段落{i}。" + ("説明文と会話。" * 180) for i in range(28)]
        body = "## Story\n\n### Chapter 1\n\n" + "\n\n[пауза]\n\n".join(paragraphs)
        sections = splitter.split_into_sections(body)
        for chunks in (
            splitter.build_chunks_mode_a(sections),
            splitter.build_chunks_mode_b(sections),
        ):
            self.assertGreater(len(chunks), 1)
            self.assertEqual("\n\n".join(chunks), body)


if __name__ == "__main__":
    unittest.main()
