#!/usr/bin/env python3
"""Task 2. Run time for four parallel comprehensions"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel,
    measures the total runtime and returns it.
    """
    start: float = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    elapsed: float = time.perf_counter() - start

    return elapsed
