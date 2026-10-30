import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logger = logging.getLogger(__name__)


async def start_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if update.effective_message:
        await update.effective_message.reply_text(
            "Assalamu Alaikum! 🌙\n\n"
            "Welcome to NoorixBot.\n"
            "Use /help to see the available commands."
        )


async def help_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if update.effective_message:
        await update.effective_message.reply_text(
            "🌙 NoorixBot — Commands\n\n"
            "/start — Start the bot\n"
            "/help — Show this help\n"
            "/ping — Check whether the bot is online\n"
            "/dua — Show a short dua\n"
            "/zikr — Show a short zikr\n\n"
            "More features can be added safely in future updates."
        )


async def ping_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if update.effective_message:
        await update.effective_message.reply_text("Pong! NoorixBot is online. ✅")


async def dua_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if update.effective_message:
        await update.effective_message.reply_text(
            "رَبِّ زِدْنِي عِلْمًا\n\n"
            "Meaning: My Lord, increase me in knowledge.\n"
            "(Qur'an 20:114)"
        )


async def zikr_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if update.effective_message:
        await update.effective_message.reply_text(
            "سُبْحَانَ اللَّهِ وَبِحَمْدِهِ\n\n"
            "SubhanAllahi wa bihamdihi\n"
            "Glory be to Allah and praise belongs to Him."
        )


def register_handlers(application: Application) -> None:
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("ping", ping_command))
    application.add_handler(CommandHandler("dua", dua_command))
    application.add_handler(CommandHandler("zikr", zikr_command))
    logger.info("NoorixBot command handlers registered.")
