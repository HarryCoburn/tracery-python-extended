from .modifiers import modifiers as base_modifiers
from .symbol import Symbol


class Grammar:
    def __init__(self) -> None:
        self.symbols = {}
        self.modifiers = base_modifiers.copy()
        self.symbol_names = []

    def clear(self):
        """Resets the grammar instance"""
        self.symbols = {}
        self.modifiers = base_modifiers.copy()

    def load_from(self, obj):
        """Loads obj into the Grammar instance"""
        self.clear()
        if isinstance(obj, dict) and "symbols" in obj:
            symbol_source = obj["symbols"]
        else:
            symbol_source = obj

        symbol_keys = obj.keys()

        for idx, key in enumerate(symbol_keys):
            self.symbol_names.append(key)
            self.symbols[key] = Symbol(self, key)
            self.symbols[key].load_from(symbol_source[key])
