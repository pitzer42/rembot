class EventBus:

    def __init__(self):
        self._events = dict()
    
    def on(self, event, action):
        print(event)
        if event not in self._events:
            self._events[event] = set()
        self._events[event].add(action)

    async def notify(self, event):
        event_type = type(event)
        print(event_type)
        print(self._events)
        if event_type not in self._events:
            return
        for action in self._events[event_type]:
            await action(event)


class ServiceLocator:

    def __init__(self):
        self._services = dict()

    def register(self, key, obj):
        self._services[key] = obj

    def get(self, key):
        return self._services[key]
    
    def start(self):
        for service in self._services.values():
            service.start(self)



class RemBot():

    def __init__(self):
        self.services = ServiceLocator()
        self.events = EventBus()
    
    def start(self):
        self.services.start()