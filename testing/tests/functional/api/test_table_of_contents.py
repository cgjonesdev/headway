#!/usr/bin/env python

'''
Provides a set of tests that validate access to the Table of Contents in the
application.
'''

from tests.base import *

class TestTableOfContents(BaseTest):

    def setUp(self):
        self.toc = Toc()

    def test_contents_not_empty(self):
        self.assertNotEqual(repr(self.toc), '')

    def test_recursive(self):
    	self.toc('1')

if __name__ == '__main__':
    unittest.main()
