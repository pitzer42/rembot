import asyncio
from datetime import datetime
from collections import namedtuple


TICK = 1
ASAP = TICK
MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR
WEEK = 7 * DAY
MONTH = 4 * WEEK

_calendar = list()


class ScheduledFunc:

    def __init__(self, func, exec_datetime, repeat_after):
        self._func = func
        self._exec_datetime = exec_datetime
        self._repeat_after = repeat_after
        self._suspended = False

    def is_on_time(self):
        return self._exec_datetime <= datetime.now()

    async def __call__(self):
        await self._func()
        if self._repeat_after:
            await self._repeat()

    async def _repeat(self):
        while True:
            await asyncio.sleep(self._repeat_after)
            if self._suspended:
                return
            await self._func()

    def suspend(self):
        self._suspended = True


async def attach(events):
    async def exec_calendar():
        while True:
            for scheduled_func in _calendar:
                if scheduled_func.is_on_time():
                    _calendar.remove(scheduled_func)
                    asyncio.create_task(scheduled_func())
            await asyncio.sleep(TICK)

    asyncio.create_task(exec_calendar())


def schedule(func, first_exec, repeat=False):
    entry = ScheduledFunc(func, first_exec, repeat)
    _calendar.append(entry)
    return entry
