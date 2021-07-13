import os

KEY = 'ENV'


class Service:
    
    def get(key):
        return os.getenv(key)