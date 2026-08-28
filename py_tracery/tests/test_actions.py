import unittest

from ..grammars import grammar_test_actions_1
from ..grammar import Grammar

class TestActions(unittest.TestCase):
    g = grammar_test_actions_1
    test_g = Grammar(g)

    def test_action_shape(self):



if __name__ == "__main__":
    unittest.main()
