#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache is a caching system that inherits from BaseCaching.
        This caching system uses the MRU eviction policy.
    """

    def __init__(self):
        """ Initialize the MRUCache
        """
        super().__init__()
        self.order = []  # List to keep track of the order of keys

    def put(self, key, item):
        """ Add an item in the cache.
            If key or item is None, do nothing.
            If the cache exceeds the MAX_ITEMS, remove
              the most recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                last_key = self.order.pop()  # Remove the last itemInOrderList
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

            self.cache_data[key] = item
            self.order.append(key)  # Add the key to the end of the order list

    def get(self, key):
        """ Get an item by key.
            If key is None or if the key doesn’t exist
              in self.cache_data, return None.
        """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)  # Move key to the end (most recent)
            return self.cache_data[key]
        return None
