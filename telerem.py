import os
import requests
from telegram.ext import Updater, MessageHandler, Filters, Handler


""" keep app alive on heroku """
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Telerem'


REMNOTE_API_URL_CREATE = 'https://api.remnote.io/api/v0/create'
REMNOTE_DOC_URL = 'https://www.remnote.io/document/'
REMNOTE_API_KEY = os.getenv('REMNOTE_API_KEY')
REMNOTE_USER_ID = os.getenv('REMNOTE_USER_ID')
ROOT_REM = os.getenv('ROOT_REM')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

assert None not in (
    REMNOTE_API_KEY,
    REMNOTE_USER_ID,
    ROOT_REM,
    TELEGRAM_BOT_TOKEN)


def create_inbox_rem(update, context):
    request_data = dict(
        apiKey=REMNOTE_API_KEY,
        userId=REMNOTE_USER_ID,
        parentId=ROOT_REM,
        text=update.message.text,
        positionAmongstSiblings=0)
    response = requests.post(REMNOTE_API_URL_CREATE, data=request_data)
    response_data = response.json()
    rem_url = REMNOTE_DOC_URL + response_data['remId']
    context.bot.send_message(chat_id=update.effective_chat.id, text=rem_url)


updater = Updater(TELEGRAM_BOT_TOKEN)
handler = MessageHandler(Filters.all, create_inbox_rem)
updater.dispatcher.add_handler(handler)
updater.start_polling()
updater.idle()


