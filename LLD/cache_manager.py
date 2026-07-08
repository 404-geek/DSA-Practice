import time
from collections import OrderedDict


class CacheManager:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def put(self, key, value, ttl_seconds):
        self._cleanup_expired_once()

        expiry_time = time.time() + ttl_seconds

        if key in self.cache:
            self.cache[key] = {
                "value": value,
                "expiry": expiry_time
            }
            self.cache.move_to_end(key)
            return

        if len(self.cache) >= self.capacity:
            self._evict_lru()

        self.cache[key] = {
            "value": value,
            "expiry": expiry_time
        }

    def get(self, key):
        if key not in self.cache:
            return None

        item = self.cache[key]

        if time.time() > item["expiry"]:
            self.cache.pop(key)
            return None

        self.cache.move_to_end(key)
        return item["value"]

    def delete(self, key):
        self.cache.pop(key, None)

    def _cleanup_expired_once(self):
        current_time = time.time()

        expired_keys = [
            key for key, item in self.cache.items()
            if current_time > item["expiry"]
        ]

        for key in expired_keys:
            self.cache.pop(key, None)

    def _evict_lru(self):
        self.cache.popitem(last=False)

    def display(self):
        print(list(self.cache.keys()))