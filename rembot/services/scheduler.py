import asyncio

from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler


TIMEZONE = 'America/Sao_Paulo'

_scheduler = None


async def enable(events):
    global _scheduler
    loop = asyncio.get_running_loop()
    _scheduler = AsyncIOScheduler(event_loop=loop)
    _scheduler.start()


def schedule(func, crontab):
    """https://crontab.guru \n minute hour day_month month day_week"""
    global _scheduler
    trigger = CronTrigger.from_crontab(crontab, timezone=TIMEZONE)
    return _scheduler.add_job(func, trigger=trigger)


def suspend(job):
    global _scheduler
    _scheduler.remove_job(job)
