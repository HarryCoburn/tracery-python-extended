from .modifiers import modifiers as base_modifiers


class Grammar:
    def __init__(self) -> None:
        self.symbols = {}
        self.modifiers = base_modifiers

    def createGrammar(self, obj):
        pass
