###
# Original author of Tracery is Kate Compton
# Conversion and upgrade by Harry Coburn
###

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
        if not isinstance(rules, (RuleSet, list)):
            # TODO Removed string as a rule type. See if this appears in the grammars.
            raise ValueError(f"Unknown rules type: {rules}")

    def parse_all(self):
        """Turns rules into Rule objects, if they are not"""
        self.rules = [r if isinstance(r, Rule) else Rule(r) for r in self.rules]

    def mapRules(self, fxn):
        pass

    def applyToRules(self, fxn):
        pass

    def getRuleByIndex(self, fxn):
        pass

    def getRandomIndex(self):
        pass

    def getIndex(self):
        pass

    def decayUses(self, pct):
        pass

    def testRandom(self):
        pass

    def getSaveRules(self):
        pass

    def __repr__(self) -> str:
        return f"RuleSet({self.rules!r})"
