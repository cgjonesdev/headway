#!/usr/bin/env python

'''
Provides a set of tests that validate role's being changed in the application.
'''

from tests.base import *
from code.api import Roles

class TestRolesChanged(BaseTest):

    def setUp(self, *args, **kwargs):
        self.roles = Roles()

    def test_change_to_admin_role(self):
        '''Testing that role gets changed to Administrator'''
        self.roles.role = 'Administrator'

    def test_change_to_marketer_designer_role(self):
        '''Testing that role gets changed to Marketer/Designer'''
        self.roles.role = quote_plus('Marketer/Designer')

    def test_change_to_designer_role(self):
        '''Testing that role gets changed to Designer'''
        self.roles.role = 'Designer'

    def test_change_to_content_steward_role(self):
        '''Testing that role gets changed to Content Steward'''
        self.roles.role = 'Content Steward'

    def test_change_to_design_steward_role(self):
        '''Testing that role gets changed to Design Steward'''
        self.roles.role = 'Design Steward'

    def test_change_to_asset_librarian_role(self):
        '''Testing that role gets changed to Asset Librarian'''
        self.roles.role = 'Asset Librarian'

    def test_change_to_opar_science_role(self):
        '''Testing that role gets changed to OPAR Science'''
        self.roles.role = 'OPAR Science'

    def test_change_to_translator_role(self):
        '''Testing that role gets changed to Translator'''
        self.roles.role = 'Translator'

if __name__ == '__main__':
    unittest.main()
