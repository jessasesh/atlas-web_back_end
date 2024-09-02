#!/usr/bin/env python3
"""
Module to measure the runtime of the wait_n function.
"""

import asyncio
import time
from typing import List

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures total execution time
    Args:
        n: number of times to spawn wait_random
        max_delay: max delay for wait_random

    Returns: Execution time
    """
    beginning_of_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_of_time = time.perf_counter()
    total_time = end_of_time - beginning_of_time

    return total_time / n
