# -*- coding: utf-8 -*-
import sys
import unittest

from tests.AuthTests import SignUpTest, LoginTest
from tests.MainPageTest import MainPageTest
from tests.BrowseTest import BrowseTest
from tests.PlayerTest import PlayerTest

if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
            # unittest.makeSuite(SignUpTest),
            # unittest.makeSuite(LoginTest)
            unittest.makeSuite(BrowseTest),
            unittest.makeSuite(MainPageTest),
            unittest.makeSuite(PlayerTest)
        )
    )
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
