#!/usr/bin/python3
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFO caching system
    """

    def __init__(self):
        """ Initialize the class with parent class attributes """
        super().__init__()
        self.order = []  # List to keep track of insertion order

    def put(self, key, item):
        if key is None or item is None:
            return

        
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

            self.cache_data[key] = item
            self.order.append(key)


    def get(self, key):
        return self.cache_data.get(key, None)
