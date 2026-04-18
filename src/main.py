"""
The main entry point for the to-be-made library. Expects a Tracery grammar.
TODO: make a way to import the Tracery grammar from a file, whether by command line argument or by passing elsewhere.
TODO: make a way to specify the entry point into the grammar function.
Possible alternative: Just make Grammar the entry point and expose parts of it?
"""

from .grammar import Grammar

g = Grammar({"animal": ["unicorn", "raven"]})  # for testing.
response = g.flatten("#animal#")
