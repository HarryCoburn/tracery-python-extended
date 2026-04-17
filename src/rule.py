###
# Original author of Tracery is Kate Compton
# Conversion and upgrade by Harry Coburn
###

from .parsers import parse_rule


class Rule:
    def __init__(self, raw) -> None:
        self.raw = raw
        self.sections = parse_rule(raw)
        self.error = ""

    def get_parsed(self):
        if not self.sections:
            self.sections = parse_rule(self.raw)

        return self.sections

    def __str__(self) -> str:
        return self.raw

    def __repr__(self) -> str:
        return f"Rule({self.raw!r})"

    def to_json(self) -> str:
        return self.raw

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rule):
            return NotImplemented
        return self.raw == other.raw and self.sections == other.sections

    def __hash__(self) -> int:
        return hash(self.raw)
