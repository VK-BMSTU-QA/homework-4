# -*- coding: utf-8 -*-

import sys
import unittest

from tests.favorites_test import FavoritesTest
from tests.login_test import PositiveLoginTest, NegativeLoginTest

import unittest
from selenium import webdriver

from tests.main_test import MainPageTest
from tests.register_test import NegativeRegisterTest, PositiveRegisterTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(PositiveLoginTest),
        # unittest.makeSuite(NegativeLoginTest),
        # unittest.makeSuite(PositiveRegisterTest),
        # unittest.makeSuite(NegativeRegisterTest),
        # unittest.makeSuite(MainPageTest),
        unittest.makeSuite(FavoritesTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
