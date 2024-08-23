#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache is a caching system that inherits from BaseCaching.
        This caching system uses the LFU (Least Frequently Used)
          eviction policy,
        with LRU (Least Recently Used) as a tiebreaker.
    """

    def __init__(self):
        """ Initialize the LFUCache
        """
        super().__init__()
        self.usage_frequency = {}  # Dictionary to store theFrequencyOfUsageOfKeys
        self.usage_order = []  # List to store the order of usage of keys

    def put(self, key, item):
        """ Add an item in the cache.
            If key or item is None, do nothing.
            If the cache exceeds the MAX_ITEMS, remove the least
              frequently used item,
            and if there's a tie, remove the least recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.usage_order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # Find the least frequently used key(s)
                min_freq = min(self.usage_frequency.values())
                least_frequent_keys = [k for k, v in self.usage_frequency.items() if v == min_freq]
                
                # If there's a tie, use LRU to evict the least recently used among them
                if len(least_frequent_keys) > 1:
                    for k in self.usage_order:
                        if k in least_frequent_keys:
                            lfu_key = k
                            break
                else:
                    lfu_key = least_frequent_keys[0]

                # Remove the LFU key from cache
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                self.usage_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Add the item to the cache and update frequency and order
            self.cache_data[key] = item
            self.usage_frequency[key] = self.usage_frequency.get(key, 0) + 1
            self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key.
            If key is None or if the key doesn’t exist in self.cache_data, return None.
            Otherwise, update the frequency and order, and return the value.
        """
        if key is not None and key in self.cache_data:
            self.usage_frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
