import argparse
import logging
import os
import sys

from datetime import datetime

import discord

from jorkol.discord_cage_bot.src.quote_generator import random_quote
from jorkol.discord_cage_bot.src.discord_message_utils import in_whitelisted_channel
from jorkol.discord_cage_bot.src.discord_message_utils import is_yikes_message
from jorkol.discord_cage_bot.src.discord_message_utils import is_cage_related_message
from jorkol.discord_cage_bot.src.discord_message_utils import is_cage_quote_request
from jorkol.discord_cage_bot.src.discord_message_utils import is_cage_insult
from jorkol.discord_cage_bot.src.string_utils import cagify_string


class DiscordCageClient(discord.Client):
    async def on_ready(self):
        logging.info(
            """Logged in as:
            user: %s
            id: %s""",
            self.user.name,
            self.user.id,
        )

    async def on_message(self, message):
        logging.info(
            "%s Message received", datetime.now().strftime("%d/%m/%y %H:%M:%S")
        )
        if message.author.id == self.user.id:
            logging.info("Message detected by this bot")
            return

        if not in_whitelisted_channel(message):
            logging.info("Message channel not whitelisted")
            return

        if is_yikes_message(message):
            logging.info("Message is Y I K E S")
            await message.add_reaction("🇾")
            await message.add_reaction("🇮")
            await message.add_reaction("🇰")
            await message.add_reaction("🇪")
            await message.add_reaction("🇸")
            return

        if is_cage_quote_request(message):
            logging.info("Message is request for cage quote")
            await message.reply(
                "You asked for a Cage quote? I shall deliver: \n"
                + cagify_string(random_quote())
            )
            return

        if is_cage_insult(message):
            logging.info("Message is an insult")
            await message.reply(insult_response())
            return

        if is_cage_related_message(message):
            logging.info("Message is C A G E")
            await message.add_reaction("🇨")
            await message.add_reaction("🇦")
            await message.add_reaction("🇬")
            await message.add_reaction("🇪")
            return


def insult_response():
    return """What the fuck did you just fucking say about me, you little bitch? \
            I'll have you know I graduated top of my class in the  IMC Military Academy, and I've been involved in numerous secret raids on the SRS Militia, and I have over 300 confirmed kills. \
            I am trained in gorilla warfare and I'm the top Kraber player in Titanfall. \
            You are nothing to me but just another target. \
            I will wipe you the fuck out with precision the likes of which has never been seen before on this Kings Canyon, mark my fucking words. \
            You think you can get away with saying that shit to me over the Internet? \
            Think again, fucker. As we speak I am contacting my secret network of spies across the Syndicate and your IP is being traced right now so you better prepare for the ring, maggot. \
            The ring that wipes out the pathetic little thing you call your life. \
            You're fucking dead, kid. \
            I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my Mozambique. \
            Not only am I extensively trained in Mozambique, \
            but I have access to the entire arsenal of the  IMC and I will use it to its full extent to wipe your miserable ass off the face of the continent, \
            you little shit. \
            If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. \
            But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. \
            I will shit fury all over you and you will drown in it. \
            You're fucking dead, kiddo. \
        """


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--loglevel",
        default="warning",
        help="Provide logging level. Example --loglevel debug, default=warning",
    )

    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel.upper())

    discord_cage_client = DiscordCageClient()
    discord_token = os.environ.get("CAGE_BOT_TOKEN")
    if discord_token == "":
        logging.error("CAGE_BOT_TOKEN env var undefined")
        sys.exit(1)
    discord_cage_client.run(discord_token)
