# -*- coding: utf-8 -*-
import sys
import unittest
from page_objects.login import LoginPage

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginPage)))
    result = unittest.TextTest().run(suite)
    sys.exit(not result.wasSuccessful())