#!/usr/bin/env python3
""""""
import redis
from typing import Union, List
import uuid

class Cache():
    """Initialization of the instance for redis"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key