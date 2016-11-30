#!/usr/bin/env python

'''
Provides a set of decorators that can be used to wrap functionality.
'''

from functools import wraps

def query(query):
    def decorator(func):
        @wraps(func)
        def wrapper(obj):
            obj.resource += '/' + query
            return func(obj)
        return wrapper
    return decorator
