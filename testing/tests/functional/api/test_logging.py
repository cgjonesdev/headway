#!/usr/bin/env python

'''
Provides a set of tests that validate access to the application's logging system.
'''

from tests.base import *

class TestGetLogs(BaseTest):

    def setUp(self):
        repr(Logs.Clear())
        self.logs = Logs.Get()

    def test_contents_not_empty(self):
        Logs.Message().note = 'NOTE'.ljust(7) + ': Test note message'
        self.assertNotEquals(repr(self.logs), '')

class TestLogMessages(BaseTest):

    def setUp(self):
        self.message = Logs.Message()

    def test_error_log_is_created(self):
        Logs.Message().note = 'ERROR'.ljust(7) + ': Test error message'
        self.error = 'ERROR'.ljust(7) + 'Test message'

    def test_warning_log_is_created(self):
        Logs.Message().note = 'WARNING'.ljust(7) + ': Test warning message'
        self.warning = 'WARNING'.ljust(7) + 'Test warning message'

    def test_trace_log_is_created(self):
        Logs.Message().note = 'TRACE'.ljust(7) + ': Test trace message'
        self.trace = 'TRACE'.ljust(7) + 'Test trace message'

    def test_note_log_is_created(self):
        self.note = 'NOTE'.ljust(7) + 'Test note message'

    def tearDown(self):
        logger.info('\n' + repr(Logs.Get()))

if __name__ == '__main__':
    unittest.main()
