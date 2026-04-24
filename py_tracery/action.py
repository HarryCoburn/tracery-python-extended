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

        # Replace hashtags
        self.amended = self.grammar.flatten(self.raw)

        parsed = parse_tag(self.amended)

        for sub_action_raw in parsed["pre_actions"]:
            self.sub_actions.append(Action(self.node, sub_action_raw))

        if parsed["symbol"]:
            split_symbol = parsed["symbol"].split(":")

            if len(split_symbol) == 2:
                symbol, rules = split_symbol[0], split_symbol[1].split(",")
                self.push = {"symbol": symbol, "rules": rules}
                self.node.grammar.push_rules(self.push["symbol"], self.push["rules"])

            else:
                raise ValueError(f"Unknown action: {parsed['symbol']!r}")

        for sub_action in self.sub_actions:
            sub_action.activate()

    def deactivate(self):
        for sub_action in self.sub_actions:
            sub_action.deactivate()

        if self.push:
            self.node.grammar.pop_rules(self.push["symbol"], self.push["rules"])
