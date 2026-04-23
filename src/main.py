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

grammar_test_actions_2 = {
    "name": [
        "Cheri",
        "Fox",
        "Morgana",
        "Jedoo",
        "Brick",
        "Shadow",
        "Krox",
        "Urga",
        "Zelph",
    ],
    "story": [
        "#hero.capitalize# was a great #occupation#, and this song tells of #heroTheir# adventure. #hero.capitalize# #didStuff#, then #heroThey# #didStuff#, then #heroThey# went home to read a book."
    ],
    "monster": [
        "dragon",
        "ogre",
        "witch",
        "wizard",
        "goblin",
        "golem",
        "giant",
        "sphinx",
        "warlord",
    ],
    "setPronouns": [
        "[heroThey:they][heroThem:them][heroTheir:their][heroTheirs:theirs]",
        "[heroThey:she][heroThem:her][heroTheir:her][heroTheirs:hers]",
        "[heroThey:he][heroThem:him][heroTheir:his][heroTheirs:his]",
    ],
    "setOccupation": [
        "[occupation:baker][didStuff:baked bread,decorated cupcakes,folded dough,made croissants,iced a cake]",
        "[occupation:warrior][didStuff:fought #monster.a#,saved a village from #monster.a#,battled #monster.a#,defeated #monster.a#]",
    ],
    "origin": ["#[#setPronouns#][#setOccupation#][hero:#name#]story#"],
}

grammar_test_nested = {
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
    "occupationBase": [
        "wizard",
        "witch",
        "detective",
        "ballerina",
        "criminal",
        "pirate",
        "lumberjack",
        "spy",
        "doctor",
        "scientist",
        "captain",
        "priest",
    ],
    "occupationMod": [
        "occult ",
        "space ",
        "professional ",
        "gentleman ",
        "erotic ",
        "time ",
        "cyber",
        "paleo",
        "techno",
        "super",
    ],
    "strange": ["mysterious", "portentous", "enchanting", "strange", "eerie"],
    "tale": ["story", "saga", "tale", "legend"],
    "occupation": ["#occupationMod##occupationBase#"],
    "mood": ["vexed", "indignant", "impassioned", "wistful", "astute", "courteous"],
    "setPronouns": [
        "[heroThey:they][heroThem:them][heroTheir:their][heroTheirs:theirs]",
        "[heroThey:she][heroThem:her][heroTheir:her][heroTheirs:hers]",
        "[heroThey:he][heroThem:him][heroTheir:his][heroTheirs:his]",
    ],
    "setSailForAdventure": [
        "set sail for adventure",
        "left #heroTheir# home",
        "set out for adventure",
        "went to seek #heroTheir# forture",
    ],
    "setCharacter": ["[#setPronouns#][hero:#name#][heroJob:#occupation#]"],
    "openBook": [
        "An old #occupation# told #hero# a story. 'Listen well' she said to #hero#, 'to this #strange# #tale#. ' #origin#'",
        "#hero# went home.",
        "#hero# found an ancient book and opened it.  As #hero# read, the book told #strange.a# #tale#: #origin#",
    ],
    "story": ["#hero# the #heroJob# #setSailForAdventure#. #openBook#"],
    "origin": ["Once upon a time, #[#setCharacter#]story#"],
}

g = Grammar(grammar_test_nested)  # for testing.
# g.pretty() # For printing the grammar tree
for _ in range(1, 6):
    response = g.flatten("#origin#")
    print(f"The response is: {response}")
