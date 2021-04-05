"""This is a module that loads a random quotes"""

from random import randrange


def string_contains_word(text, word_list):
    return any(word in text for word in word_list)


def cagify_string(text):
    words = text.split()
    word_count = len(words)
    cage_count = int(word_count * 0.15)

    if cage_count == 0:
        cage_count = 1

    for _ in range(cage_count):
        index = randrange(word_count)

        cagification = "cage"

        if words[index][0].isupper():
            cagification = cagification.capitalize()

        if words[index].endswith("."):
            cagification += "."
        elif words[index].endswith(","):
            cagification += ","

        words[index] = cagification

    return " ".join(words)
