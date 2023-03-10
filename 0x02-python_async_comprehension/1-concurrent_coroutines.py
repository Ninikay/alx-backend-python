#!/usr/bin/env python3
""" Async Comprehensions module
"""

import asyncio
from typing import Generator


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """ async_comprehension will collect 10 random numbers using an
    async comprehensing over async_generator,
    then return the 10 random numbers.
    """
    result = [i async for i in async_generator()]
    return result
