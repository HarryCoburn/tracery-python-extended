"""
The RuleSet class defines what a set of rules does, and it also defines the selection of a word from a ruleset works.
The only way this is done currently is through a counting system.

TODO: adding weights, randomization, and other selection methods, then updating the grammar to define how to do track these.

Accepts: rules, which should be a list, a string, or another RuleSet.

Properties:
    rules: the rules to be processed. First verified to be of the right type for processing, and then
    each item in the list is turned into a Rule object, if not done yet, using RuleSet.parse_all()
    uses: A list of ints showing how many times a rule has been used. Used to spread randomization about.

Future expansion:
    get() gets the specific rule string out. This could be fed functions or parameters to created different kinds of fetching.

"""

###
# Original author of Tracery is Kate Compton
# Conversion and upgrade by Harry Coburn
###

import random

from .rule import Rule


class RuleSet:
    def __init__(self, rules) -> None:
        self.verify_rules(rules)
        self.rules = self._normalize_rules(rules)
        self.parse_all()
        self.uses = [0] * len(self.rules)

    def _normalize_rules(self, rules):
        """Normalizes the rules we receive into the right list shape, or returns an unknown rules type"""
        if isinstance(rules, RuleSet):
            return list(rules.rules)  # I believe this is ultimately how it ends up?
        if isinstance(rules, str):
            return [rules]
        if isinstance(rules, list):
            return list(rules)
        raise TypeError(f"Unknown rules type: {rules}")

    def parse_all(self):
        """Turns items in a RuleSet list into Rule objects, if they are not"""
        self.rules = [r if isinstance(r, Rule) else Rule(r) for r in self.rules]

    def get(self):
        """Get a word from the rule by index"""
        return self.rules[self._get_index()]

    def _get_index(self):
        """Return an index based on a random selection weighted by the number of uses."""
        min_uses = min(self.uses)
        candidates = [i for i, u in enumerate(self.uses) if u == min_uses]
        idx = random.choice(candidates)
        self.uses[idx] += 1
        return idx

    def __repr__(self) -> str:
        return f"RuleSet({self.rules!r})"
