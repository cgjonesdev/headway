#!/usr/bin/env python

'''
Provides a set of meta classes that can be used to enhance object creation.
'''

class RequestMeta(type):

    def __new__(cls, name, bases, data):
        return type.__new__(cls, name, bases, data)
