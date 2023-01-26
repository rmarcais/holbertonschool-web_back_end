#!/usr/bin/python3
""" MRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system
    """

    order = []

    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data
        the item value for the key key
        """
        if key is None or item is None:
            return
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                key not in self.cache_data.keys()):
            discard = MRUCache.order[-1]
            print("DISCARD: {}".format(discard))
            self.cache_data.pop(discard)
            MRUCache.order.pop()
        self.cache_data[key] = item
        if key in MRUCache.order:
            MRUCache.order.remove(key)
        MRUCache.order.append(key)

    def get(self, key):
        """Returns the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        if key in MRUCache.order:
            MRUCache.order.remove(key)
        MRUCache.order.append(key)

        return self.cache_data[key]
