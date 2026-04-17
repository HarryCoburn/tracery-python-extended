from .grammar import Grammar

g = Grammar({"animal": ["unicorn", "raven"]})  # for testing.
response = g.flatten("#animal#")


# from traceryCore:
# Ignore addError or use a logger.
# Fold test into test cases
