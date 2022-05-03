# -*- coding: utf-8 -*-
import sys
import unittest

from tests.AuthTests import SignUpTest

if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
        unittest.makeSuite(SignUpTest)
        )
    )
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
