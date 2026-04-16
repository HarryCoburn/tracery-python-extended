from grammar import Grammar


class Tracery:
    def __init__(self) -> None:
        self.grammar = Grammar()

    def createGrammar(self, grammar_obj):
        self.grammar = self.grammar.loadFrom(grammar_obj)
