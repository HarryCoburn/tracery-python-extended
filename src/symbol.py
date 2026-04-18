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

    def get_rule(self):
        return self.current_rules.get()

    def mapRules(self, fxn):
        pass

    def applyToRules(self, fxn):
        pass

    def wrapRules(self, rules):
        if not isinstance(rules, RuleSet):
            if isinstance(rules, list):
                return RuleSet(rules)
            elif isinstance(rules, str):
                return RuleSet(rules)
            else:
                raise TypeError(f"Unknown rules type: {rules}")
        return rules

    def push_rules(self, rules):
        rules = self.wrap_rules(rules)
        self.rule_sets.append(rules)
        self.current_rules = self.rule_sets[-1]

    def pop_rules(self, rules):
        ex_rules = self.rule_sets.pop()
        if self.rule_sets:
            self.current_rules = self.rule_sets[-1]

    def setRules(self, rules):
        pass

    def addRule(self, rule):
        pass

    def select(self, rule):
        pass

    def deselect(self, rule):
        pass

    def __repr__(self) -> str:
        return f"Symbol({self.key!r})"
