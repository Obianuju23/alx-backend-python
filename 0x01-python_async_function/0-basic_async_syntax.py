#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument max_delay"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function that waits for random delay and returns the max_delay"""
    wait_time = max_delay * random.random()
    await asyncio.sleep(wait_time)
    return wait_time
