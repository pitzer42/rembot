import pytest

from datetime import datetime
from rembot.services.scheduler import ScheduledFunc


@pytest.fixture
def now():
    return datetime.utcnow()


def test_all_properties_defined_on_all_equal(now):
    scheduled = ScheduledFunc(None, scheduled_datetime=now)
    assert scheduled.on_time(now)


def test_suspended_all_properties_defined_on_all_equal(now):
    scheduled = ScheduledFunc(None, scheduled_datetime=now)
    scheduled.suspend()
    assert not scheduled.on_time(now)


def test_all_properties_defined_on_different_minute(now):
    other_minute = 59 - now.minute
    other = now.replace(minute=other_minute)
    scheduled = ScheduledFunc(None, scheduled_datetime=other)
    assert not scheduled.on_time(now)


def test_only_minute_defined_on_same_minute(now):
    scheduled = ScheduledFunc(None, minute=30)
    now = now.replace(minute=scheduled.minute)
    assert scheduled.on_time(now)


def test_suspended_only_minute_defined_on_same_minute(now):
    scheduled = ScheduledFunc(None, minute=30)
    scheduled.suspend()
    now = now.replace(minute=scheduled.minute)
    assert not scheduled.on_time(now)


def test_only_minute_defined_on_different_minute(now):
    scheduled = ScheduledFunc(None, minute=30)
    other_minute = 59 - now.minute
    now = now.replace(minute=other_minute)
    assert not scheduled.on_time(now)


def test_no_properties_defined_on_any(now):
    scheduled = ScheduledFunc(None)
    assert scheduled.on_time(now)


def test_suspended_no_properties_defined_on_any(now):
    scheduled = ScheduledFunc(None)
    scheduled.suspend()
    assert not scheduled.on_time(now)
