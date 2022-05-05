# -*- coding: utf-8 -*-
import sys
import unittest
from page_objects.login import LoginPage
from tests.level_edit.add_level_test import AddLevelTest
from tests.level_edit.edit_level_test import EditLevelTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginPage),
        unittest.makeSuite(AddLevelTest),
        # unittest.makeSuite(EditLevelTest)))
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
