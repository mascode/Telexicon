### Telexicon (A portmanteau of Telegram + Lexicon)

A self hosted dictionary for Telegram. This bot uses a dictionary API to look up words and send you the definitions. 

### Libraries

This bot uses: 

-[PyDictionary](https://github.com/geekpradd/PyDictionary/) - For definitions
-[WordHoard](https://github.com/johnbumgarner/wordhoard) - For synonyms and antonyms
-[Python-Telegram-Bot](https://github.com/python-telegram-bot/python-telegram-bot) - API Wrapper for Telegram written in Python

##### Commands

`/start - Start the bot`

`/help - Get help and info`

`/source - Get the source code (this page)`

`/define - Define a word`

`/synonym - Get the synonym(s) of a word`

`/antonym - Get the antonym(s) of a word`

##### Setup

1. Creat a new bot with [@Botfather](https://t.me/botfather) and grab the API key.

2. Copy/rename .env-example to .env and place your API key in there in between the double quotes. 

3. Setup a virtual environment and activate it. 

4. Install requirements via `pip install -r requirements.txt`in your virtual environment

5. Run `python3 bot.py`

##### Deploy on Heroku

- Connect repository to account either through Heroku CLI or github

- In Config Vars add a new Key (API_Token) and Value (Your API Key)

- Deploy


#### Deploy on Caprover

- Connect repository to account 

- Add you `API_Key` as an environment variable

- Deploy