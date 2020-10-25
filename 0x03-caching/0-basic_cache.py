#!/usr/bin/python3
""" Basic Cache module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ inherits from BaseCaching and is a caching system"""
    def put(self, key, item):
        """ Add an item value for the key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value linked to the key"""
        return self.cache_data.get(key, None)
