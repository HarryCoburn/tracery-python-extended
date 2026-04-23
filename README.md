# Tracery 1.x for Python

## About

This is an implementation of the earlier version of the [Tracery](https://github.com/galaxykate/tracery/tree/master) library by Kate Compton into Python. This is not Tracery2, nor the tracery2 branch in the project above. Those features may get added later and I will likely extend it further once I use it in some of my other projects.

## Why convert it?

I did this conversion as my first personal project for [boot.dev](https://boot.dev). I have played several games that used random text generation or took a base text and changed it based on who was talking. Tracery seemed like the way to go, but it was in JS. 

I have some experience in JS of that vintage, but I do not like the language so I put it into Python. This has the added benefit that I may be able to turn it into a library to use with Evennia for MUD text randomization.

## Basic Usage

To use it, you need to have a Tracery grammar first. More on that below. Once you have one:

```
import Grammar

grammar = Grammar(your_grammar_object)
response = grammar.flatten("#origin#")
```

Create an instance of the Grammar class with your grammar, then use flatten() on an origin point in your grammar to generate a random string that fits the grammar.

## About Tracery grammars

Instead of JSON, this version uses python dictionaries where each key:value pair has a string key and a value of a list of strings.

The key "origin" (or whatever you choose) holds the base statement you're creating. For now, you must place the key between two # signs when you use flatten.

### Hashtags

Hashtag pairs are used to tag parts of a sentence for replacement.

```
color_sentence = {
  "sentence": ["This color is #color#"],
  "color": ["red", "green", "blue"]
}

color_grammar = Grammar(color_sentence)
response = color_grammar.flatten()
```

### Modifiers

Modifiers take the result of a hashtag pair and runs an additional function on it. The modifiers.py has base modifiers, but this can be extended. Modifiers are marked using the . symbol, and they can be chained.

Examples:

#color.capitalize# would capitalize the first letter in whatever #color# returned.

#color.s# would pluralize whatever #color# returned

#color.capitalize.s# would do both, starting with capitalizing and then pluralizing.

This functionality may get extended later with the Inflect library. It is built for this sort of transformation.

### Actions

Actions will get renamed later, but they serve as variables to retain story information across a generation. They are in the form:

```
[action:#tag#]
```

After it runs, whatever #tag# returns will be stored in #action# and can be referred to. Notably, it will stay consistent because it will be the only option.

An slice of an example from one of the original tutorials:

```
{
"origin": ["#[hero:#name#][heroPet:#animal#]story#"],
"story": [
        "#hero# traveled with her pet #heroPet#.  #hero# was never #mood#, for the #heroPet# was always too #mood#."
    ],
}
```

In this sample, #mood# could end up being two separate moods, but the #name# stored in hero: will always be the same when #hero# is called, unless the full action is called again.

### Nesting

There's nothing stopping you from nesting actions or tags to create loops within your story. Just make sure you have a way out so you don't create an infinite loop.

### TODO

- Change action to something like StoryVar, since that's what they seem to be acting like
- Create some sort of an Accent system to transform a whole sentence based on accent rules (e.g. Chrono Cross)
- Follow up on later versions of Tracery to see how it was extended
- Consider if there is a better way to make the grammars than magic strings
