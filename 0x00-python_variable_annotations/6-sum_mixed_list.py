#!/usr/bin/env python3
"""Task 6. Complex types - mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Takes a list mcd_list of integers and floats and
    returns their sum as a float
    """
    return sum(mxd_list)
