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