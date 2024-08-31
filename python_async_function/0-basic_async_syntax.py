#!/usr/bin/env python3
"""
Asynchronous coroutine that takes in an
integer argument that waits for a random
delay and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Async coroutine with delay.

    Args:
        max_delay: maximum delay in seconds.

    Returns:
        float: delay time in seconds.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
