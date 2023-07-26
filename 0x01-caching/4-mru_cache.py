#!/usr/bin/python3
""" MRUCache module"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        self.order = []  # To track the order of item usage

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)  # Remove the key from the order list
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # Get the most recently used key from the end of the order list
                mru_key = self.order.pop()
                print(f"DISCARD: {mru_key}")
                del self.cache_data[mru_key]

            self.cache_data[key] = item
            self.order.append(key)  # Append the key to the end of the order list

    def get(self, key):
        """ Get an item by key from the cache
        """
        if key is not None and key in self.cache_data:
            # Move the key to the end of the order list to indicate it was recently used
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
