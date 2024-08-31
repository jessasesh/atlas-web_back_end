#!/usr/bin/env python3
"""
Function that creates tuples from a string and a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Tuple that has str for first element and second element
    is the square of the float.

    Args:
        k: str value
        v: int value

    Returns:
        a tuple
    """
    return (k, float(v ** 2))
