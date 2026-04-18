"""
The main entry point for the to-be-made library. Expects a Tracery grammar.
TODO: make a way to import the Tracery grammar from a file, whether by command line argument or by passing elsewhere.
TODO: make a way to specify the entry point into the grammar function.
Possible alternative: Just make Grammar the entry point and expose parts of it?
"""

from .grammar import Grammar

grammar_test_2 = {
    "sentence": ["The #color# #animal# of the #natureNoun# is called #name#"],
    "color": [
        "orange",
        "blue",
        "white",
        "black",
        "grey",
        "purple",
        "indigo",
        "turquoise",
    ],
    "animal": [
        "unicorn",
        "raven",
        "sparrow",
        "scorpion",
        "coyote",
        "eagle",
        "owl",
        "lizard",
        "zebra",
        "duck",
        "kitten",
    ],
    "natureNoun": [
        "ocean",
        "mountain",
        "forest",
        "cloud",
        "river",
        "tree",
        "sky",
        "sea",
        "desert",
    ],
    "name": ["Arjun", "Yuuma", "Darcy", "Mia", "Chiaki", "Izzi", "Azra", "Lina"],
}

grammar_test_3 = {
    "sentence": ["#name# the #color# #animal# was ... something."],
    "name": ["Arjun", "Yuuma", "Darcy", "Mia", "Chiaki", "Izzi", "Azra", "Lina"],
    "color": [
        "orange",
        "blue",
        "white",
        "black",
        "grey",
        "purple",
        "indigo",
        "turquoise",
    ],
    "animal": [
        "unicorn",
        "raven",
        "sparrow",
        "scorpion",
        "coyote",
        "eagle",
        "owl",
        "lizard",
        "zebra",
        "duck",
        "kitten",
    ],
}

grammar_test_modifiers = {
    "sentence": [
        "#color.capitalize# #animal.s# are #often# #mood#.",
        "#animal.a.capitalize# is #often# #mood#, unless it is #color.a# one.",
    ],
    "often": ["rarely", "never", "often", "almost always", "always", "sometimes"],
    "color": [
        "orange",
        "blue",
        "white",
        "black",
        "grey",
        "purple",
        "indigo",
        "turquoise",
    ],
    "animal": [
        "unicorn",
        "raven",
        "sparrow",
        "scorpion",
        "coyote",
        "eagle",
        "owl",
        "lizard",
        "zebra",
        "duck",
        "kitten",
    ],
    "mood": ["vexed", "indignant", "impassioned", "wistful", "astute", "courteous"],
    "natureNoun": [
        "ocean",
        "mountain",
        "forest",
        "cloud",
        "river",
        "tree",
        "sky",
        "earth",
        "void",
        "desert",
    ],
}

grammar_test_actions_1 = {
    "name": ["Arjun", "Yuuma", "Darcy", "Mia", "Chiaki", "Izzi", "Azra", "Lina"],
    "animal": [
        "unicorn",
        "raven",
        "sparrow",
        "scorpion",
        "coyote",
        "eagle",
        "owl",
        "lizard",
        "zebra",
        "duck",
        "kitten",
    ],
    "mood": ["vexed", "indignant", "impassioned", "wistful", "astute", "courteous"],
    "story": [
        "#hero# traveled with her pet #heroPet#.  #hero# was never #mood#, for the #heroPet# was always too #mood#."
    ],
    "origin": ["#[hero:#name#][heroPet:#animal#]story#"],
}

g = Grammar(grammar_test_actions_1)  # for testing.
g.pretty()
for _ in range(1, 6):
    response = g.flatten("#sentence#")
    print(f"The response is: {response}")
