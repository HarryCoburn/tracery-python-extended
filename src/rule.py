"""
The base Rule class, which is the lowest level we would give inside of a Tracery grammar after processing. This lowest level is then further processed
by parse_rule.

Properties:
    raw: The raw rule given.
    sections: the rule divided into its components from parse_rule (perhaps rename get_parsed to get_sections?)
    error: A place for error messages related to the rule.
"""

###
# Original author of Tracery is Kate Compton
# Conversion and upgrade by Harry Coburn
###

from .parsers import parse_rule


class Rule:
    def __init__(self, raw) -> None:
        self.raw = raw
        self.sections = parse_rule(raw)
        self.error = None

    def get_parsed(self):
        """Get the parsed sections of the rule"""
        return self.sections

    def __str__(self) -> str:
        return self.raw

    def __repr__(self) -> str:
        return f"Rule({self.raw!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rule):
            return NotImplemented
        return self.raw == other.raw

    def __hash__(self) -> int:
        return hash(self.raw)
