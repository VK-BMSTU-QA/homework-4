# -*- coding: utf-8 -*-
import sys
import unittest

from tests.AuthTests import SignUpTest, LoginTest
from tests.ProfileTest import ProfileTest
from tests.MainPageTest import MainPageTest
from tests.BrowseTest import BrowseTest
from tests.PlayerTest import PlayerTest
from tests.NavbarTest import NavbarTest
from tests.ActorPageTest import ActorPageTest
from tests.FilmPage import FilmPageTest

if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
            unittest.makeSuite(SignUpTest),
            unittest.makeSuite(LoginTest),
            unittest.makeSuite(ProfileTest),
            unittest.makeSuite(BrowseTest),
            unittest.makeSuite(MainPageTest),
            unittest.makeSuite(NavbarTest),
            unittest.makeSuite(PlayerTest),
            unittest.makeSuite(FilmPageTest),
            unittest.makeSuite(ActorPageTest)
        )
    )
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
