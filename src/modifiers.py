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
from typing import Callable

VOWELS = "aeiou"

modifiers: dict[str, Callable[[str], str]] = {}


def modifier(name):
    def decorator(fn):
        modifiers[name] = fn
        return fn

    return decorator


# Helper functions


def is_consonant(c: str) -> bool:
    """Returns true if a character c is an alphabetic consonant.
    Non-letters return false."""
    return c.isalpha() and c.lower() not in VOWELS


def ends_with_consonant_and_y(word: str) -> bool:
    """For pluralization of words ending in y to make ies.
    Words fewer than two characters return false."""
    return len(word) >= 2 and is_consonant(word[-2]) and word[-1] == "y"


# Modifiers to add to dictionary


@modifier("title_case")
def title_case(sentence: str) -> str:
    """Capitalize the first letter in each word of the string."""
    # Was capitalizeAll
    if sentence:
        return string.capwords(sentence)
    else:
        return sentence


@modifier("sentence_case")
def sentence_case(sentence: str) -> str:
    """Capitalizes the first letter in a string representing a sentence."""
    # Was capitalize
    if sentence:
        return sentence[0].upper() + sentence[1:]
    else:
        return sentence


@modifier("in_quotes")
def in_quotes(sentence: str) -> str:
    """Wraps sentence in quotes"""
    if sentence:
        return f'"{sentence}"'
    else:
        return sentence


@modifier("add_end_punctuation")
def add_end_punctuation(sentence: str) -> str:
    """Confirms end puncutation. Adds a comma if it is missing."""
    # was comma
    if not sentence:
        return sentence
    if sentence[-1] in ",.?!":
        return sentence
    return sentence + ","


@modifier("bee_speak")
def bee_speak(sentence: str) -> str:
    """Example of a custom tweak. Replaces the first s in the string with zzz"""
    if not sentence:
        return sentence
    sentence = re.sub(r"s", "zzz", sentence, count=1)
    return sentence


@modifier("a")
def add_indefinite_article(word: str) -> str:
    """Adds the correct indefinite article"""
    if not word:
        return word
    if not is_consonant(word[0]):
        return "an " + word
    return "a " + word


@modifier("s")
def pluralize(word: str) -> str:
    """Makes a given word plural"""
    if not word:
        return word
    if word[-1] == "y":
        if not ends_with_consonant_and_y(word):
            return word + "s"
        else:
            return word[:-1] + "ies"
    elif word[-1] == "x":
        return word + "en"
    elif word[-1] in "zh":
        return word + "es"
    else:
        return word + "s"


@modifier("ed")
def past_tense(text: str) -> str:
    """Makes a word past tense. Original library assumed possible multi-word string.
    Only first word is put into past tense"""
    # TODO: Consider studying the Inflect or Pattern libraries for their grammar tools, or just use Inflect.
    if not text:
        return text
    first, sep, rest = text.partition(" ")
    if first[-1] == "y":
        if not ends_with_consonant_and_y(first):
            return first + "ed" + sep + rest
        else:
            return first[:-1] + "ied" + sep + rest
    elif first[-1] == "e":
        return first + "d" + sep + rest
    else:
        return first + "ed" + sep + rest
