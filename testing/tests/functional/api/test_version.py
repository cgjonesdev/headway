#!/usr/bin/env python

'''
Provides a set of tests that validate access to the application's version
information.
'''

from tests.base import *

class TestVersion(BaseTest):

    def setUp(self):
        self.version = repr(Version())

    def test_contents_not_empty(self):
        logger.debug('\n\n' + '\n'.join(unquote_plus(self.version).split(',')))
        self.assertNotEqual(self.version, '')

if __name__ == '__main__':
    unittest.main()
