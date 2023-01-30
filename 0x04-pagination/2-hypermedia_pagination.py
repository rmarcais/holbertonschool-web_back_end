#!/usr/bin/env python3
"""Task 2. Hypermedia pagination"""

import csv
import math
from typing import Any, Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate page of the dataset
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        range = index_range(page, page_size)
        pages: List[List] = self.dataset()
        return pages[range[0]:range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns a dictionary containing key-value pairs
        """
        dataset = self.dataset()
        data: List[List] = self.get_page(page, page_size)
        next_page = page + 1
        if next_page * page_size > len(dataset):
            next_page = None
        prev_page = page - 1
        if prev_page == 0:
            prev_page = None
        total_pages: int = math.ceil(len(dataset) / page_size)
        if data == []:
            page_size = 0

        params: Dict[str, Any] = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

        return params
