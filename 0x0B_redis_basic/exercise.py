#!/usr/bin/env python3
"""
Using Redis for simple cache and
basic operations
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method
    is called using Redis
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)

        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and
    outputs for a method
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


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

    @count_calls
    @call_history
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


def replay(method: Callable):
    """
    Display history of calls for a specific method
    """
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    self = method.__self__
    redis_client = self._redis

    inputs = redis_client.lrange(input_key, 0, -1)
    outputs = redis_client.lrange(output_key, 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times: ")

    for input_data, output_data in zip(inputs, outputs):
        f_input = input_data.decode('utf-8')
        f_output = output_data.decode('utf-8')
        print(f"{method.__qualname__}(*{f_input}) -> {f_output}")
