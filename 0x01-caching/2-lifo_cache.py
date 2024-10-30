#!/usr/bin/python3
"""
FIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    BaseCaching = __import__('base_caching').BaseCaching
    """

    def __init__(self):
        """ initializer """
        super().__init__()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                toBeDeleted_key, toBeDeleted_value = self.cache_data.popitem()
                print('DISCARD: {}'.format(toBeDeleted_key))
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
