###
# Original author of Tracery is Kate Compton
# Conversion and upgrade by Harry Coburn
###

import random
from enum import Enum

from .rule import Rule


class RuleWeighting(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


class RuleSet:
    def __init__(self, rules) -> None:
        self.verify_rules(rules)
        self.rules = rules
        self.parse_all()
        self.uses = [0] * len(self.rules)
        self.startUses = list(self.uses)
        self.totalUses = 0

    def verify_rules(self, rules):
        if isinstance(rules, RuleSet):
            return list(rules.rules)
        if isinstance(rules, str):
            return [rules]
        if isinstance(rules, list):
            return list(rules)
        raise TypeError(f"Unknown rules type: {rules}")

    def parse_all(self):
        """Turns rules into Rule objects, if they are not"""
        self.rules = [r if isinstance(r, Rule) else Rule(r) for r in self.rules]

    def mapRules(self, fxn):
        pass

    def applyToRules(self, fxn):
        pass

    def get(self):
        return self.rules[self._get_index()]

    def _get_index(self):
        min_uses = min(self.uses)
        candidates = [i for i, u in enumerate(self.uses) if u == min_uses]
        idx = random.choice(candidates)
        self.uses[idx] += 1
        self.totalUses += 1
        return idx

    # Original decayUses, testRandom, and getSaveRules are not needed.

    def __repr__(self) -> str:
        return f"RuleSet({self.rules!r})"
