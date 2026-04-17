###
# Original author of Tracery is Kate Compton
# Conversion and upgrade by Harry Coburn
###

from .main import tracery


class Rule:
    def __init__(self, raw) -> None:
        self.raw = raw
        self.sections = tracery.parseRule(raw)

    def getParsed(self):
        pass

    def toString(self):
        pass

    def toJSONString(self):
        pass

    def __str__(self) -> str:
        return self.raw

    def __repr__(self) -> str:
        return f"Rule({self.raw!r})"

    def to_json(self) -> str:
        return self.raw
