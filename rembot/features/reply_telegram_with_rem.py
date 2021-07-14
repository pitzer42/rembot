import os

from rembot.services import remnote
from rembot.services import telegram

from rembot.services.telegram.events import MessageReceived


async def attach(app):

    INBOX_REM = os.environ['INBOX_REM']
    
    async def reply_telegram_with_rem(message):
        rem_url = remnote.create_rem(INBOX_REM, message.text)
        await telegram.send_message(rem_url, message.chat, message.receiver)

    app.events.on(MessageReceived, reply_telegram_with_rem)
