#!/usr/bin/env python3
"""
Asyncronous that takes an integeras an argument
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that generates a random delay between
        0 and max_delay seconds.

    Args:
        max_delay (int, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The generated random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
