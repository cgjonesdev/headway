#!/usr/bin/env python

'''
Provides a set of tests that validate access to the application's version
information.
'''

from tests.base import *

class TestQuit(BaseTest):

    def setUp(self):
        self.close_all = CloseAll()
        drop = Drop()
        test_path = os.environ['ASSEMBLER_TESTS']
        drop[quote_plus('file://{}/TestData.zip'.format(test_path))]
        drop[quote_plus('file://{}/TestData.zip'.format(test_path))]

    def test_close_all_closes_all_windows_app(self):
        repr(self.close_all)

    def tearDown(self):
        self.close_all('click', CLICK_OK)

if __name__ == '__main__':
    unittest.main()
