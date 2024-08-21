#!/usr/bin/env python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a caching system that inherits from BaseCaching.
        This caching system has no limit on the number of items it can store.
    """

    def put(self, key, item):
        """ Add an item in the cache.
            If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key.
            If key is None or if the key doesn’t
              exist in self.cache_data, return None.
        """
        return self.cache_data.get(key, None)
