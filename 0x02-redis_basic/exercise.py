#!/usr/bin/env python3
'''
A Cache class that interfaces with redis
'''
import redis
import uuid
from typing import Union


class Cache:
    """Interface class for redis"""
    def __init__(self):
        """class construction"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        key = uuid.uuid4().hex
        self._redis.set(key, data)
        return key
