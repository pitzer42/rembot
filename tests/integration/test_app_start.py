import pytest

from unittest.mock import MagicMock


@pytest.fixture
def app():
    return MagicMock()


def test_smoke(app):
    assert app.events.on()