import asyncio

from datetime import datetime

from rembot.services import scheduler


async def attach(events):

    async def ping():
        print('ping')
    
    async def pong():
        print('pong')

    past = datetime.now()
    scheduler.schedule(ping, past, repeat=scheduler.ASAP * 8)
    scheduler.schedule(pong, past, repeat=scheduler.ASAP * 4)
