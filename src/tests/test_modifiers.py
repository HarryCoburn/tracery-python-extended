import unittest

from ..modifiers import *


class TestModifiers(unittest.TestCase):
    def test_characterIsNotaConsonant(self):
        self.assertFalse(is_consonant("a"))

    def test_characterIsAConsonant(self):
        self.assertTrue(is_consonant("c"))

    def test_characterIsAConsonantUpper(self):
        self.assertTrue(is_consonant("C"))

    def test_ends_with_consonant_and_y(self):
        self.assertTrue(ends_with_consonant_and_y("harpy"))
        self.assertFalse(ends_with_consonant_and_y("they"))
        self.assertFalse(ends_with_consonant_and_y("tree"))


if __name__ == "__main__":
    unittest.main()
