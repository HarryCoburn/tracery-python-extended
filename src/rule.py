###
# Original author of Tracery is Kate Compton
# Conversion and upgrade by Harry Coburn
###


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
