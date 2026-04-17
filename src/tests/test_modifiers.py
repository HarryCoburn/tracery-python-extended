import unittest
from copyreg import add_extension

from ..modifiers import *


class TestModifiers(unittest.TestCase):
    def test_character_is_consonant(self):
        self.assertTrue(is_consonant("c"))
        self.assertFalse(is_consonant("a"))
        self.assertTrue(is_consonant("C"))

    def test_ends_with_consonant_and_y(self):
        self.assertTrue(ends_with_consonant_and_y("harpy"))
        self.assertFalse(ends_with_consonant_and_y("they"))
        self.assertFalse(ends_with_consonant_and_y("tree"))

    def test_title_case(self):
        self.assertEqual(title_case("hello world"), "Hello World")

    def test_sentence_case(self):
        self.assertEqual(sentence_case("i'm a phrase"), "I'm a phrase")

    def test_in_quotes(self):
        self.assertEqual(in_quotes("hello world"), '"hello world"')

    def test_add_end_punctuation(self):
        self.assertEqual(
            add_end_punctuation("I have punctuation."), "I have punctuation."
        )
        self.assertEqual(
            add_end_punctuation("I do not have punctuation"),
            "I do not have punctuation,",
        )

    def test_bee_speak(self):
        self.assertEqual(bee_speak("sass"), "zzzass")
        self.assertEqual(bee_speak("bert"), "bert")

    def test_add_indefinite_article(self):
        self.assertEqual(add_indefinite_article("bobcat"), "a bobcat")
        self.assertEqual(add_indefinite_article("antelope"), "an antelope")

    def test_pluralize(self):
        self.assertEqual(pluralize("harpy"), "harpies")
        self.assertEqual(pluralize("assay"), "assays")
        self.assertEqual(pluralize("ox"), "oxen")
        self.assertEqual(pluralize("bob"), "bobs")
        self.assertEqual(pluralize("blitz"), "blitzes")
        self.assertEqual(pluralize("marsh"), "marshes")

    def test_past_tense(self):
        self.assertEqual(past_tense("jumps on you"), "jumped on you")


if __name__ == "__main__":
    unittest.main()
