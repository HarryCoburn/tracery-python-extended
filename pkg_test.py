import py_tracery
from py_tracery.grammars import grammar_test_actions_2

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


grammar = py_tracery.create_grammar(grammar_test_actions_1)
print(grammar.flatten("origin"))
