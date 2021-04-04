"""Unit-Test Discord Cage Bot"""

import unittest

from ..src.discord_cage_bot import cage_related_message, string_contains_word


class TestDiscordCageBot(unittest.TestCase):
    def test_string_contains_word(self):
        self.assertTrue(string_contains_word("I like dropping cage", ["cage"]))
        self.assertFalse(string_contains_word("I like playing caustic", ["cage"]))

    def test_cage_related_message(self):
        discord_message = type(
            "MessageMock", (object,), {"content": "", "role_mentions": []}
        )()

        self.assertFalse(cage_related_message(discord_message))

        discord_message.content = "cage"
        self.assertTrue(cage_related_message(discord_message))
        discord_message.content = ""

        discord_message.content = "caustic"
        self.assertFalse(cage_related_message(discord_message))
        discord_message.content = ""

        discord_message.role_mentions = [
            type("RoleMentionMock", (object,), {"name": "cage"})()
        ]
        self.assertTrue(cage_related_message(discord_message))
        discord_message.role_mentions = []

        discord_message.role_mentions = [
            type("RoleMentionMock", (object,), {"name": "caustic"})()
        ]
        self.assertFalse(cage_related_message(discord_message))
        discord_message.role_mentions = []


if __name__ == "__main__":
    unittest.main()
