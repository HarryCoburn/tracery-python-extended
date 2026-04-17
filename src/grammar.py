from .modifiers import modifiers as base_modifiers
from .node import RootNode
from .rule import Rule
from .symbol import Symbol


class Grammar:
    def __init__(self) -> None:
        self.symbols = {}
        self.modifiers = base_modifiers.copy()
        self.symbol_names = []

    # Loading and changing grammars
    def clear(self):
        """Resets the grammar instance"""
        self.symbols = {}
        self.modifiers = base_modifiers.copy()

    def load_from(self, obj):
        """Loads obj into the Grammar instance"""
        self.clear()

        symbol_keys = obj.keys()

        for idx, key in enumerate(symbol_keys):
            self.symbol_names.append(key)
            self.symbols[key] = Symbol(self, key)
            self.symbols[key].load_from(obj[key])

    # Creating output

    def flatten(self, raw):
        """Entrypoint for output. Feed flatten the #entrypoint# in your grammar
        The one built into the samples is #origin#"""
        root = RootNode(self, raw)
        root.expand()
        return root.child_text

    def get_rule(self, key):
        symbol = self.symbols.get(key)
        if not symbol:
            r = Rule(f"((missing symbol: {key}))")
            r.error = f"Missing symbol {key}"
            return r

        rule = symbol.get_rule()
        if not rule:
            r = Rule(f"((empty: {key}))")
            r.error = f"Symbol {key} has no rule"
            return r

        return rule

    def __repr__(self) -> str:
        return f"Grammar(symbols={list(self.symbols)})"
