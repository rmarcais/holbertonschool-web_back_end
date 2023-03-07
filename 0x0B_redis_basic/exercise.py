#!/usr/bin/env python3
"""Exercise module"""

import redis
from functools import wraps
from typing import Callable, Optional, Union
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """
    System to count how many times methods
    of the Cache class are called
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Increments the count for the key key
        every time the method method is called
        """
        self._redis.incr(key)
        return method(self, *args)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    System to store the history of inputs and outputs
    for a particular function
    """
    key_input = method.__qualname__ + ":inputs"
    key_ouput = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwrags):
        """
        Add the input parameters in one list and
        the ouputs in another list
        """
        self._redis.rpush(key_input, str(args))
        output = method(self, *args)
        self._redis.rpush(key_ouput, output)
        return output
    return wrapper


def replay(method) -> None:
    """Displays the history of calls of a particular function"""
    local_redis = redis.Redis()

    key_input = method.__qualname__ + ":inputs"
    key_output = method.__qualname__ + ":outputs"

    history_inputs = local_redis.lrange(key_input, 0, -1)
    history_outputs = local_redis.lrange(key_output, 0, -1)

    result = list(zip(history_inputs, history_outputs))

    print("{} was called {} times:".format(method.__qualname__,
                                           len(result)))

    for item in result:
        print("{}(*{}) -> {}".format(method.__qualname__,
                                     item[0].decode(),
                                     item[1].decode()))


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        """Initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and stores the data in Redis"""
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) \
            -> Union[str, bytes, int, float, None]:
        """Redifines the Redis.get() method"""
        value = self._redis.get(key)
        if not value:
            return None

        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """Parametrizes self.get with the correct conversion function"""
        return self.get(key, lambda value: value.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Parametrizes self.get with the correct conversion function"""
        return self.get(key, int)
