#!/usr/bin/env python3
"""Task 1. Let's execute multiple coroutines at the same time with async"""

import asyncio
from typing import Any, Awaitable, Callable, List

wait_random: Callable[[int], float]
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that takes in 2 int arguments: n and max_delay
    """

    result: List[float] = []

    tasks: List[Awaitable[Any]] = []

    for i in range(n):
        task: Awaitable[Any] = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        result.append(await task)

    return result
