def parse_rule(rule):

    # Confirm rule is a string
    if not isinstance(rule, str):
        raise TypeError(f"Cannot parse non-string rule: {rule}")

    # Handle empty case
    if not rule:
        return []

    _validate_rule(rule)

    depth = 0
    start = 0
    in_tag = False
    sections = []

    # Create sections
    for idx, char in enumerate(rule):
        match char:
            case "[":
                depth += 1  # Going deeper
            case "]":
                depth -= 1  # Going shallower
            case "#":
                if depth == 0:
                    section = rule[start:idx]
                    if section:
                        sections.append(parse_tag(section) if in_tag else section)
                    start = idx + 1
                    in_tag = not in_tag

    trailing_rule = rule[start:]
    if trailing_rule:
        sections.append(trailing_rule)

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
        raise ValueError(f"Unclosed [ in rule {rule!r}")

    if rule.count("#") % 2 != 0:
        raise ValueError(f"Odd number of # in rule {rule!r}")


def _validate_tag(tag):
    depth = 0
    for char in tag:
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth < 0:
                raise ValueError(f"Unmatched ']' in tag {tag!r}")

    if depth > 0:
        raise ValueError(f"Too many [ in tag '{tag!r}'")


def parse_tag(tag):
    prefxns = []  # Prefixes
    postfxns = []  # Postfixes
    symbol = []
    mods = []

    depth = 0
    start = 0

    in_pre = True
    _validate_tag(tag)
    for idx, char in enumerate(tag):
        match char:
            case "[":
                if depth == 0:
                    if start != idx:
                        section = tag[start:idx]
                        if not in_pre:
                            raise ValueError(
                                f"multiple possible expansion symbols in tag: {tag!r}"
                            )
                        else:
                            in_pre = False
                            tag_split = section.split(".")
                            symbol = tag_split[0]
                            mods = tag_split[1:]
                depth += 1

            case "]":
                depth -= 1
                if depth == 0:
                    section = tag[start + 1 : idx]
                    if in_pre:
                        prefxns.append(parse_action(section))
                    else:
                        postfxns.append(parse_action(section))
                    start = idx + 1

    final_idx = len(tag)
    if start != final_idx:
        section = tag[start:final_idx]
        if not in_pre:
            raise ValueError(f"multiple possible expansion symbols in tag: {tag!r}")
        else:
            in_pre = False
            tag_split = section.split(".")
            symbol = tag_split[0]
            mods = tag_split[1:]

    return {
        "pre_actions": prefxns,
        "post_actions": postfxns,
        "symbol": symbol,
        "mods": mods,
        "raw": tag,
    }


def parse_action(action):
    """Parse an action string like key:value"""
    ### TODO. Original library was no-op. Defer until we decide to expand on this.

    return action
