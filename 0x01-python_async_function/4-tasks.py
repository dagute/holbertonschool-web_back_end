#!/usr/bin/env python3
"""Tasks"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns the sorted list of delays.
    """
    x = await asyncio.gather(*(task_wait_random(max_delay) for i in range(n)))
    return sorted(x)
