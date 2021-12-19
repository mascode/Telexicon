import requests
import logging
import os
from telegram.chataction import ChatAction
from telegram.ext import Updater, CommandHandler 
from dotenv import load_dotenv


logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
API_Token = os.getenv("API_Token")

logger = logging.getLogger(__name__)

def start(update, context) -> None:
    """Start the bot."""
    logger.info(f"User {update.message.chat.first_name} started the bot")
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    update.message.reply_text('Hello! This bot will define a word for you! \n Just send /define <your word> to get a definition!')

def define(update, context) -> None:
    """Define a word"""
    word = context.args[0]
    logger.info(f"User {update.message.chat.first_name} wants to define: {word}")

    url = f"https://api.dictionaryapi.dev/api/v1/entries/en/{word}"

    response = requests.get(url).json()
    logger.info(f"Checking API Response")
    if type(response) == dict:
        logger.info(f"Could not find a defintion for: {word}")
        update.message.reply_text(f"Sorry, I couldn't find the word: {word}")
    else:
        logger.info(f"Found a definition for: {word}")
        word = response[0]["word"]
        definitions = []
        for meaning in response[0]["meaning"].values():
            for definition in meaning:
                definitions.append(definition["definition"])
        logger.info(f"Sending definitions for: {word} to User: {update.message.chat.first_name}")
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        update.message.reply_text(f"{word}:\n {' '.join(definitions)}")
    
def source(update, context) -> None:
    """Source code"""
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    update.message.reply_text("Check out the source code here ")

def main() -> None:
    """Start the bot."""
    updater = Updater(API_Token, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("define", define))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
