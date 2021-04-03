# Usage

[local] Start the bot
```shell
DISCORD_BOT_TOKEN=xxxx python3 src/discord_cage_bot.py
```

[remote] In background with logging
```shell
python3 -u /usr/local/app/discord_cage_bot.py > /var/log/discord_cage_bot.log 2>&1 &
```

Stop background (not safe)
```shell
kill $(pgrep python)
```

Get the bot token from [here](https://discord.com/developers/applications)

# Setup
install python3 and pip3
install discord pip package
```shell
pip3 install discord
```
