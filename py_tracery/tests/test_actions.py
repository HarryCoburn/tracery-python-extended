import unittest

from ..grammars import grammar_test_actions_1
from ..grammar import Grammar

class TestActions(unittest.TestCase):

    def test_action_holds_a_value_across_references(self):
        g = Grammar({
            "origin": ["#[hero:#name#]story#"],
            "story": ["#hero# and #hero#"],
            "name": ["Arjun", "Yuuma", "Darcy", "Mia"],
        })
        out = g.flatten("#origin#")
        first, second = out.split(" and ")
        self.assertEqual(first, second)

    def test_top_level_actions_are_not_supported(self):
        """Known gap: parse_rule does not handle [ ] outside a tag."""
        g = Grammar({"origin": ["[hero:#name#]#hero#"], "name": ["Arjun"]})
        out = g.flatten("#origin#")
        self.assertIn("[hero:", out)

    def test_action_symbol_is_removed_after_flatten(self):
        g = Grammar({"origin": ["#[hero:#name#]story#"],
                     "story": ["#hero#"],
                     "name": ["Arjun"]})
        g.flatten("#origin#")
        self.assertNotIn("hero", g.symbols)

    def test_grammar_symbol_survives_an_action_push(self):
        g = Grammar({"origin": ["#[name:Bob]story#"],
                     "story": ["#name#"],
                     "name": ["Arjun"]})
        g.flatten("#origin#")
        self.assertIn("name", g.symbols)
        self.assertEqual(g.flatten("#name#"), "Arjun")

    def test_repeated_flatten_does_not_grow_symbols(self):
        g = Grammar({"origin": ["#[hero:#name#]story#"],
                     "story": ["#hero#"],
                     "name": ["Arjun"]})
        before = set(g.symbols)
        for _ in range(10):
            g.flatten("#origin#")
        self.assertEqual(set(g.symbols), before)

if __name__ == "__main__":
    unittest.main()
