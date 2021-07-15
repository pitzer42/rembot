import os
import asyncio

from aiogram import Bot, Dispatcher, executor, types

from rembot.services.telegram.events import MessageReceived


TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

_bot = Bot(token=TELEGRAM_BOT_TOKEN)
_dispatcher = Dispatcher(_bot)


async def attach(events):

    @_dispatcher.message_handler()
    async def _notify(message):
        chat_id = message.chat.id
        text = message.text
        message_id = message.message_id
        replies = None if not message.reply_to_message else message.reply_to_message.text
        event = MessageReceived(chat_id, message_id, text, replies)
        await events.notify(event)

    asyncio.create_task(_dispatcher.start_polling())


async def send_message(chat_id, text):
    await _bot.send_message(chat_id, text)


async def reply_message(chat_id, message_id, text):
    await _bot.send_message(chat_id, text, reply_to_message_id=message_id)
