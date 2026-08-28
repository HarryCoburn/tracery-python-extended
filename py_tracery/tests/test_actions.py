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

if __name__ == "__main__":
    unittest.main()
