#!/usr/bin/env python3
"""func to_kv that takes str k and an int/float v as arg & returns a tuple"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple consisting of k and the square of v"""
    return (k, v * v)
