#!/usr/bin/env python3
"""
Using Redis for simple cache and
basic operations
"""
import redis
import uuid
from typing import Union


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
