#!/usr/bin/env python3
"""The basics of async"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ waits for a random delay between 0 and max_delay"""
    random_num = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num
