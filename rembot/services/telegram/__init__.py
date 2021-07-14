import os
import asyncio

from aiotelegrambot import Bot, Client, Content, Message
from aiotelegrambot.rules import Contains

from rembot.services.telegram.events import MessageReceived


from collections import namedtuple



TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']


async def run(bot: Bot):
    await bot.initialize()
    while True:
        await asyncio.sleep(1)


def send_message(text, chat, bot):
    await bot.send_message(text, True)


def attach(app):

    async def handle(message):
        text = message.raw['message']['text']
        event = MessageReceived(text, None, message)
        app.events.notify(event)


    loop = asyncio.get_event_loop()
    client = Client(TELEGRAM_BOT_TOKEN)
    bot = Bot(client)
    bot.add_handler(handle, content_type=Content.TEXT)

    try:
        loop.run_until_complete(run(bot))
    except KeyboardInterrupt:
        loop.run_until_complete(bot.close())
        loop.run_until_complete(bot.client.close())
    finally:
        loop.close()