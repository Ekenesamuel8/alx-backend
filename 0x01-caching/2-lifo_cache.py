#!/usr/bin/env python
"""LIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache class"""
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ remove an item in the cache.
            If key or item is None, do nothing.
            If the cache exceeds the MAX_ITEMS, remove the last added item.
            if key is already in the cache, update the item and
              move it to the end of the queue.
            if key is not in the cache, add it to the end of the queue.
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                del self.cache_data[self.queue[-1]]
                print("DISCARD:", self.queue[-1])
                self.queue.pop(-1)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get an item by key
            return None if key is not found
            move the key to the end of the queue
        """
        return self.cache_data.get(key, None)
