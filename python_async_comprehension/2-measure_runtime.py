#!/usr/bin/env python3
"""
Coroutine to measure runtime with parallel execution.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure total runtime.

    Returns: total runtime in seconds.
    """
    beginning_of_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_of_time = time.perf_counter()
    total_runtime = end_of_time - beginning_of_time

    return total_runtime
