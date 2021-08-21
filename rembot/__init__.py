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

        print('enabling services', end='', flush=False)
        init_services = map(lambda s: s.enable(events), services)
        await asyncio.gather(*init_services)
        print('...ok')

        print('starting features', end='', flush=False)
        init_features = map(lambda f: f.start(events), features)
        await asyncio.gather(*init_features)
        print('...ok')

        while True:
            await asyncio.sleep(1)

    asyncio.run(_run())
