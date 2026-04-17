from .ruleset import RuleSet


class Symbol:
    def __init__(self, grammar, key) -> None:
        self.grammar = grammar
        self.key = key
        self.current_rules = None
        self.rule_sets = []

    def load_from(self, rules):
        rule_set = RuleSet(rules)
        self.base_rules = rule_set
        self.rule_sets.append(rule_set)
        self.current_rules = self.rule_sets[-1]

    def __repr__(self) -> str:
        return f"Symbol({self.key!r})"
