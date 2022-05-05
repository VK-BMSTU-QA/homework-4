import os
import unittest

from Favorites.FavoritesPage import FavoritesPage
from Home.HomePage import HomePage
from Login.LoginPage import LoginPage
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options


class FavoritesTest(unittest.TestCase):
    EMAIL = os.environ["TESTUSERNAME"]
    PASSWORD = os.environ["TESTPASSWORD"]

    def setUp(self):
        browser = os.environ.get("TESTBROWSER", "CHROME")
        options = Options()
        options.headless = bool(os.environ.get("HEADLESS", False))
        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
        )
        self.login_page = LoginPage(self.driver)
        self.login_page.login(self.EMAIL, self.PASSWORD)

        self.favorites_page = FavoritesPage(self.driver)
        self.favorites_page.open()

        self.home_page = HomePage(self.driver)
        self.favorites_page = FavoritesPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_album_opening(self):
        self.favorites_page.track_list.open_first_album()
        self.assertTrue(self.favorites_page.track_list.album_is_opened())

    def test_artist_opening(self):
        self.favorites_page.track_list.open_first_artist()
        self.assertTrue(self.favorites_page.track_list.artist_is_opened())

    def test_like(self):
        track_id = self.favorites_page.track_list.get_track_id()

        self.favorites_page.track_list.remove_like(track_id)
        self.assertFalse(self.favorites_page.track_list.track_is_liked(track_id))

        self.favorites_page.track_list.get_like_btn(track_id)

        self.favorites_page.track_list.add_like(track_id)
        self.assertTrue(self.favorites_page.track_list.track_is_liked(track_id))

    def test_favorites_opening_from_navbar(self):
        self.home_page.sidebar.go_favorites()
        self.assertTrue(self.favorites_page.is_open())
