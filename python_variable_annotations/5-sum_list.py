#!/usr/bin/env python3
"""
Function which takes a list of floats as argument
and returns their sum as a float.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum of lists.

    Args:
        input_list: list of floats to add.

    Returns:
        float: sum of floats in the list.
    """
    return sum(input_list)
