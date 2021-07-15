import asyncio

from collections import namedtuple


def consts(**kwargs):
    """ factory function for creating namedtuple from dict """
    return namedtuple(
        'consts',
        list(kwargs.keys()),
        defaults=list(kwargs.values()))()


class EventBus:

    def __init__(self):
        self._events = dict()

    def on(self, event, action):
        if event not in self._events:
            self._events[event] = set()
        self._events[event].add(action)

    async def notify(self, event):
        event_type = type(event)
        if event_type not in self._events:
            return
        for action in self._events[event_type]:
            await action(event)


def run(services, features):

    async def _run():
        events = EventBus()

        print('enabling services', end='')
        for service in services:
            asyncio.create_task(service.enable(events))
            print('.', end='')
        print('ok')

        print('attaching features', end='')
        for feature in features:
            await feature.attach(events)
            print('.', end='')
        print('ok')

        print('running...')
        while True:
            await asyncio.sleep(1)

    asyncio.run(_run())
