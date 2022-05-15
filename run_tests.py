import sys
import unittest

from tests.favorites_test import FavoritesTest
from tests.home_test import HomePageTest
from tests.login_test import LoginTest
from tests.player_test import PlayerTest
from tests.playlists_test import PlaylistsTest
from tests.profile_test import ProfilePageTest
from tests.register_test import RegisterTest
from tests.search_test import SearchPageTest

if __name__ == "__main__":
    suite = unittest.TestSuite(
        (
            # unittest.makeSuite(LoginTest),
            # unittest.makeSuite(RegisterTest),
            # unittest.makeSuite(HomePageTest),
            # unittest.makeSuite(SearchPageTest),
            # unittest.makeSuite(ProfilePageTest),
            # unittest.makeSuite(FavoritesTest),
            # unittest.makeSuite(PlayerTest),
            unittest.makeSuite(PlaylistsTest),
        )
    )
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
