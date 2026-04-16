###
# Original author of Tracery is Kate Compton
# Conversion and upgrade by Harry Coburn
###


class Action:
    def __init__(self, node, raw) -> None:
        self.node = node
        self.grammar = node.grammar
        self.raw = raw

    def activate(self):
        pass

    def deactivate(self):
        pass
