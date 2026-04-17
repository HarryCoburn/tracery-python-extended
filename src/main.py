from grammar import Grammar


class Tracery:
    def __init__(self) -> None:
        self.grammar = Grammar()

    def createGrammar(self, grammar_obj):
        self.grammar = self.grammar.loadFrom(grammar_obj)


tracery = Tracery()

# Making this utility function module-level


def parseRule(rule):
    sections = []
    # Confirm rule is a string
    if not isinstance(rule, str):
        # addError is a just a call to console.warn(error)
        raise TypeError(f"Cannot parse non-string rule: {rule}")

    # Handle empty case
    if len(rule) == 0:
        return []

    _validate_rule(rule)

    depth = 0
    start = 0
    in_tag = False

    def create_section(end):
        nonlocal start, in_tag
        section = rule[start:end]
        if (len(section)) > 0:
            if in_tag:
                # Tag parser to come later
                sections.append(parse_tag(section))
            else:
                sections.append(section)
        in_tag = not in_tag
        start = end + 1

    # Create sections
    for idx, char in enumerate(rule):
        match char:
            case "[":
                depth += 1  # Going deeper
            case "]":
                depth -= 1  # Going shallower
            case "#":
                if depth == 0:
                    create_section(idx)

    create_section(len(rule))

    return sections


def _validate_rule(rule):
    depth = 0
    for char in rule:
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth < 0:
                raise ValueError(f"Unmatched ']' in rule {rule!r}")

    if depth > 0:
        raise ValueError(f"Too many ] in rule '{rule}'")

    if rule.count("#") % 2 != 0:
        raise TypeError(f"Odd number of # in rule '{rule}'")
