# -*- coding: utf-8 -*-
import sys
import unittest

from tests.AuthTests import SignUpTest, LoginTest

if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
            unittest.makeSuite(SignUpTest),
            unittest.makeSuite(LoginTest)
        )
    )
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
