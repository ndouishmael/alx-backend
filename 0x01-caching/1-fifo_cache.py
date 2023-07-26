#!/usr/bin/python3
""" FIFOCache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize FIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Get the first item that was put in the cache (FIFO)
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from the cache
        """
        if key is not None:
            return self.cache_data.get(key, None)
        return None
