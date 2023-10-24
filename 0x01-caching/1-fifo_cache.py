#!/usr/bin/env python3
"""FIFOCache module"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """Cache that implements FIFO algorithm.
    Cache limit is `BaseCaching.MAX_ITEMS`
    """

    def __init__(self):
        """Initialize new FIFOCache"""

        super(FIFOCache, self).__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache.
        If the number of items in cache exceeds `BaseCaching.MAX_ITEMS`,
        the first item to be inserted is removed from the cache.

        Args:
            key (Any): Key of the item to insert.
            item (Any):Value of the item to insert.
        """
        if key and item:
            if key in self.queue:
                # Prevent duplicates.
                self.queue.remove(key)

            self.queue.insert(0, key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed_key = self.queue.pop()
                del self.cache_data[removed_key]
                print("DISCARD: {}".format(removed_key))

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
