#!/usr/bin/env python3
"""
Accepts a list input_list of floats as argument and
returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Outputs sum of all elements in mxd_lst"""
    return float(sum(mxd_lst))
