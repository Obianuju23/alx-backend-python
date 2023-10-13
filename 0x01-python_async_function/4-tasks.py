#!/usr/bin/env python3
"""code from wait_n & alter it into a new function task_wait_n being called"""


import asyncio
import random
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """executes wait_random n times"""
    task_wait_random = __import__('3-tasks').task_wait_random

    delay_list = []
    i = 0

    while i < n:
        delay_list.append(await task_wait_random(max_delay))
        i += 1

    return sorted(delay_list)
