import os
import asyncio

from datetime import timedelta
from datetime import datetime

from rembot.services import scheduler
from rembot.services import telegram
from rembot.services import remnote
from rembot.services.scheduler import ScheduledFunc

REMAIND_TAG = 'WIP'
HEADER = "Good Morning! 🌞☕\nThis is your work in progress:\n"
BULLET_TEMPLATE = ' • {0}'
UTC_HOUR=9


async def attach(events):

    async def bullet_list_for_tagged_rems(tag_name):
        children = list()
        tag = await remnote.get_by_name(REMAIND_TAG)
        for child in tag['tagChildren']:
            child = await remnote.get(child)
            child = child['nameAsMarkdown']
            child = BULLET_TEMPLATE.format(child)
            children.append(child)
        return '\n'.join(children)

    async def send_rems_tagged_to_remaind():
        bullet_list = await bullet_list_for_tagged_rems(REMAIND_TAG)
        message = HEADER + bullet_list
        await telegram.send_message(message)

    entry = ScheduledFunc(send_rems_tagged_to_remaind, hour=UTC_HOUR)
    scheduler.schedule(entry)
