
from telegram.ext import Application
from plugins import register_handlers


def load_handlers(application: Application) -> None:
    register_handlers(application)
  
