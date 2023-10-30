#!/usr/bin/env python3
"""Implementation of a function that uses the reuests module to obtain the HTML content of a URL"""
import redis
import requests
def get_page(url: str) -> str:
    """Implementation of a function that uses the reuests module to obtain the HTML content of a URL"""
    coun = redis.Redis()
    key = f"visited:{url}"
    coun.set(key, 0)
    response = requests.get(url).text
    counter = f"count:{url}"
    coun.incr(counter)
    coun.setex(key, 10, coun.get(key))
    return response