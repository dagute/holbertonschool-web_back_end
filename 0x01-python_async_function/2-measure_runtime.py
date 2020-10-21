#!/usr/bin/env python3
""" Measure the runtime"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time"""
    s_t = time.time()
    asyncio.run(wait_n(n, max_delay))
    t_t = time.time() - s_t
    return t_t / n
