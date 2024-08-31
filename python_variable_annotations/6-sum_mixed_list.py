#!/usr/bin/env python3
"""
Function which takes a list of integers and
floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum of a list containing integers and floats.

    Args:
        mxd_lst: list of integers and floats.

    Returns:
        Sum of values in the list as a float.
    """
    return sum(mxd_lst)
