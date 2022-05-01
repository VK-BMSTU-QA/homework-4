# -*- coding: utf-8 -*-

import sys
import unittest
from tests.login_test import LoginTest

import unittest
from selenium import webdriver

from tests.main_test import MainPageTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTest),
        unittest.makeSuite(MainPageTest)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
