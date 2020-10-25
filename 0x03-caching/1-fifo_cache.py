#!/usr/bin/python3
"""FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Caching system and Inherits from BaseCaching"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.data = {}
        self.push_in, self.pop_out = 0, 0

    def put(self, key, item):
        """ Add an item in the cache"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self.pushin(key, item)

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        return self.cache_data.get(key, None)

    def popout(self):
        """ leave the list"""
        self.pop_out += 1
        key = self.data[self.pop_out]
        del self.data[self.pop_out], self.cache_data[key]

    def pushin(self, key, item):
        """ attach to a list"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.pop_out + 1]))
            self.popout()
        self.cache_data[key] = item
        self.push_in += 1
        self.data[self.push_in] = key
