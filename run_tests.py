import sys
import unittest
from tests.login.login_test import LoginTest
from tests.profile_edit.profile_test import ProfileTest
from tests.level_edit.add_level_test import AddLevelTest
from tests.level_edit.edit_level_test import EditLevelTest
from tests.search_creator.search_test import SearchTest
from tests.creator.creator_test import CreatorTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(LoginTest),
        unittest.makeSuite(ProfileTest),
        unittest.makeSuite(AddLevelTest),
        unittest.makeSuite(EditLevelTest),
        unittest.makeSuite(SearchTest),
        unittest.makeSuite(CreatorTest)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
