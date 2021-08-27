from rembot.services import remnote
from rembot.services import telegram
from rembot.services.telegram.events import MessageReceived


INBOX_REM = 'q5MhuXuBri2tn4qc5'


async def start(events):

    async def rem_id_from_message(message):
        if message.replies:
            # replied a message with a URL?
            if 'https://' in message.replies:
                return remnote.rem_id_from_url(message.replies)
            else:
                rem = await remnote.get_by_name(message.replies)
                return rem['_id']
        return INBOX_REM

    async def reply_telegram_with_rem(message):
        parent = await rem_id_from_message(message)
        text = message.text
        rem_url = await remnote.create(parent, text)
        message_id = message.message_id
        print(f'telegram_to_rem: {text} {rem_url}')
        await telegram.reply_message(message_id, rem_url)

    events.on(MessageReceived, reply_telegram_with_rem)
