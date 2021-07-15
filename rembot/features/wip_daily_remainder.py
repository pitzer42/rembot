import os
import asyncio

from datetime import datetime

from rembot.services import scheduler
from rembot.services import telegram
from rembot.services import remnote

WIP_REM = 'WIP'
CHAT_ID = os.environ['CHAT_ID']

HEADER = "Good Morning! 🌞☕\nThis is your work in progress:\n"
ITEM_TEMPLATE = ' • {0}\n'

async def attach(events):

    async def feature():
        items = ''
        tag = await remnote.get_by_name(WIP_REM)
        for tagged_id in tag['tagChildren']:
            tagged_rem = await remnote.get(tagged_id)
            text = tagged_rem['nameAsMarkdown']
            items += ITEM_TEMPLATE.format(text)
        message = HEADER + items
        await telegram.send_message(CHAT_ID, message)
    
    past = datetime.now()
    scheduler.schedule(feature, past, repeat=scheduler.ASAP * 10)
