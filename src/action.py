###
# Original author of Tracery is Kate Compton
# Conversion and upgrade by Harry Coburn
###

from .parsers import parse_tag


class Action:
    def __init__(self, node, raw) -> None:
        self.node = node
        self.grammar = node.grammar
        self.raw = raw
        self.amended = None
        self.sub_actions = []
        self.push = {}

    def activate(self):
        self.node.actions.append(self)
        self.amended = self.grammar.flatten(self.raw)
        parsed = parse_tag(self.amended)
        sub_action_raw = parsed.pre_actions
        if sub_action_raw:
            for sub_action in sub_action_raw:
                self.sub_action.append(Action(self, sub_action))

        if parsed.symbol:
            split_symbol = parsed.symbol.split(":")

            if len(split_symbol) == 2:
                self.push["symbol"] = split_symbol[0]
                self.push["rules"] = split_symbol[1].split(",")
                self.node.grammar.pushRules(self.push["symbol"], self.push["rules"])
            else:
                raise Exception(f"Unknown Action: {parsed.symbol}")

        if len(self.sub_actions) > 0:
            for sub_action in self.sub_actions:
                sub_action.activate()

    def deactivate(self):
        if len(self.sub_actions) > 0:
            for sub_action in self.sub_actions:
                sub_action.deactivate()

        if len(self.push) > 0:
            self.node.grammar.popRules(self.push["symbol"], self.push["rules"])
