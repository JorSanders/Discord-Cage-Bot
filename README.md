# Usage
Start the bot
```
DISCORD_BOT_TOKEN=xxxx python3 src/bot.py
```

In background
```
python3 src/bot.py &
```

In background with logging
```
python3 /usr/local/app/discord_cage_bot.py > /var/log/discord_cage_bot.log 2>&1 &
```

stop background
```
kill $(pgrep python)
```

Get the bot token from [here](https://discord.com/developers/applications)

# Setup
install python3 and pip3
install discord pip package
```
pip3 install discord
```