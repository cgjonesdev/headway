#!/usr/bin/env python

'''
Provides an interface to the application's configuration data.
'''

import sys
import os
from ConfigParser import ConfigParser
from pprint import pformat

class BaseConfig(ConfigParser):

    def __str__(self):
        return self.__class__.__name__.replace('Config', '').upper()

    def __repr__(self):
        return '\n{}\n'.format(pformat(list(self)))

    def __init__(self, input_file, *args, **kwargs):
        ConfigParser.__init__(self, *args, **kwargs)
        self.read(input_file)

    def __iter__(self):
        return (dict(self.items(section)) for section in self.sections())

    def __getitem__(self, item):
        return self.get(str(self), item)

class AssemblerConfig(BaseConfig):
    pass

class TestFilesConfig(BaseConfig):
    pass
