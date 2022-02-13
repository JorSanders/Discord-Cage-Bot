FROM python:3.10-alpine

RUN pip install discord requests

COPY jorkol /usr/local/app/jorkol

WORKDIR /usr/local/app

ENTRYPOINT python -m jorkol.discord_cage_bot.src.discord_cage_bot
