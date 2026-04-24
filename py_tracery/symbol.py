"""
The class for the top-level entries in a processed Tracery grammar. Symbols are the keys in the Grammar class' symbols dict.

Properties:
    key: The name of the Symbol
    current_rules: The current rule for processing
    rule_sets: a list that serves as a stack of rules, which should all be of type RuleSet

TOOD: Feed rules in directly into the constructor like we're doing with Grammar?
"""

from .ruleset import RuleSet


class Symbol:
    def __init__(self, key) -> None:
        self.key = key
        self.current_rules = None
        self.rule_sets = []

    def load_rules(self, rules):
        """Takes the rules from a Tracery grammar and converts them into RuleSet"""
        self.push_rules(rules)
        rule_set = RuleSet(rules)
        self.rule_sets.append(rule_set)
        self.current_rules = self.rule_sets[-1]  # current_rules is a stack?

    def get_rule(self):
        """Grabs the specifics of whatever is considered the current rule"""
        return self.current_rules.get()

    # Action Processing
    def push_rules(self, rules):
        """Adds rules from actions to the set of rules and puts it at the top of the stack"""
        if not isinstance(rules, RuleSet):
            rules = RuleSet(rules)
        self.rule_sets.append(rules)
        self.current_rules = rules

    def pop_rules(self):
        """Pops a rule off the stack after processing and shifts the current rule to the next in the stack"""
        if not self.rule_sets:
            return

        self.rule_sets.pop()
        self.current_rules = self.rule_sets[-1] if self.rule_sets else None

    def to_dict(self) -> dict:
        return {
            "Symbol key": self.key,
            "rule_sets": [rs.to_dict() for rs in self.rule_sets],
        }

    def __repr__(self) -> str:
        return f"Symbol({self.key!r})"
