#!/usr/bin/env python

'''
Provides a set of tests that validate access to the application's version
information.
'''

from code.utils import is_open_socket
from tests.base import *

class TestRestart(BaseTest):

    def setUp(self):
        self.restart = Restart()

    def test_restart_closes_app(self):
        repr(self.restart)
        try:
            repr(Version())
        except Exception as e:
            self.assertIn('Connection refused', str(e))

    def test_restart_starts_app(self):
        while not is_open_socket():
            time.sleep(1)
            logger.debug('Waiting for socket to reopen')
        else:
            try:
                repr(Version())
                self.assertNotIn('Connection refused', str(e))
                self.assertEqual(is_open_socket(), 0)                
            except Exception as e:
                logger.error(str(e))

if __name__ == '__main__':
    unittest.main()
