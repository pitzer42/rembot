import os

from rembot.services import remnote
from rembot.services import telegram


def attach(app):

    INBOX_REM = os.environ['INBOX_REM']
    
    def reply_telegram_with_rem(message):
        rem_url = remnote.create_rem(INBOX_REM, message.text)
        telegram.send_message(rem_url, message.chat, message.receiver)

    app.events.on(telegram.events.MessageReceived, reply_telegram_with_rem)
