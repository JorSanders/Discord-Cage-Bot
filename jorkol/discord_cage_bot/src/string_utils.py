"""This is a module that loads a random quotes"""

from random import randrange


def string_contains_word(text, word_list):
    return any(word in text for word in word_list)


def cagify_string(text):
    words = text.split()
    word_count = len(words)
    cage_count = int(word_count / 10)

    if cage_count == 0:
        cage_count = 1

    for _ in range(cage_count):
        index = randrange(word_count)

        if words[index].endswith("."):
            words[index] = "cage."
        elif words[index].endswith(","):
            words[index] = "cage,"
        else:
            words[index] = "cage"

    return "".join(words)
