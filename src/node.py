###
# Original author of Tracery is Kate Compton
# Conversion and upgrade by Harry Coburn
###


# This class originally relied on a class library to create inheritance. We can do this all in Python.

import logging

from .action import Action
from .parsers import parse_rule

logger = logging.getLogger(__name__)


class Node:
    nodeCount = 0

    def __init__(self) -> None:
        self.depth = 0
        self.id = Node.nodeCount
        Node.nodeCount += 1
        self.child_text = None
        self.final_text = None
        self.parent = None
        self.grammar = None
        self.children = []
        self.error = ""
        self.actions = []

    def set_parent(self, parent):
        if parent:
            self.depth = parent.depth + 1
            self.parent = parent
            self.grammar = parent.grammar

    def expand(self):
        """Subclasses must set self.final_text to a string."""
        raise NotImplementedError("Subclasses must implement expand()")

    def expand_children(self):
        if self.children:
            self.child_text = ""
            for child in self.children:
                child.expand()
                self.child_text += child.final_text
            self.final_text = self.child_text

    def create_children_from_sections(self, sections):
        self.children = [self._make_child(s) for s in sections]

    def _make_child(self, section):
        if isinstance(section, str):
            return TextNode(self, section)
        return TagNode(self, section)


class RootNode(Node):
    def __init__(self, grammar, raw_rule) -> None:
        super().__init__()
        self.grammar = grammar
        self.sections = parse_rule(raw_rule)

    def expand(self):
        self.create_children_from_sections(self.sections)
        self.expand_children()


class TagNode(Node):
    def __init__(self, parent, parsed_tag) -> None:
        super().__init__()
        if not isinstance(parsed_tag, dict):
            raise TypeError(
                f"TagNode expects a parsed tag dict, got {type(parsed_tag).__name__}"
            )
        self.set_parent(parent)
        self.symbol = parsed_tag["symbol"]
        self.mods = parsed_tag["mods"]
        self.pre_actions = parsed_tag["pre_actions"]
        self.post_actions = parsed_tag["post_actions"]
        self.raw = parsed_tag["raw"]

    def expand(self):
        self.rule = self.grammar.get_rule(self.symbol)

        if self.rule.error:
            self.error = self.rule.error
            logger.warning(self.error)

        self.actions = []

        self.create_children_from_sections(self.rule.get_parsed())

        for pre_action in self.pre_actions:
            action = Action(self, pre_action)
            action.activate()
            self.actions.append(action)

        self.expand_children()

        for action in self.actions:
            action.deactivate()

        self.final_text = self.child_text

        for mod in self.mods:
            self.final_text = self.grammar.apply_mod(mod, self.final_text)

    # Add a __repr__ later to show symbol, mods, pre, post actions


class TextNode(Node):
    isLeaf = True

    def __init__(self, parent, text) -> None:
        super().__init__()
        self.set_parent(parent)
        self.text = text
        self.final_text = text

    def expand(self):
        # Leaf node: final_text is set at construction, nothing to expand.
        pass

    def to_label(self):
        return self.text


# Immediately returns root node.
