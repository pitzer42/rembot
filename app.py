
from rembot import RemBot
from rembot.services import telegram
from rembot.features import reply_telegram_with_rem




import asyncio

async def main():
    app = RemBot()
    await reply_telegram_with_rem.attach(app)
    await telegram.attach(app)

    #app.start()
    print('running...')
    while True:
        await asyncio.sleep(1)

# Python 3.7+
asyncio.run(main())