#!/usr/bin/env python3
"""Web module"""

from functools import wraps
import redis
import requests
from typing import Callable

local_redis = redis.Redis()


def count_requests(f: Callable) -> Callable:
    """
    System to count how many times methods
    of the Cache class are called
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        """
        Increments the count for the key key
        every time the method method is called
        """
        key_count = "count:{}".format(*args)
        key_cached = "cached:{}".format(*args)

        local_redis.incr(key_count)

        result = f(*args)
        local_redis.setex(key_cached, 10, result)

        return result
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Returns the HTML content of a particular URL"""
    r = requests.get(url)

    return r.text
