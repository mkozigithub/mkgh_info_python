import socket
import time


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            time.sleep(1)
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear_cache(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache