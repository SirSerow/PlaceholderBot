import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")

NEW_BOT_NAME = os.getenv("NEW_BOT_NAME", "")

bot_mention = f"@{NEW_BOT_NAME}" if NEW_BOT_NAME else "our new bot"

PLACEHOLDER_MESSAGE = (
    f"This bot has moved! Please switch to {bot_mention} for further updates. "
    "We are sorry for the inconvenience and look forward to seeing you there!"
)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handler for the /start command (optional).
    """
    await update.message.reply_text(PLACEHOLDER_MESSAGE)


async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handler for any incoming message that is not a command.
    Replies with the placeholder message.
    """
    await update.message.reply_text(PLACEHOLDER_MESSAGE)


def main():
    """
    Build the application and run it in a blocking manner, letting
    python-telegram-bot manage the asyncio event loop internally.
    """
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message)
    )

    application.run_polling()


if __name__ == "__main__":
    main()
