#!/usr/bin/env python3

from base_caching import BaseCaching


class BasicCache(BaseCaching):

    def put(self, key, item):
        """
        Assigns dictionary to item value,
        if key or item is none it does nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in dictionary to linked
        key, if key is none or doesnt exist it
        returns nothing.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
