#!/usr/bin/env python3
"""function with int n&max_delay as args that measures total execution time"""


import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """Executes tpotal execution time"""
    wait_n = __import__('1-concurrent_coroutines').wait_n

    start_time = time.time()
    run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n
