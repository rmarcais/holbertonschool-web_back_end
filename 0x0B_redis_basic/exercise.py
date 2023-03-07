#!/usr/bin/env python3
"""Exercise module"""

import redis
from typing import Callable, Optional, Union
from uuid import uuid4


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        """Initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and stores the data in Redis"""
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(self,
            key: str,
            fn: Optional[Callable]) -> Union[str, bytes, int]:
        """Redifines the Redis.get() method"""
        value = self._redis.get(key)
        if not value:
            return None

        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """Returns data as a string"""
        return self.get(key, lambda value: value.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Returns data as an integer"""
        return self.get(key, int)
