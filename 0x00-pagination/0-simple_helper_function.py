#!/usr/bin/env python3
"""index_page module"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Find start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.

    Args:
        page (int): Page number.
        page_size (int): Number of items in a page.

    Returns:
        Tuple[int, int]: tuple of the start and end indexes.
    """
    start = page_size * (page - 1)
    end = page_size * page

    return start, end
