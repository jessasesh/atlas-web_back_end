#!/usr/bin/python3
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFO caching system
    """

    def __init__(self):
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Adds or updates an item in cache; if cache
        is full, last added item is removed.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.last_key is not None:
                    print(f"DISCARD: {self.last_key}")
                    del self.cache_data[self.last_key]

            self.cache_data[key] = item
            self.last_key = key


    def get(self, key):
        """
        Retrieves an item from cache.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
