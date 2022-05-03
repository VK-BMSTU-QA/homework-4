# -*- coding: utf-8 -*-

import sys
import unittest

from tests.main_test import MainPageTest
from tests.login_test import LoginTest
from tests.register_test import RegisterTest
from tests.favorites_test import FavoritesTest
from tests.profile_test import ProfilePageTest
from tests.search_test import SearchPageTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTest),
        unittest.makeSuite(RegisterTest),
        unittest.makeSuite(MainPageTest),
        unittest.makeSuite(SearchPageTest),
        unittest.makeSuite(ProfilePageTest),
        unittest.makeSuite(FavoritesTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
