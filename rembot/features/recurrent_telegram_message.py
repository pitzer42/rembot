import asyncio

from rembot.services import telegram


async def attach(events):

    while True:
        await asyncio.sleep(10)
        #telegram.send_message(0, 'ping')
        print('ping')
