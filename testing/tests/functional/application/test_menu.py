#!/usr/bin/env python

'''
Provides a set of tests that validate access to the application's menu.
'''

from tests.base import *

class TestMenu(BaseTest):

    def setUp(self):
        self.preferences = Menu.Preferences()

    def test_menu_pops_up(self):
        repr(self.preferences)
        repr(Key.Hold.CtrlOpt())
        self.assertEquals(self.preferences('click', CLICK_OK), RETURN_OK)

if __name__ == '__main__':
    unittest.main()
