#!/usr/bin/env python3
"""Task 0. Simple helper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size

    return (start, end)
