#!/usr/bin/env python3
"""LIFOCache module"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """Cache that implements LIFO algorithm
    Cache limit is `BaseCaching.MAX_ITEMS`
    """

    def __init__(self):
        """Initialize new LIFOCache"""

        super(LIFOCache, self).__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item to the cache.
        If the number of items in cache exceeds `BaseCaching.MAX_ITEMS`,
        the last item to be inserted is removed from the cache.

        Args:
            key (Any): Key of the item to insert.
            item (Any):Value of the item to insert.
        """
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed_key = self.stack.pop()
                del self.cache_data[removed_key]
                print("DISCARD: {}".format(removed_key))

            if key in self.stack:
                # Prevent duplicates.
                self.stack.remove(key)

            self.stack.append(key)

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key (Any): Key of the item to retrieve.

        Returns:
            Any: Value of the item if found, else None.
        """
        item = None

        if key:
            item = self.cache_data.get(key)

        return item
