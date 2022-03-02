import logging
import os
from telegram.chataction import ChatAction
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
from PyDictionary import PyDictionary
from wordhoard import Antonyms, Synonyms

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
    \nJust send /define <your word> to get a definition!
    \nSend /help for more commands""")


def define(update, context) -> None:
    """ Define a word using the Dictionary API. """
    word = context.args[0]
    logger.info(f"User {update.message.chat.first_name} wants to define: {word}")
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    Dictionary = PyDictionary()
    Definition = Dictionary.meaning(word)

    if Definition is None or Definition == {}:
        logger.info(f"Could not find a definition for {word}. Notifying user {update.message.chat.first_name} ")
        update.message.reply_text(f"Sorry, I couldn't find a definition for: {word}. Try again and/or check spelling.")
    else:
        logger.info(f"Found a definition for {word}. Notifying user {update.message.chat.first_name} ")
        definitions = []
        for key, value in Definition.items():
            definitions.append(f"{key}: {value}")
        update.message.reply_text(f"{word}: \n\n".capitalize() + "\n\n".join(definitions))
        logger.info(f"Sent the definition(s) for {word} to user {update.message.chat.first_name}")


def antonym(update, context) -> None:
    """Antonyms of a word"""
    word = context.args[0]
    logger.info(f"User {update.message.chat.first_name} wants to find antonyms for: {word}")
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    antonym = Antonyms(word)
    results = antonym.find_antonyms()
    if results == []:
        logger.info(f"Could not find antonym for {word}. Notifying user {update.message.chat.first_name} ")
        update.message.reply_text(f"Sorry, I couldn't find any antonyms for: {word}")
    else:
        logger.info(f"Found antonyms for {word}. Notifying user {update.message.chat.first_name} ")
        update.message.reply_text(", ".join(results))


def synonym(update, context) -> None:
    """Synonyms of a word"""
    word = context.args[0]
    logger.info(f"User {update.message.chat.first_name} wants to find synonyms for: {word}")
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    synonym = Synonyms(word)
    results = synonym.find_synonyms()
    if results == []:
        logger.info(f"Could not find synonyms for {word}. Notifying user {update.message.chat.first_name} ")
        update.message.reply_text(f"Sorry, I couldn't find any synonyms for: {word}")
    else:
        logger.info(f"Found synonyms for {word}. Notifying user {update.message.chat.first_name} ")
        update.message.reply_text(", ".join(results))


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
Send /define your_word to get a definition.\n
Send /source to see the source code.\n
Send /help to see all commands.\n
Remember to use the / before the command!\n
If you want these commands as a menu then you will have to set that up with the @BotFather.\n
For any questions or suggestions please see the github page with /source.\n
    """)


def main() -> None:
    """ Start the bot. """
    updater = Updater(API_Token, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("define", define))
    dispatcher.add_handler(CommandHandler("source", source))
    dispatcher.add_handler(CommandHandler("synonym", synonym))
    dispatcher.add_handler(CommandHandler("antonym", antonym))
    dispatcher.add_handler(CommandHandler("help", help))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    logger.info("Starting bot")
    main()
