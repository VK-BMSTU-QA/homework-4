# -*- coding: utf-8 -*-

import sys
import unittest
from tests.login_test import LoginTest

import unittest
from selenium import webdriver

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
