#!/usr/bin/env python3
"""
Coroutine that generates random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that asynchronously generates numbers
    with delay.

    Yields: random number between 0-10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
