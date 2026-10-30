import logging
import os

from core.client import build_application
from core.loader import load_handlers

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("NoorixBot")


def main() -> None:
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "BOT_TOKEN is missing. Add your BotFather token in Render "
            "Environment Variables; never put it in source code."
        )

    application = build_application(token)
    load_handlers(application)

    logger.info("NoorixBot is starting...")
    application.run_polling(
        allowed_updates=["message"],
        drop_pending_updates=True,
    )


if __name__ == "__main__":
    main()
