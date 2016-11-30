#!/usr/bin/env python

'''
Provides a set of tests that validate access to the application's project drag
and drop functionality.
'''

from tests.base import *

class TestDrop(BaseTest):

    def setUp(self):
        self.drop = Drop()

    def test_drop_xml_project_file_on_assembler_opens_project(self):
        logger.debug(
            self.drop[quote_plus(
                'file:///Users/cary/Desktop/headway/xml/small.xml')])

    def test_drop_zipped_project_file_on_assembler_opens_project(self):
        logger.debug(
            self.drop[quote_plus(
                'file:///Users/cary/Desktop/headway/TestData.zip')])

    def test_drop_project_folder_on_assembler_opens_project(self):
        logger.debug(
            self.drop[quote_plus(
                'file:///Users/cary/Desktop/headway/small.assemblerProject')])

if __name__ == '__main__':
    unittest.main()
