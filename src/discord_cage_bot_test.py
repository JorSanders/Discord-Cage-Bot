from .discord_cage_bot import cage_related_message
from .discord_cage_bot import string_contains_word
from .discord_cage_bot import DiscordCageClient
from mock import Mock
import unittest

class DiscordMessageMock():
    content = ""
    role_mentions = []

class DiscordRoleMentionMock():
    name = ""

class TestDiscordCageBot(unittest.TestCase):
    def test_string_contains_word(self):
       self.assertTrue(string_contains_word("I like dropping cage", ["cage"]))
       self.assertFalse(string_contains_word("I like playing caustic", ["cage"]))

    def test_cage_related_message(self):
        discord_message = type('MessageMock', (object,),{'content':'', 'role_mentions': []})()

        self.assertFalse(cage_related_message(discord_message))

        discord_message.content='cage'
        self.assertTrue(cage_related_message(discord_message))
        discord_message.content=''

        discord_message.content='caustic'
        self.assertFalse(cage_related_message(discord_message))
        discord_message.content=''

        discord_message.role_mentions=[type('RoleMentionMock', (object,),{'name':'cage'})()]
        self.assertTrue(cage_related_message(discord_message))
        discord_message.role_mentions=[]

        discord_message.role_mentions=[type('RoleMentionMock', (object,),{'name':'caustic'})()]
        self.assertFalse(cage_related_message(discord_message))
        discord_message.role_mentions=[]

if __name__ == '__main__':
    unittest.main()