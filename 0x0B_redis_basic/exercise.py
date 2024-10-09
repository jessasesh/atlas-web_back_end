#!/usr/bin/env python3
"""
Using Redis for simple cache and
basic operations
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Methods to store data in Redis db
    """
    def __init__(self) -> None:
        """
        Creates Redis client and flushes db
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data and returns uuid for that data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """
        Retrieve the value from Redis and converts data
        back to the desired format
        """
        value = self.client.get(key)

        if value is None:
            return None

        if fn:
            return fn(value)

        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Get the value and decode it
        """
        value = self.get(key)
        if value is not None:
            return value.decode('utf-8')
        return None

    def get_int(self, key: str) -> Optional[int]:
        """
        Get the value and convert it to an integer
        """
        value = self.get(key)
        if value is not None:
            try:
                return int(value)
            except ValueError:
                return None
        return None
