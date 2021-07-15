import asyncio

from rembot.event_bus import EventBus

from rembot.services import telegram
from rembot.services import scheduler
from rembot.services import remnote


from rembot.features import reply_telegram_with_rem
from rembot.features import wip_daily_remainder


async def main():

    events = EventBus()

    print('init services')
    asyncio.create_task(scheduler.enable(events))
    asyncio.create_task(telegram.enable(events))
    asyncio.create_task(remnote.enable(events))

    print('attach features')
    await reply_telegram_with_rem.attach(events)
    await wip_daily_remainder.attach(events)

    print('running...')

    while True:
        await asyncio.sleep(1)

asyncio.run(main())
