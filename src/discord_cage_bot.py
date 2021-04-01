import discord
import os
from datetime import datetime

apex_words = [
    'cage',
    'apex',
    'game',
    'c a g e',
    'carry',
    'spot',
    'play',
    'ready',
    'jor'
]

bot_channels = [
    'general'
]

def string_contains_word(text, word_list):
    return any(word in text for word in word_list)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            # We do not want the bot to reply to itself
            return

        if not string_contains_word(message.channel.name, bot_channels):
            # We do not want the bot to text in non whitelisted channels
            return

        if string_contains_word(message.content.lower(), apex_words):
            print(datetime.now().strftime("%d/%m/%y %H:%M:%S") + " - CAGE")
            await message.add_reaction('🇨')
            await message.add_reaction('🇦')
            await message.add_reaction('🇬')
            await message.add_reaction('🇪')

client = MyClient()

client.run(os.environ.get('DISCORD_BOT_TOKEN'))
