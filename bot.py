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


def start(update, context) -> None:
    """ Start the conversation with the user. """
    logger.info(f"User {update.message.chat.first_name} started the bot")
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    update.message.reply_text("""Hello! This bot will define a word for you!
    \n Just send /define <your word> to get a definition!
    \n Send /help for more commands \n""")


def define(update, context) -> None:
    """ Define a word using the Dictionary API. """
    word = context.args[0]
    logger.info(f"User {update.message.chat.first_name} wants to define: {word}")

    url = f"https://api.dictionaryapi.dev/api/v1/entries/en/{word}"

    response = requests.get(url).json()
    logger.info("Checking API Response")
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
    logger.info(f"User {update.message.chat.first_name} wants to see the source code")
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    update.message.reply_text("You can view the source code here https://github.com/mascode/Telexicon")


def help(update, context) -> None:
    """Help command"""
    logger.info(f"User {update.message.chat.first_name} asked for help")
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    update.message.reply_text(""" Send /start to start the bot.\n
    Send /define <your word> to get a definition.\n
    Send /source to see the source code.\n
    Send /help to see all commands.\n
    Remember to use the / before the command!\n
    If you want these commands as a menu then you will have to set that up with the @BotFather.\n
    For any questions or suggestions please see the github page with /source.
    """)


def main() -> None:
    """ Start the bot. """
    updater = Updater(API_Token, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("define", define))
    dispatcher.add_handler(CommandHandler("source", source))
    dispatcher.add_handler(CommandHandler("help", help))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    logger.info("Starting bot")
    main()
