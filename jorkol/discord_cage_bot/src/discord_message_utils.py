from jorkol.discord_cage_bot.src.string_utils import match_in_regex, match_in_regexes

channel_whitelist_regexes = [r"general", r"cage"]

role_regexes = [r"cage"]

apex_regexes = [
    r"c(.|)a(.|)g(.|)e",
    r"pex",
    r"game",
    r"c a g e",
    r"carry",
    r"spot",
    r"play",
    r"ready",
    r"jor",
    r"1(.|)am",
    r"warrior",
    r"join",
    r"bique",
    r"bathe",
    r"broth",
]

yikes_regexs = ["caustic", "world(.|)s edge"]


def is_yikes_message(message):
    return match_in_regexes(message.content, yikes_regexs)


def is_cage_related_message(message):
    if match_in_regexes(message.content, apex_regexes):
        return True

    for mention in message.role_mentions:
        if match_in_regexes(mention.name, role_regexes):
            return True

    return False


def in_whitelisted_channel(message):
    return match_in_regexes(message.channel.name, channel_whitelist_regexes)


def is_cage_quote_request(message):
    return match_in_regex(message.content, r"(cage.*quote)|(quote.*cage)")


def is_cage_insult(message):
    return match_in_regex(message.content, r"stupid|lame") and match_in_regex(
        message.content, r"cage|bot"
    )
