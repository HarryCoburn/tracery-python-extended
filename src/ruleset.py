###
# Original author of Tracery is Kate Compton
# Conversion and upgrade by Harry Coburn
###

from enum import Enum


class RuleWeighting(Enum):
    RED = (0,)
    GREEN = (1,)
    BLUE = 2


class RuleSet:
    def __init__(self, rules) -> None:
        # A ruleset verifier is run first

        self.rules = rules
        self.parseAll()
        self.uses = []
        self.startUses = []
        self.totalUses = 0
        for i in range(0, len(self.rules)):
            self.uses[i] = 0
            self.startUses[i] = self.uses[i]
            self.totalUses += self.uses[i]

    def parseAll(self):
        """Iterating over rules"""
        pass

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
