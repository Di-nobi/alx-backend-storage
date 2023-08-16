#!/usr/bin/env python3
""""""
import redis
from typing import Union, List, Callable, Optional
import uuid
def count_calls(method: Callable) -> Callable:

class Cache():
    """Initialization of the instance for redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Creates a get method that take a key string argument and an optional Callable argument named fn"""
        num = self._redis.get(key)
        if fn:
            num = fn(num)
        return num
    def get_str(self, key: str) -> str:
        """Automatically parametrize Cache.get with the correct conversion function"""
        return str(self._redis.get(key).decode("utf-8"))
    def get_int(self, key: str) -> int:
        """Automatically parametrize Cache.get with the correct conversion function"""
        return int(self._redis.get(key).decode("utf-8"))