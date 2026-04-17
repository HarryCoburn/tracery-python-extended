from .ruleset import RuleSet


class Symbol:
    def __init__(self, grammar, key) -> None:
        self.grammar = grammar
        self.key = key
        self.current_rules = None
        self.rule_sets = []

    def load_from(self, rules):
        rules = self.wrap_rules(rules)
        self.base_rules = rules
        self.rule_sets.append(rules)
        self.current_rules = self.rule_sets[-1]
