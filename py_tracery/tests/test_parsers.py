import unittest

from ..parsers import parse_tag


class TestParseTag(unittest.TestCase):
    def test_simple_tag(self):
        t = parse_tag("color")
        self.assertEqual(t["symbol"], "color")
        self.assertEqual(t["mods"], [])
        self.assertEqual(t["pre_actions"], [])
        self.assertEqual(t["post_actions"], [])

    def test_tag_with_mod(self):
        t = parse_tag("color.capitalize")
        self.assertEqual(t["symbol"], "color")
        self.assertEqual(t["mods"], ["capitalize"])

    def test_tag_with_multiple_mods(self):
        t = parse_tag("color.capitalize.s")
        self.assertEqual(t["symbol"], "color")
        self.assertEqual(t["mods"], ["capitalize", "s"])

    def test_tag_with_pre_action(self):
        t = parse_tag("[mood:happy]color")
        self.assertEqual(t["symbol"], "color")
        self.assertEqual(len(t["pre_actions"]), 1)
        self.assertEqual(t["post_actions"], [])

    def test_tag_with_post_action(self):
        t = parse_tag("color[setMood:calm]")
        self.assertEqual(t["symbol"], "color")
        self.assertEqual(t["pre_actions"], [])
        self.assertEqual(len(t["post_actions"]), 1)

    def test_tag_preserves_raw(self):
        t = parse_tag("color.capitalize")
        self.assertEqual(t["raw"], "color.capitalize")


if __name__ == "__main__":
    unittest.main()
