#!/usr/bin/env python3
"""Exercise module"""

import redis
from typing import Any
from uuid import uuid4


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        """Initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """Generates a random key and stores the data in Redis"""
        key = str(uuid4())
        self._redis.set(key, data)

        return key
