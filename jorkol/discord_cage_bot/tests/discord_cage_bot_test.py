"""Unit-Test Discord Cage Bot"""

import unittest

from jorkol.discord_cage_bot.src.discord_cage_bot import (
    is_cage_related_message,
    is_yikes_message,
    is_whitelisted_channel,
    string_contains_word,
)


class TestDiscordCageBot(unittest.TestCase):
    def test_string_contains_word(self):
        self.assertTrue(string_contains_word("I like dropping cage", ["cage"]))
        self.assertFalse(string_contains_word("I like playing caustic", ["cage"]))

    def test_is_whitelisted_channel(self):
        self.assertFalse(is_whitelisted_channel(""))
        self.assertTrue(is_whitelisted_channel("general"))
        self.assertFalse(is_whitelisted_channel("memes"))

    def test_is_cage_related_message(self):
        discord_message = type(
            "MessageMock", (object,), {"content": "", "role_mentions": []}
        )()

        self.assertFalse(is_cage_related_message(discord_message))

        discord_message.content = "cage"
        self.assertTrue(is_cage_related_message(discord_message))
        discord_message.content = ""

        discord_message.content = "caustic"
        self.assertFalse(is_cage_related_message(discord_message))
        discord_message.content = ""

        discord_message.role_mentions = [
            type("RoleMentionMock", (object,), {"name": "cage"})()
        ]
        self.assertTrue(is_cage_related_message(discord_message))
        discord_message.role_mentions = []

        discord_message.role_mentions = [
            type("RoleMentionMock", (object,), {"name": "caustic"})()
        ]
        self.assertFalse(is_cage_related_message(discord_message))
        discord_message.role_mentions = []

    def test_is_yikes_message(self):
        discord_message = type(
            "MessageMock", (object,), {"content": "", "role_mentions": []}
        )()

        self.assertFalse(is_yikes_message(discord_message))

        discord_message.content = "caustic"
        self.assertTrue(is_yikes_message(discord_message))
        discord_message.content = ""

        discord_message.content = "cage"
        self.assertFalse(is_yikes_message(discord_message))
        discord_message.content = ""


if __name__ == "__main__":
    unittest.main()
