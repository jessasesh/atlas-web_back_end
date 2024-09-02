#!/usr/bin/env python3
"""
Async routine that takes in two
int arguments in specific order.
"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawn wait_random, n times with specified
    max_delay.

    Args:
        n: number of times to spawn wait_random
        max_delay: max delay for wait_random

    Returns: List of all delays in ascending order.
    """
    delay_list: List[float] = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delay_list.append(delay)

    return delay_list
