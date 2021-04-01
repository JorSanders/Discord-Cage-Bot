import discord
import os
from datetime import datetime

# Bot triggers on these words
apex_words = [
    'cage',
    'apex',
    'game',
    'c a g e',
    'carry',
    'spot',
    'play',
    'ready',
    'jor',
    '1 am',
    '1am',
    'warrior',
    'wow',
    'lmao',
    'join',
    'night',
    'bique',
    'bangalore',
    'bloodhound',
    'crypto',
    'fuse',
    'gib'
    'horizon',
    'lifeline',
    'loba',
    'miraga',
    'tane',
    'path',
    'rampart',
    'rev', 
    'wattson',
    'wraith'
]

# Bot triggers in these channels
bot_channels = [
    'general',
    'cage'
]

# Bot triggers on role mentions
role_names = [
    'cage'
]

def string_contains_word(text, word_list):
    return any(word in text for word in word_list)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    def cage_related_message(self, message):
        if string_contains_word(message.content.lower(), apex_words):
            print("Apex word found in message")
            return True

        for mention in message.role_mentions:
            if string_contains_word(mention.name.lower(), role_names):
                print("Cage mention found in message")
                return True
        
        print("Not a cage message")
        return False

    async def on_message(self, message):
        if message.author.id == self.user.id:
            # We do not want the bot to reply to itself
            Print("This bot message")
            return

        if not string_contains_word(message.channel.name, bot_channels):
            # We do not want the bot to text in non whitelisted channels
            Print("Channel not in whitelist")
            return

        if self.cage_related_message(message):
            print(datetime.now().strftime("%d/%m/%y %H:%M:%S") + " - C A G E")
            await message.add_reaction('🇨')
            await message.add_reaction('🇦')
            await message.add_reaction('🇬')
            await message.add_reaction('🇪')

client = MyClient()
client.run(os.environ.get('DISCORD_BOT_TOKEN'))
