import logging
from random import randrange
import re

to_be_verb_regexes = [r"^be$", r"^is$", r"^am$", r"^are$", r"^was$", r"^were$"]

signal_word_regexes = [
    r"^and$",
    r"^as$",
    r"^or$",
    r"^additionally$",
    r"^along$",
    r"^with$",
    r"^also$",
    r"^in$",
    r"^plus$",
    r"^similarly$",
    r"^likewise$",
    r"^too$",
    r"^but$",
    r"^although$",
    r"^however$",
    r"^instead$",
    r"^except$",
    r"^currently$",
    r"^while$",
    r"^now$",
    r"^later$",
    r"^next$",
    r"^ultimately$",
    r"^no$",
    r"^yes$",
    r"^the$",
    r"^a$",
    r"^an$",
    r"^affirmative$",
]

cage_word_regexes = [r"cage", r"caging", r"cagism"]


def match_in_regex(text, regex):
    pattern = re.compile(regex, re.IGNORECASE)
    return pattern.search(text)


def match_in_regexes(text, regexes):
    for regex in regexes:
        if match_in_regex(text, regex):
            return True
    return False


def strip_non_alpha(text):
    return "".join(char for char in text if char.isalpha())


def is_to_be_verb(word):
    return match_in_regexes(strip_non_alpha(word), to_be_verb_regexes)


def is_signal_word(word):
    return match_in_regexes(strip_non_alpha(word), signal_word_regexes)


def is_cage_word(word):
    return match_in_regexes(strip_non_alpha(word), cage_word_regexes)


def is_cagifyable(word):
    return not (is_to_be_verb(word) or is_cage_word(word) or is_signal_word(word))


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

    logging.debug("Replacing '%s' with '%s'", word, cagification)

    return cagification


def cagify_string(text):
    words = text.split()
    word_count = len(words)
    cage_count = int(word_count * 0.1)

    if cage_count == 0:
        cage_count = 1

    for _ in range(cage_count):

        # 40 rolls to find a cagifyable word
        for _ in range(40):
            index = randrange(word_count)
            if is_cagifyable(words[index]):
                break

        logging.debug(
            "Replacing #{%s} in word index {%d}/{%d} ", words[index], index, word_count
        )
        words[index] = cagify_word(words[index])

    return " ".join(words)
