#!/usr/bin/env python
'''
Provides base functionality for tests in the suite.
'''

import os
import unittest
from unittest import TestCase
from code.config import TestFilesConfig
from code.logger import logger
from code.api import *

test_files_cfg = TestFilesConfig('{}/configs/assembler.cfg'.format(
                                 os.environ['ASSEMBLER_TESTS']))

class BaseTest(TestCase):
    pass
