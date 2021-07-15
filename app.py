import asyncio

from rembot.event_bus import EventBus

from rembot.services import telegram
from rembot.services import scheduler


from rembot.features import reply_telegram_with_rem
from rembot.features import recurrent_telegram_message
from rembot.features import wip_daily_remainder


async def main():

    events = EventBus()

    print('init services')
    await telegram.attach(events)
    await scheduler.attach(events)

    print('attach features')
    await reply_telegram_with_rem.attach(events)
    await recurrent_telegram_message.attach(events)
    await wip_daily_remainder.attach(events)

    print('running...')

    while True:
        await asyncio.sleep(1)

asyncio.run(main())
