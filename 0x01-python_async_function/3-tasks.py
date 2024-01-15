#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function,
use the regular function syntax to do this)
task_wait_random that takes an integer max_delay
and returns a asyncio.Task.
"""

import asyncio
import importlib

wait_random_module = importlib.import_module('0-basic_async_syntax')
wait_random = wait_random_module.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random.

    """
    return asyncio.create_task(wait_random(max_delay))
