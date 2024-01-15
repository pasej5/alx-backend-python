#!/usr/bin/env python3
"""
importing wait_random, an asyn croutine called wait_n
"""

import asyncio
import random


import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> list[float]:
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    
    return sorted(delays)