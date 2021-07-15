import pytest
import inspect
import asyncio

from rembot.services import telegram
from rembot.services import scheduler
from rembot.services import remnote


@pytest.fixture
def services():
    return scheduler, telegram, remnote


def test_service_is_module(services):
    for service in services:
        assert inspect.ismodule(service)


def test_service_has_coroutine_func_enable(services):
    for service in services:
        assert service.enable
        assert asyncio.iscoroutinefunction(service.enable)
