import pytest

from rembot import RemBot


@pytest.fixture
def rembot():
    return RemBot()


def test_set_and_retrieve_service(rembot):
    key = int
    obj = 1
    rembot.set_service(key, obj)
    assert rembot.get_service(key) == obj


def test_a_service_is_registred_under_a_unique_key(rembot):
    key = int
    obj_a = 1
    obj_b = 2
    rembot.set_service(key, obj_a)
    rembot.set_service(key, obj_b)
    assert rembot.get_service(key) == obj_b
