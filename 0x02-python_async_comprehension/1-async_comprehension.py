#!/usr/bin/env python3
"""
Async Comprehensions
mandatory
Import async_generator from the previous task and then write
a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random
numbers.
"""

import asyncio
import importlib
from typing import List


async_generator_module = importlib.import_module('0-async_generator.py')
async_generator = async_generator_module.async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async
    comprehensions over async_generator.
    """
    result = [number async for number in async_generator]
    return result
