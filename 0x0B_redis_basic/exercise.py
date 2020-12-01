#!/usr/bin/env python3
"""Redis Basic"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Any, Optional


def count_calls(method: Callable) -> Callable:
    """Count calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, args):
        """Wrapper function"""
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
        """Wrapper function"""
        self._redis.rpush(input_key, str(args))
        res = method(self, *args)
        self._redis.rpush(output_key, str(res))
        return res
    return wrapper


def replay(method: Callable):
    """Replay function"""
    c = redis.Redis()
    storage = method.__qualname__
    aux = c.get(storage).decode('utf-8')
    inputs = c.lrange(storage + ':inputs', 0, -1)
    outputs = c.lrange(storage + ':outputs', 0, -1)
    print("{} was called {} times:".format(storage, aux))
    for i, o in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(storage, i.decode("utf-8"),
                                     o.decode("utf-8")))


class Cache:
    """A redis cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """take a key string argument """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, data: str) -> str:
        """Convert bytes to str"""
        return self._redis.get(data).decode('utf-8')

    def get_int(self, data: str) -> int:
        """Convert bytes to int"""
        return int(self._redis.get(data))
