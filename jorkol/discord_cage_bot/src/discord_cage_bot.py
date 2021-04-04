"""This is a Discord bot that replies C A G E to certain messages"""

import os
from datetime import datetime

import discord

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
    "up",
]

yikes_words = ["caustic", "worlds edge", "world's edge"]


def log(text):
    if __name__ == "__main__":
        print(text)


def string_contains_word(text, word_list):
    return any(word in text for word in word_list)


def is_yikes_message(message):
    return string_contains_word(message.content.lower(), yikes_words)


def is_cage_related_message(message):
    if string_contains_word(message.content.lower(), apex_words):
        log("Apex word found in message")
        return True

    for mention in message.role_mentions:
        if string_contains_word(mention.name.lower(), role_names):
            log("Cage mention found in message")
            return True

    log("Not a cage message")
    return False


def is_whitelisted_channel(channel_name):
    return string_contains_word(channel_name, whitelisted_channels)


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

        if not is_whitelisted_channel(message.channel.name):
            # We do not want the bot to text in non whitelisted channels
            log("Channel not in whitelist")
            return

        if is_yikes_message(message):
            log(datetime.now().strftime("%d/%m/%y %H:%M:%S") + " - C A G E")
            await message.add_reaction("🇾")
            await message.add_reaction("🇮")
            await message.add_reaction("🇰")
            await message.add_reaction("🇪")
            await message.add_reaction("🇸")
            return

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
