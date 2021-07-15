import asyncio

from datetime import datetime
from collections import namedtuple


_TICK = 60
_calendar = list()


class ScheduledFunc:

    def __init__(self, func, scheduled_datetime=None, minute=None, hour=None, day=None, month=None, weekday=None):
        self._func = func
        self._suspended = False
        if scheduled_datetime:
            self.minute = scheduled_datetime.minute
            self.hour = scheduled_datetime.hour
            self.day = scheduled_datetime.day
            self.month = scheduled_datetime.month
            self.weekday = scheduled_datetime.weekday
        else:
            self.minute = minute
            self.hour = hour
            self.day = day
            self.month = month
            self.weekday = weekday

    def on_time(self, now):
        return (not self._suspended) and not(
            (self.minute and self.minute != now.minute) or
            (self.hour and self.hour != now.hour) or
            (self.day and self.day != now.day) or
            (self.month and self.month != now.month) or
            (self.weekday and self.weekday != now.weekday))

    def suspend(self):
        self._suspended = True


async def enable(events):
    while True:
        for entry in _calendar:
            if entry._suspended:
                _calendar.remove(entry)
                continue
            now = datetime.utcnow()
            if entry.on_time(now):
                asyncio.create_task(entry._func())
        await asyncio.sleep(_TICK)


def schedule(entry):
    _calendar.append(entry)


def suspend(entry):
    entry.suspend()
