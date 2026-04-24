## grammar.py
- [] Standardize the input grammar type
- [] Confirm action flows.
- [] Decide whether deeper parts of grammar should reach up to top-level grammar

## symbol.py
- [] Simplify current_rules to just call the last one in rules?
- [] Confirm action flows.

## ruleset.py
- [] Implement additional ways to get a rule string out of a list.


## action.js
- [] Class definition
- [] activate
- [] deactivate
- [] testing



## node.js
- [] Node base class



To fix:

symbol.py:37 — Symbol.push_rules calls self.wrap_rules(rules) but the method is defined as wrapRules (line 23). AttributeError on first call.
grammar.py:84 — add_or_get_symbol calls Symbol(key) with one arg, but Symbol.__init__ requires (grammar, key). TypeError.
grammar.py:92 — pop_rules calls symbol.pop(key, None) on a Symbol instance. Should presumably be self.symbols.pop(key, None). AttributeError.



RuleSet.verify_rules returns a normalized list but the caller ignores the return value and uses rules directly. Either the method should mutate/assign, or __init__ should use what it returns. Right now it's doing neither cleanly.
Rule.get_parsed checks if not self.sections and re-parses, but __init__ already parses unconditionally. The lazy path is dead code.
Node.nodeCount as a class variable is the JS pattern. In Python this is usually done with itertools.count() or just left out if IDs aren't actually used (are they?).
Rule.error is set to "" in __init__ and checked with if self.rule.error in TagNode.expand. An empty string is falsy so it works, but None is the more idiomatic sentinel.
