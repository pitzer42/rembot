import asyncio

from rembot.services import telegram
from rembot.features import reply_telegram_with_rem
from rembot.event_bus import EventBus


async def main():

    events = EventBus()
    await reply_telegram_with_rem.attach(events)
    await telegram.attach(events)

    print('running...')

    while True:
        await asyncio.sleep(1)

asyncio.run(main())
