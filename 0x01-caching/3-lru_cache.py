#!/usr/bin/env python3
"""LRUCache module"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """Cache implementing LRU algorithm
    Cache limit is `BaseCaching.MAX_ITEMS`
    """

    def __init__(self):
        """Initialize a new LRUCache"""

        super(LRUCache, self).__init__()
        self.recently_used = []

    def put(self, key, item):
        """Add an item to the cache.
        If the number of items in cache exceeds `BaseCaching.MAX_ITEMS`,
        the least recently used item is removed from the cache.

        Args:
            key (Any): Key of the item to insert.
            item (Any):Value of the item to insert.
        """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed_key = self.recently_used.pop()
                del self.cache_data[removed_key]
                print("DISCARD: {}".format(removed_key))

            if key in self.recently_used:
                # Prevent duplicates.
                self.recently_used.remove(key)

            self.recently_used.insert(0, key)

    def get(self, key):
        """Retrieve an item from the cache.
        Updates the `recently_used` list if the key is valid.

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

        return item
