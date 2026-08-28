import unittest

from ..grammars import grammar_test_actions_1
from ..grammar import Grammar

class TestActions(unittest.TestCase):

    def test_action_holds_a_value_across_references(self):
        g = Grammar({
            "origin": ["[hero:#name#]#hero# and #hero#"],
            "name": ["Arjun", "Yuuma", "Darcy", "Mia"],
        })
        out = g.flatten("#origin#")
        _, _, names = out.partition("]") if "]" in out else ("", "", out)
        first, second = out.split(" and ")
        assert first == second


if __name__ == "__main__":
    unittest.main()
