#!/usr/bin/env python3
"""Task 8. Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier
    """
    def f(second_multiplier: float) -> float:
        """The returned function"""
        return multiplier * second_multiplier
    return f
