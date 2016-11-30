#!/usr/bin/env python

'''
Provides a set of tests that validate role's being changed in the application.
'''

from tests.base import *

class TestPrtReport(BaseTest):

	def setUp(self):
		self.open_project_menu = Menu.OpenProject()

	def test_report_is_generated(self):
		self.open_project_menu[quote_plus(
			'file:///Users/cary/Desktop/headway/xml/small.xml')]

if __name__ == '__main__':
    unittest.main()
