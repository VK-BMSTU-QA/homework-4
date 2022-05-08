# -*- coding: utf-8 -*-

import subprocess
import sys
import unittest

from tests.LoginTest import LoginTest
from tests.SignUpTest import SignUpTest
from tests.MainTest import MainTest
from tests.SalesmanTest import SalesmanTest
from tests.AdvertTest import AdvertTest
from tests.NewAdvertTest import NewAdvertTest
from tests.EditTest import EditTest
from tests.ProfileTest import ProfileTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTest),
        unittest.makeSuite(SignUpTest),
        unittest.makeSuite(SalesmanTest),
        unittest.makeSuite(MainTest),
        unittest.makeSuite(AdvertTest),
        unittest.makeSuite(EditTest),
        unittest.makeSuite(NewAdvertTest),
        unittest.makeSuite(ProfileTest)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
