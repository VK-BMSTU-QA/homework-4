# -*- coding: utf-8 -*-
import sys
import unittest

from tests.AuthTests import SignUpTest, LoginTest
from tests.ProfileTest import ProfileTest

if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
            unittest.makeSuite(SignUpTest),
            unittest.makeSuite(LoginTest),
            unittest.makeSuite(ProfileTest),
        )
    )
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
