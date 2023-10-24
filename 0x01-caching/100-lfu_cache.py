#!/usr/bin/env python3
"""LFUCache module"""

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Cache implementing LFU algorithm
    Cache limit is `BaseCaching.MAX_ITEMS`
    """

    def __init__(self):
        """Initialize a new LRUCache"""

        super(LFUCache, self).__init__()
        self.recently_used = []
        self.frequency = {}

    def _get_least_frequently_used(self):
        """Get the least frequently used items' keys.

        Returns:
            List: List of keys of the least frequently used items.
        """
        least_frequency = min(self.frequency.values())
        lfu_keys = [
            key
            for key, value in self.frequency.items()
            if value == least_frequency
        ]

        return lfu_keys

    def _get_least_recently_used(self, lfu_list):
        """Get the least recently used item's key from a list
        of least frequently used items' keys.

        Args:
            lfu_list (List): List of least frequently used items' keys.

        Returns:
            All: Key of the least recently used item.
        """

        lru_index = max([self.recently_used.index(key) for key in lfu_list])
        lru_key = self.recently_used[lru_index]

        return lru_key

    def _remove_least_frequently_used(self):
        """Remove the least frequently used item from the cache."""

        lfu_keys = self._get_least_frequently_used()

        if len(lfu_keys) == 1:
            removed_key = lfu_keys[0]
        else:
            removed_key = self._get_least_recently_used(lfu_keys)

        self.recently_used.remove(removed_key)
        del self.frequency[removed_key]
        del self.cache_data[removed_key]
        print("DISCARD: {}".format(removed_key))

    def put(self, key, item):
        """Add an item to the cache.
        If the number of items in cache exceeds `BaseCaching.MAX_ITEMS`,
        the least frequently used item is removed from the cache.
        If there are several least frequently used items, then the
        least recently used item in the list is removed.

        Args:
            key (Any): Key of the item to insert.
            item (Any):Value of the item to insert.
        """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self._remove_least_frequently_used()

            if key in self.recently_used:
                # Prevent duplicates.
                self.recently_used.remove(key)

            self.recently_used.insert(0, key)

            if self.frequency.get(key) is not None:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 0

    def get(self, key):
        """Retrieve an item from the cache.
        Updates the `recently_used` list and the `frequency` dictionary
        if the key is valid.

        Args:
            key (Any): Key of the item to retrieve.

        Returns:
            Any: Value of the item if found, else None.
        """
        item = None

        if key:
            item = self.cache_data.get(key)

        if item:
            # Move the key up in the recently_used list as it was
            # accessed recently.
            self.recently_used.remove(key)
            self.recently_used.insert(0, key)
            self.frequency[key] += 1

        return item
