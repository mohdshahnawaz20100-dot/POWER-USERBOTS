from telegram.ext import Application

from plugins import register_handlers


def load_handlers(application: Application) -> None:
    """Register all public bot command handlers."""
    register_handlers(application)
