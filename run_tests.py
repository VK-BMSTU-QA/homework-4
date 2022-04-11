# -*- coding: utf-8 -*-

import subprocess
import sys
import unittest

from tests.LoginAndSignUpTest import LoginAndSignUpTest
from tests.MainTest import MainTest
from tests.PromotionTest import PromotionTest
from tests.SalesmanTest import SalesmanTest
from tests.AdvertTest import AdvertTest
from tests.NewAdvertTest import NewAdvertTest
from tests.EditTest import EditTest
from tests.ProfileTest import ProfileTest

from tests.config import config

if __name__ == '__main__':
    if (not config.DRIVER):
        subprocess.Popen(["bash", "./hub.sh"])
        subprocess.Popen(["bash", "./node.sh"])
    suite = unittest.TestSuite((
        # unittest.makeSuite(LoginTest)
        # unittest.makeSuite(MainTest)
        # unittest.makeSuite(PromotionTest)
        # unittest.makeSuite(SalesmanTest)
        # unittest.makeSuite(AdvertTest)
        # unittest.makeSuite(NewAdvertTest)
        # unittest.makeSuite(EditTest)
        unittest.makeSuite(ProfileTest)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())