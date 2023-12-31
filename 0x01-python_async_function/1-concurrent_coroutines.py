#!/usr/bin/env python3
"""func with int n&max_delay as args that measures total executn time for"""


import asyncio
import random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """executes wait_random n times"""
    wait_random = __import__('0-basic_async_syntax').wait_random

    delay_list = []
    i = 0

    while i < n:
        delay_list.append(await wait_random(max_delay))
        i += 1

    return sorted(delay_list)
