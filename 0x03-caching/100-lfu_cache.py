#!/usr/bin/python3
"""LFU caching"""

from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Caching system and Inherits from BaseCaching"""
    def __init__(self):
        self.lru = OrderedDict()
        self.lfu = {}
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key in self.lru:
            del self.lru[key]
        if len(self.lru) > BaseCaching.MAX_ITEMS - 1:
            least = min(self.lfu.values())
            freq = [k for k, v in self.lfu.items() if v == least]
            if len(freq) == 1:
                print("DISCARD:", freq[0])
                self.lru.pop(freq[0])
                del self.lfu[freq[0]]
            else:
                for k, _ in list(self.lru.items()):
                    if k in freq:
                        print("DISCARD:", k)
                        self.lru.pop(k)
                        del self.lfu[k]
                        break
        self.lru[key] = item
        self.lru.move_to_end(key)
        if key in self.lfu:
            self.lfu[key] += 1
        else:
            self.lfu[key] = 1
        self.cache_data = dict(self.lru)

    def get(self, key):
        """return an item from the cache"""
        if key and key in self.cache_data:
            value = self.cache_data[key]
            self.lru.move_to_end(key)
            if key in self.lfu:
                self.lfu[key] += 1
            else:
                self.lfu[key] = 1
            return value
        return None
