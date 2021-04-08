from jorkol.discord_cage_bot.src.string_utils import string_contains_word

whitelisted_channels = ["general", "cage"]

role_names = ["cage"]

apex_words = [
    "cage",
    "apex",
    "game",
    "c a g e",
    "carry",
    "spot",
    "play",
    "ready",
    "jor",
    "1 am",
    "1am",
    "warrior",
    "wow",
    "lmao",
    "join",
    "night",
    "bique",
    "bangalore",
    "bloodhound",
    "crypto",
    "fuse",
    "gib",
    "horizon",
    "lifeline",
    "loba",
    "miraga",
    "tane",
    "path",
    "rampart",
    "rev",
    "wattson",
    "wraith",
    "bathe",
    "broth",
    "down",
    " up",
]

yikes_words = ["caustic", "worlds edge", "world's edge"]


def is_yikes_message(message):
    return string_contains_word(message.content.lower(), yikes_words)


def is_cage_related_message(message):
    if string_contains_word(message.content.lower(), apex_words):
        return True

    for mention in message.role_mentions:
        if string_contains_word(mention.name.lower(), role_names):
            return True

    return False


def in_whitelisted_channel(message):
    return string_contains_word(message.channel.name, whitelisted_channels)


def is_cage_quote_request(message):
    content = message.content.lower()
    return "cage" in content and "quote" in content


def is_cage_insult(message):
    content = message.content.lower()
    return string_contains_word(content, ["cage", "bot"]) and string_contains_word(
        content, ["stupid", "lame"]
    )
