#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache is a caching system that inherits from BaseCaching.
        This caching system uses the FIFO eviction policy.
    """

    def __init__(self):
        """ Initialize the FIFOCache
        """
        super().__init__()
        self.order = []  # List to keep track of the order of keys

    def put(self, key, item):
        """ Add an item in the cache.
            If key or item is None, do nothing.
            If the cache exceeds the MAX_ITEMS, remove the first added item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key.
            If key is None or if the key doesn’t
              exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
