#!/usr/bin/env python3
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRU caching system
    """
    def __init__(self):
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Add or updates an item in cache; if cache
        is full, remove least recently used item.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.usage_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieves item from cache.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
