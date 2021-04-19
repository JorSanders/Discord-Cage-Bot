from random import randrange


def string_contains_word(text, word_list):
    return any(word in text for word in word_list)


def is_to_be_verb(word):
    word = strip_non_alpha(word).lower()
    return word in ["be", "is", "am", "are", "was", "were"]


def is_cage(word):
    word = strip_non_alpha(word).lower()
    return word in ["cage", "caged", "caging", "cagism"]


def is_cagifyable(word):
    return not (is_to_be_verb(word) or is_cage(word) or is_signal_word(word))


def is_signal_word(word):
    word = strip_non_alpha(word).lower()
    return word in [
        "and",
        "as",
        "additionally",
        "along",
        "with",
        "also",
        "in",
        "plus",
        "similarly",
        "likewise",
        "too",
        "but",
        "although",
        "however",
        "instead",
        "except",
        "currently",
        "while",
        "now",
        "later",
        "next",
        "ultimately",
    ]


def strip_non_alpha(text):
    return "".join(char for char in text if char.isalpha())


def cagify_string(text):
    words = text.split()
    word_count = len(words)
    cage_count = int(word_count * 0.08)

    if cage_count == 0:
        cage_count = 1

    for _ in range(cage_count):

        # 10 rolls to find a cagifyable word
        for _ in range(10):
            index = randrange(word_count)
            if is_cagifyable(words[index]):
                break

        words[index] = cagify_word(words[index])

    return " ".join(words)


def cagify_word(word):
    cagification = "cage"

    special_suffix = ""

    for i in range(1, len(word) + 1):
        if word[-i].isalpha():
            break

        special_suffix += word[-i]

    word = strip_non_alpha(word)

    if word.endswith("ed"):
        cagification = "caged"
    elif word.endswith("ing"):
        cagification = "caging"
    elif word.endswith("ism"):
        cagification = "cagism"

    if len(word) > 0 and word[0].isupper():
        cagification = cagification.capitalize()

    cagification += special_suffix

    return cagification
