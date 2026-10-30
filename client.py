from telegram.ext import Application


def build_application(token: str) -> Application:
    """Create the Telegram Bot API application."""
    return Application.builder().token(token).build()
