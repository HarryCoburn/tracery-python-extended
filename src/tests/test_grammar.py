import unittest

from ..grammar import Grammar
from ..rule import Rule

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
        self.assertEqual(
            animal.current_rules.rules,
            [Rule("unicorn"), Rule("raven"), Rule("sparrow")],
        )
        self.assertEqual(animal.current_rules.uses, [0, 0, 0])

    def test_flatten_simple_symbol(self):
        grammar = Grammar()
        grammar.load_from({"animal": ["unicorn", "raven", "sparrow"]})
        result = grammar.flatten("#animal#")
        self.assertIn(result, {"unicorn", "raven", "sparrow"})

    def test_flatten_with_modifier(self):
        grammar = Grammar()
        grammar.load_from({"animal": ["unicorn"]})
        self.assertEqual(grammar.flatten("#animal.capitalize#"), "Unicorn")

    def test_flatten_nested_symbols(self):
        grammar = Grammar()
        grammar.load_from(
            {
                "origin": ["the #animal# sleeps"],
                "animal": ["unicorn"],
            }
        )
        self.assertEqual(grammar.flatten("#origin#"), "the unicorn sleeps")


if __name__ == "__main__":
    unittest.main()
