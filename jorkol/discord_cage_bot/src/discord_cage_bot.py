"""This is a Discord bot that replies C A G E to certain messages"""

import os
from datetime import datetime

import discord

from jorkol.discord_cage_bot.src.quote_generator import random_quote
from jorkol.discord_cage_bot.src.discord_message_utils import in_whitelisted_channel
from jorkol.discord_cage_bot.src.discord_message_utils import is_yikes_message
from jorkol.discord_cage_bot.src.discord_message_utils import is_cage_related_message
from jorkol.discord_cage_bot.src.discord_message_utils import is_cage_quote_request
from jorkol.discord_cage_bot.src.string_utils import cagify_string


def log(text):
    if __name__ == "__main__":
        print(text)


class DiscordCageClient(discord.Client):
    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

    async def on_message(self, message):
        log("Message received")
        if message.author.id == self.user.id:
            # We do not want the bot to reply to itself
            log("This bot message")
            return

        if not in_whitelisted_channel(message):
            # We do not want the bot to text in non whitelisted channels
            log("Channel not in whitelist")
            return

        if is_yikes_message(message):
            log(datetime.now().strftime("%d/%m/%y %H:%M:%S") + " - Y I K E S")
            await message.add_reaction("🇾")
            await message.add_reaction("🇮")
            await message.add_reaction("🇰")
            await message.add_reaction("🇪")
            await message.add_reaction("🇸")
            return

        if is_cage_quote_request(message):
            await message.reply(
                "You asked for a Cage quote? I shall deliver: \n"
                + cagify_string(random_quote())
            )

        if is_cage_related_message(message):
            log(datetime.now().strftime("%d/%m/%y %H:%M:%S") + " - C A G E")
            await message.add_reaction("🇨")
            await message.add_reaction("🇦")
            await message.add_reaction("🇬")
            await message.add_reaction("🇪")
            return


if __name__ == "__main__":
    discord_cage_client = DiscordCageClient()
    discord_cage_client.run(os.environ.get("DISCORD_BOT_TOKEN"))
