# -*- coding: utf-8 -*-

import sys
import unittest

from tests.login_test import LoginTest
from tests.main_test import MainPageTest
from tests.search_test import SearchPageTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTest),
        unittest.makeSuite(MainPageTest),
        unittest.makeSuite(SearchPageTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
