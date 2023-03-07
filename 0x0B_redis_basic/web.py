#!/usr/bin/env python3
"""Web module"""

from functools import wraps
import redis
import requests
from typing import Callable
from time import sleep


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
        key = "count:{}".format(*args)
        local_redis = redis.Redis()
        local_redis.incr(key)
        calls = local_redis.get(key)
        if calls:
            return "hello"
        local_redis.expire(key, 10)

        return f(*args)
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Returns the HTML content of a particular URL"""
    r = requests.get(url)

    return r.text
