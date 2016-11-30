#!/usr/bin/env python

'''
Provides a set of tests that validate file manipulation by the application.
'''

from tests.base import *

class TestFileExistsCheck(BaseTest):

    def test_directory_exists_check(self):
        response = File.Exists()[quote_plus(
            'file://{}'.format(test_files_cfg['CHECK_DIRECTORY_EXISTS_PATH']))]
        self.assertEquals(response, FILE_RETURN_DIRECTORY)

    def test_file_exists_check(self):
        response = File.Exists()[quote_plus(
            'file://{}'.format(test_files_cfg['CHECK_FILE_EXISTS_PATH']))]
        self.assertEquals(response, FILE_RETURN_FILE)

class TestGetFileContents(BaseTest):

    def test_file_contents_not_empty_for_non_empty_file(self):
        pass

    def test_no_content_not_empty_for_empty_file(self):
        pass

class TestGetFileUrl(BaseTest):

    def test_get_url_returns_url(self):
        pass

    def test_get_url_returns_correct_url(self):
        pass

if __name__ == '__main__':
    unittest.main()
