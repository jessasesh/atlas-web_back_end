#!/usr/bin/python3
"""
MRU caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    def __init__(self):
        """
        Initialize the MRUCache instance.

        Inherits from BaseCaching and initializes the cache_data dictionary.
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Add or update an item in the cache.

        If the cache is full, remove the most recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.usage_order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieves an item from the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
