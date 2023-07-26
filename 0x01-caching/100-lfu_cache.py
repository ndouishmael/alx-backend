#!/usr/bin/python3
""" LFUCache module"""
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize LFUCache
        """
        super().__init__()
        self.frequency = defaultdict(int)  # To track the frequency of item usage
        self.freq_items = defaultdict(list)  # To track items with the same frequency
        self.min_frequency = 0  # To track the minimum frequency of items

    def put(self, key, item):
        """ Add an item in the cache using LFU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item  # Update the item value
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    # Get the least frequency used item (LFU)
                    while not self.freq_items[self.min_frequency]:
                        self.min_frequency += 1
                    lfu_key = self.freq_items[self.min_frequency].pop(0)
                    print(f"DISCARD: {lfu_key}")
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]

                self.cache_data[key] = item
                self.frequency[key] = 0
                self.min_frequency = 0

            self.frequency[key] += 1
            self.freq_items[self.frequency[key]].append(key)

    def get(self, key):
        """ Get an item by key from the cache
        """
        if key is not None and key in self.cache_data:
            # Update the frequency and re-sort the items based on frequency
            self.frequency[key] += 1
            self.freq_items[self.frequency[key]].append(self.freq_items[self.frequency[key]].pop(0))

            return self.cache_data[key]
        return None
