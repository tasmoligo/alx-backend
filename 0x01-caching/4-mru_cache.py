#!/usr/bin/python3
"""
LRUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    BaseCaching = __import__('base_caching').BaseCaching
    """

    def __init__(self):
        """ initializer """
        super().__init__()
        self.recentKey = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is None or item is None:
            pass
        else:
            if key not in self.recentKey:
                self.recentKey.append(key)
            else:
                self.recentKey.append(self.recentKey.pop(
                    self.recentKey.index(key)))
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                toBeDeleted_key = self.recentKey.pop(-2)
                del self.cache_data[toBeDeleted_key]
                print('DISCARD: {}'.format(toBeDeleted_key))
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        self.recentKey.append(self.recentKey.pop(
            self.recentKey.index(key)))
        return self.cache_data.get(key)
