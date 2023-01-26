#!/usr/bin/python3
""" FIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data
        the item value for the key key
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = list(self.cache_data.keys())[0]
                print("Discard: {}".format(discard))
                self.cache_data.pop(discard)

    def get(self, key):
        """Returns the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
