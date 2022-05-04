import os
import unittest

from Favorites.FavoritesPage import FavoritesPage
from Home.HomePage import HomePage
from Login.LoginPage import LoginPage
from selenium.webdriver import DesiredCapabilities, Remote


class FavoritesTest(unittest.TestCase):
    EMAIL = os.environ["TESTUSERNAME"]
    PASSWORD = os.environ["TESTPASSWORD"]

    def setUp(self):
        browser = os.environ.get("TESTBROWSER", "CHROME")

        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
        )
        self.login_page = LoginPage(self.driver)
        self.login_page.login(self.EMAIL, self.PASSWORD)

        self.favorites_page = FavoritesPage(self.driver)
        self.favorites_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_album_opening(self):
        self.favorites_page.track_list.open_first_album()

    def test_artist_opening(self):
        self.favorites_page.track_list.open_first_artist()

    def test_like(self):
        track_id = self.favorites_page.track_list.get_track_id()

        self.favorites_page.track_list.remove_like(track_id)
        assert not self.favorites_page.track_list.track_is_liked(track_id)

        self.favorites_page.track_list.get_like_btn(track_id)

        self.favorites_page.track_list.add_like(track_id)
        assert self.favorites_page.track_list.track_is_liked(track_id)

    def test_player_like(self):
        track_id = self.favorites_page.track_list.get_track_id()

        self.favorites_page.track_list.play_track()
        self.favorites_page.track_list.pause_track()

        self.favorites_page.track_list.remove_like(track_id)
        self.favorites_page.player.track_is_not_liked()

        self.favorites_page.track_list.add_like(track_id)
        self.favorites_page.player.track_is_liked()

        self.favorites_page.player.remove_like()
        assert not self.favorites_page.track_list.track_is_liked(track_id)

        self.favorites_page.player.add_like()
        assert self.favorites_page.track_list.track_is_liked(track_id)

    def test_favorites_opening_from_navbar(self):
        self.home_page = HomePage(self.driver)
        self.home_page.sidebar.go_favorites()
