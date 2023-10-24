#!/usr/bin/env python3
"""BasicCache module"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic caching system without a limit.
    Inherits from the BaseCaching class.
    """

    def __init__(self):
        """Initialize a new BasicCache"""

        super(BasicCache, self).__init__()

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key (Any): Key of the item to insert.
            item (Any):Value of the item to insert.
        """
        if key and item:
            self.cache_data[key] = item

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
