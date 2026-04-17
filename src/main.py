from .grammar import Grammar


class Tracery:
    def __init__(self) -> None:
        self.grammar = Grammar()

    def createGrammar(self, grammar_obj):
        self.grammar = self.grammar.load_from(grammar_obj)

    # from traceryCore:
    # Ignore addError or use a logger.
    # Fold test into test cases


tracery = Tracery()
