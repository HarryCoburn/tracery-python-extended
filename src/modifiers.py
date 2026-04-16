###
# Original author of Tracery is Kate Compton
# Conversion and upgrade by Harry Coburn
###

"""This is the set of modifiers that all English grammars will
need with this library. If you have a special rule you want, like beeSpeak,
then this is the place to add it for now. Define the function, and then
add it to the dictionary at the end of this."""

import re
import string
from asyncio.unix_events import SelectorEventLoop
from random import sample

# TODO: Guards against empty strings


def isConsonant(c):
    """Returns true if a character c is a consonant"""
    return c.lower() not in ["aeiou"]


def endsWithConY(s):
    """For pluralization of words ending in y to make ies"""
    if s[-1] == "y":
        return isConsonant(s[-2])
    return False


# modifiers variable is an object of functions. Those functions are below.


def titleCase(s):
    """Capitalize the first letter in each word of the string."""
    # Was capitalizeAll
    if s:
        return string.capwords(s)


def sentenceCase(s):
    """Capitalizes the first letter in a string representing a sentence."""
    # Was capitalize
    if s:
        return s[0].upper() + s[1:]


def inQuotes(s):
    """Wraps string in quotes"""
    if s:
        return f'"{s}"'


def addEndPunctuation(s):
    """Confirms end puncutation. Adds a comma if it is missing."""
    # was comma
    if s[-1] in ",.?!":
        return s
    return s + ","


def beeSpeak(s):
    """Example of a custom tweak. Replaces the first s in the string with zzz"""
    s = re.sub(r"s", "zzz", s, count=1)
    return s


def a(s):
    """Adds the correct indefinite article"""
    if not isConsonant(s[0]):
        return "an " + s
    return "a " + s


def s(s):
    if s[-1] == "y":
        if endsWithConY(s) is False:
            return s + "s"
        else:
            return s[0:-2] + "ies"
    elif s[-1] == "x":
        return s + "en"
    elif s[-1] == "z" or s[-1] == "h":
        return s + "es"
    else:
        return s + "s"


def ed(s):
    first, sep, rest = s.partition(" ")
    if first[-1] == "y":
        if endsWithConY(first) is False:
            return first + "ed" + sep + rest
        else:
            return s[0:-2] + "ied" + sep + rest
    elif first[-1] == "e":
        return first + "d" + sep + rest
    else:
        return first + "ed" + sep + rest
