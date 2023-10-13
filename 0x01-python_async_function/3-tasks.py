#!/usr/bin/env python3
""" function that takes an integer max_delay and returns a asyncio.Task"""

import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns asyncio task object"""

    wait_random = __Import__('0-basic_async_syntax').wait_random

    Task = asyncio.create_task(wait_random(max_delay))

    return Task
