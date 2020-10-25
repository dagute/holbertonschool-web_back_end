#!/usr/bin/env python3
"""MRU Caching"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Caching system and Inherits from BaseCaching"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.current_keys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item
            if key not in self.current_keys:
                self.current_keys.append(key)
            else:
                self.current_keys.append(self.current_keys.pop(
                    self.current_keys.index(key)))
            if len(self.current_keys) > BaseCaching.MAX_ITEMS:
                least_key = self.current_keys.pop(-2)
                del self.cache_data[least_key]
                print('DISCARD: {}'.format(least_key))

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key and key in self.cache_data:
            self.current_keys.append(self.current_keys.pop(
                self.current_keys.index(key)))
            return self.cache_data.get(key)
        return None
