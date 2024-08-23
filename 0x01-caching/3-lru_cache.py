#!/usr/bin/env python
"""LRU Caching"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache class"""
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ remove an item in the cache.
            If key or item is None, do nothing.
            If the cache exceeds the MAX_ITEMS, remove the least recently
              used item.
            if key is already in the cache, update the item and
              move it to the end of the queue.
            if key is not in the cache, add it to the end of the queue.
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                del self.cache_data[self.queue[0]]
                print("DISCARD:", self.queue[0])
                self.queue.pop(0)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get an item by key
            return None if key is not found
            move the key to the end of the queue
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key, None)
