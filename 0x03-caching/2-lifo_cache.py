#!/usr/bin/python3
"""LIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Caching system and Inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.pop_out = ''

    def put(self, key, item):
        """ Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.pop_out))
                self.cache_data.pop(self.pop_out)
            self.pop_out = key

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        return self.cache_data.get(key, None)
