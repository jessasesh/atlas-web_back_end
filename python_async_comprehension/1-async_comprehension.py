#!/usr/bin/env python3
"""
Coroutine that collects 10 random numbers from async_generator.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator.

    Returns: list of 10 random numbers
    """
    return [number async for number in async_generator()]
