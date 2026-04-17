import unittest

from ..grammar import Grammar

# TODO: One test method per logical case, not per function. Split into
# separate modules or learn to use subtest. Method names should be
# about behavior, not the function.
#
# TODO: Test the modifiers case.


class TestGrammar(unittest.TestCase):
    def test_load_simple_grammar(self):
        grammar = Grammar()
        grammar.load_from({"animal": ["unicorn", "raven", "sparrow"]})

        self.assertIn("animal", grammar.symbols)
        animal = grammar.symbols["animal"]
        self.assertEqual(animal.key, "animal")
        self.assertEqual(animal.current_rules.rules, ["unicorn", "raven", "sparrow"])
        self.assertEqual(animal.current_rules.uses, [0, 0, 0])


if __name__ == "__main__":
    unittest.main()
