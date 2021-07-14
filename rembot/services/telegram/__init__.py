import os
import asyncio

from aiotelegrambot import Bot, Client, Content, Message
from aiotelegrambot.rules import Contains

from rembot.services.telegram.events import MessageReceived


from collections import namedtuple



TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']


async def run(bot: Bot):
    await bot.initialize()
    


async def send_message(text, chat, bot):
    await bot.send_message(text, True)


async def attach(app):

    async def handle(message):
        text = message.raw['message']['text']
        event = MessageReceived(text, None, message)
        await app.events.notify(event)


    client = Client(TELEGRAM_BOT_TOKEN)
    bot = Bot(client)
    bot.add_handler(handle, content_type=Content.TEXT)

    await bot.initialize()

    """
    try:
        
    except KeyboardInterrupt:
        loop.run_until_complete(bot.close())
        loop.run_until_complete(bot.client.close())
    finally:
        loop.close()
        """