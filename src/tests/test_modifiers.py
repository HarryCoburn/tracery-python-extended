import unittest

from ..modifiers import *


class TestModifiers(unittest.TestCase):
    def test_characterIsNotaConsonant(self):
        self.assertFalse(isConsonant("a"))

    def test_characterIsAConsonant(self):
        self.assertTrue(isConsonant("c"))

    def test_characterIsAConsonantUpper(self):
        self.assertTrue(isConsonant("C"))


if __name__ == "__main__":
    unittest.main()
