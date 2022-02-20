# Discord Cage bot
This is a slightly overdeveloped Discord bot that replies "C A G E" or "Y I K E S" to certain messages.
Because building a dockerized, multi-platform, unit tested, and linted discord bot with GitHub CI-CD workflow is easier than manually clicking reactions in discord as an inside joke.
Note wasn't easier or faster...

## Badges
![GitHub Super-Linter](https://github.com/JorSanders/discord_cage_bot/workflows/CI%2FCD/badge.svg)

## Contribute?
Uhm why? But go ahead make a suggestion or PR, i'll probably implement it.

## Usage
The Cage bot requires a discord bot token set as env var. Get the bot token from [here](https://discord.com/developers/applications)
```shell
export CAGE_BOT_TOKEN="xxxxxxxxxxxxxxxx"
```

Start the bot natively
```shell
python -m jorkol.discord_cage_bot.src.discord_cage_bot
```

Start the bot as container
```shell
docker stop discord_cage_bot &> /dev/null; docker run -it -d --rm --name discord_cage_bot -e CAGE_BOT_TOKEN ghcr.io/jorsanders/discord_cage_bot:latest
```

Start the bot as frewly build container
```shell
docker stop discord_cage_bot &> /dev/null; docker build . -t ghcr.io/jorsanders/discord_cage_bot:local && docker run -it --rm --name discord_cage_bot -e CAGE_BOT_TOKEN ghcr.io/jorsanders/discord_cage_bot:local
```

## Setup
- Install pyenv
    - https://github.com/pyenv/pyenv
    - https://github.com/pyenv/pyenv#automatic-installer


- Install discord pip package
```shell
pip3 install -r requirements.txt
```
dev dependencies
```shell
pip3 install -r dev.requirements.txt
```
