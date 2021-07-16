import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

_scheduler = AsyncIOScheduler()


async def enable(events):
    _scheduler.start()


def schedule(func, crontab):
    """ https://crontab.guru \n minute hour day_month month day_week"""
    trigger = CronTrigger.from_crontab(crontab)
    return _scheduler.add_job(func, trigger)


def suspend(job):
    _scheduler.remove_job(job)
