import os

from rembot.services import remnote
from rembot.services import telegram

from rembot.services.telegram.events import MessageReceived

INBOX_REM = os.environ['INBOX_REM']

_map_text_to_rem_url = dict()

async def attach(events):

    async def reply_telegram_with_rem(message):
        parent = INBOX_REM
    
        # reply with sub rem
        if message.replies:
            # replied to text, I need a URL
            if message.replies in _map_text_to_rem_url:
                reply_url = _map_text_to_rem_url[message.replies]
                parent = remnote.parse_rem_id_from_url(reply_url)
            elif '/' in message.replies:
                parent = remnote.parse_rem_id_from_url(message.replies)
        
        rem_url = await remnote.create(parent, message.text)
        _map_text_to_rem_url[message.text] = rem_url
        await telegram.reply_message(message.chat_id, message.message_id, rem_url)
        print(f'chat_id={message.chat_id}')

    events.on(MessageReceived, reply_telegram_with_rem)
