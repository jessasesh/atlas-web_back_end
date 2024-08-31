#!/usr/bin/env python3
"""
Fucntion that returns a list of tuples.
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    List of tuples that each contain an element
    of the input list and its length.

    Args:
        lst: list of sequences.

    Returns:
        List: a list of tuples where each one contains a
        sequence and its length.
    """
    return [(i, len(i)) for i in lst]
