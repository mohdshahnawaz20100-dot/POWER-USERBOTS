# NoorixBot

A public Telegram Bot API starter project.

## Local setup

1. Install Python 3.10+.
2. Install dependencies: `pip install -r requirements.txt`
3. Set the `BOT_TOKEN` environment variable using the token from BotFather.
4. Run: `python main.py`

## Render

Deploy this repository as a **Background Worker**. The included `render.yaml`
sets the build and start commands. Add `BOT_TOKEN` in Render's Environment
settings as a secret value.

Never commit your BotFather token, personal Telegram session files, API hash,
or private configuration.

## Included commands

- `/start`
- `/help`
- `/ping`
- `/dua`
- `/zikr`

This is a clean Bot API starter, not a direct copy of a Telethon userbot.
Userbot-only features must be reviewed and adapted individually.
