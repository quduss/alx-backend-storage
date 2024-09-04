#!/usr/bin/env python3
'''
A Cache class that interfaces with redis
'''
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str,
            fn: Union[Callable, None] = None) -> Union[int, str, bytes, float]:
        '''
        Ensures get format is correct
        '''
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        '''
        Ensures get format is correct for strings
        '''
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        '''
        Ensures get format is correct for integers
        '''
        return self.get(key, int)
