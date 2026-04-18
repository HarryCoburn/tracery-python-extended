"""
The Tracery Grammar class, which is the top-level class.
The two important public functions are:
    load_from(grammar): Takes grammar, a Tracery grammar, and loads it into the Grammar class by processing its symbols and rules.
    flatten(raw): Takes raw, an entry point symbol (usually #origin#), and processes its key using the grammar to return the requested string.
Grammar can also be initialized directly with a grammar.

Grammar has:
    symbols = a dict of string keys and Symbol values, taken from the keys in the loaded grammar.
    modifiers = a dict of string keys and function values to modify text with the . parameter.

A Tracery grammar fed into this function is a dict in the structure of:
    {
    Symbol: { rule_key: string or list of rules }
    }
"""

from .modifiers import modifiers as base_modifiers
from .node import RootNode
from .rule import Rule
from .symbol import Symbol


class Grammar:
    """The Tracery Grammar class"""

    def __init__(self, grammar=None) -> None:
        self.symbols = {}
        self.modifiers = base_modifiers.copy()
        if grammar is not None:
            self.load_from(grammar)

    # Loading and changing grammars
    def clear(self):
        """Resets the grammar instance"""
        self.symbols = {}
        self.modifiers = base_modifiers.copy()

    def load_from(self, grammar):
        """Loads grammar into the Grammar instance"""
        self.clear()

        for key, rules in grammar.items():
            self.symbols[key] = Symbol(self, key)
            self.symbols[key].load_from(rules)

    # Creating output

    def flatten(self, raw):
        """Entrypoint for output. Feed flatten the #entrypoint# in your grammar
        The one built into the samples is #origin#"""
        root = RootNode(self, raw)
        root.expand()
        return root.child_text

    # Nodes

    def get_rule(self, key):
        """Gets the rules from a given symbol. Called by Nodes"""
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

    # Modifiers

    def apply_mod(self, mod_name, text):
        """Applies a modifier function to a text string"""
        if mod_name not in self.modifiers:
            raise KeyError(f"Unknown modifier: {mod_name!r}")
        return self.modifiers[mod_name](text)

    # Action processing

    def add_or_get_symbol(self, key):
        """Either gets a symbol or silently makes one to prevent a crash"""
        if key not in self.symbols:
            self.symbols[key] = Symbol(self, key)

        return self.symbols[key]

    def push_rules(self, key, rules):
        """Pushes an action's rules down to a particular symbol"""
        symbol = self.add_or_get_symbol(key)
        symbol.push_rules(rules)

    def pop_rules(self, key, rules):
        # TODO: May not need the rules passing here. Check the action path.
        """Pops a rule off of a particular symbol. Removes the symbol if there are no more rules."""
        symbol = self.add_or_get_symbol(key)
        symbol.pop_rules()

        if len(symbol.rule_sets) == 0:
            self.symbols.pop(key, None)

    # Representation

    def __repr__(self) -> str:
        return f"Grammar(symbols={list(self.symbols)})"
