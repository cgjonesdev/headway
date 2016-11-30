#!/usr/bin/env python

'''
Provides a set of tests that validate access to the application's version
information.
'''

from code.utils import is_open_socket
from tests.base import *

class TestQuit(BaseTest):

    def setUp(self):
        self.quit = Quit()

    def test_quit_closes_app(self):
        repr(self.quit)
        try:
            repr(Quit())
        except Exception as e:
            self.assertIn('Connection refused', str(e))
            self.assertNotEqual(is_open_socket(), 0)

    def tearDown(self):
        os.system('"{}/Assembler" &'.format(cfg['PATH']))

if __name__ == '__main__':
    unittest.main()
