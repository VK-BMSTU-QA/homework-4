import sys
import unittest
from tests.login.login_test import LoginTest
from tests.profile_edit.profile_test import ProfileTest
from tests.creator_edit.creator_edit_test import CreatorEditTest
from tests.level_edit.add_level_test import AddLevelTest
from tests.level_edit.edit_level_test import EditLevelTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTest),
        unittest.makeSuite(ProfileTest),
        unittest.makeSuite(CreatorEditTest),
        unittest.makeSuite(AddLevelTest),
        unittest.makeSuite(EditLevelTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
