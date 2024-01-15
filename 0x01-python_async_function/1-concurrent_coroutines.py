#!/usr/bin/env python3
"""
importing wait_random, an asyn croutine called wait_n
"""

import asyncio
from typing import List
import importlib

wait_random_module = importlib.import_module('0-basic_async_syntax')
wait_random = wait_random_module.wait_random

async def task_wait_random(max_delay: int) -> float:
    """
    Asynchronous function that returns an asyncio task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))

async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times with the
    specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        List[float]: A list of delays (float values) in ascending order.
    """
    delays = await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))

    return sorted(delays)
