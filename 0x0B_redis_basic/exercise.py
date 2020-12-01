#!/usr/bin/env python3
"""Redis Basic"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Any, Optional, List
import sys


def count_calls(method: Callable) -> Callable:
    """Count calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, args):
        k = method(self, args)
        self._redis.incr(key)
        return k

    return wrapper


def call_history(method: Callable) -> Callable:
    """Call History"""
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(input_key, str(args))
        res = method(self, *args)
        self._redis.rpush(output_key, str(res))
        return res
    return wrapper


def replay(method: Callable) -> None:
    """Replay"""
    counter_key = method.__qualname__
    input_key = method.__qualname__ + ':inputs'
    output_key = method.__qualname__ + ':outputs'
    this = method.__self__

    counter = this.get_str(counter_key)
    history = list(zip(this.get_list(input_key),
                       this.get_list(output_key)))
    print("{} was called {} times:".format(counter_key, counter))
    for call in history:
        value = this.get_str(call[0])
        key = this.get_str(call[1])
        print("{}(*{}) -> {}".format(counter_key, value, key))


class Cache:
    """A redis cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store"""
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Get"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_list(self, k: str) -> List:
        """get list"""
        return self._redis.lrange(k, 0, -1)

    def get_str(self, data: bytes) -> str:
        """Convert bytes to str"""
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """Convert bytes to int"""
        return int.from_bytes(data, byteorder)
