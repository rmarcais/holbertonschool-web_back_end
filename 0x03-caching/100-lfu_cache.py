#!/usr/bin/python3
""" LFUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system
    """

    order = []
    frequencies = {}

    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data
        the item value for the key key
        """
        if key is None and item is None:
            return
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                key not in self.cache_data.keys()):
            discard = [k for k, v in LFUCache.frequencies.items()
                       if v == min(LFUCache.frequencies.values())]
            if len(discard) > 1:
                for i in LFUCache.order:
                    if i in discard:
                        discard = i
                        index = LFUCache.order.index(i)
                        break
            else:
                discard = discard[0]
                index = LFUCache.order.index(discard)
            print("DISCARD: {}".format(discard))
            self.cache_data.pop(discard)
            LFUCache.order.pop(index)
            #LFUCache.frequencies.pop(discard)
        self.cache_data[key] = item
        if key not in LFUCache.frequencies.keys():
            LFUCache.frequencies[key] = 0
        if key in LFUCache.order:
            LFUCache.order.remove(key)
        LFUCache.order.append(key)
        LFUCache.frequencies[key] += 1

    def get(self, key):
        """Returns the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        if key in LFUCache.order:
            LFUCache.order.remove(key)
        LFUCache.order.append(key)
        LFUCache.frequencies[key] += 1

        return self.cache_data[key]
