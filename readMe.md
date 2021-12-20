### Telexicon (A portmanteau of Telegram + Lexicon)

A self hosted dictionary for Telegram. This bot uses a dictionary API to look up words and send you the definitions. 

##### APIs

The API that this bot uses is generously provided by the [Free Dictionary API](https://github.com/meetDeveloper/freeDictionaryAPI). No API key needed to use the service. Please support the project if you can. 

The bot also uses the [pytho-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) API wrapper to interact with the Telegram API.

##### Commands

`/start - Start the bot`

`/help - Get help and info`

`/source - Get the source code (this page)`

`/define - define a word`

##### Limitations

The dictionary API has a rate limit of 300 requests every 5 mins

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
