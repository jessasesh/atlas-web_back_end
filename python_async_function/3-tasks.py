#!/usr/bin/env python3
"""
Module that creates asyncio task.
"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates asyncio task that runs wait_random.

    Args:
        max_delay: maximum delay in seconds

    Returns: asyncio task
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
