import os
import unittest

from Common.CommonComponents import Topbar, Tracks
from Home.HomePage import HomePage
from Login.LoginPage import LoginPage
from Playlist.PlaylistComponents import PlaylistPageControls
from Playlist.PlaylistPage import PlaylistPage
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.utils import CHECK_FREQ, TIMEOUT, has_element


class HomePageTest(unittest.TestCase):
    EMAIL = os.environ["TESTUSERNAME"]
    PASSWORD = os.environ["TESTPASSWORD"]

    def setUp(self):
        browser = os.environ.get("TESTBROWSER", "CHROME")
        options = Options()
        options.headless = bool(os.environ.get("HEADLESS", False))
        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            options=options,
        )

        login_page = LoginPage(self.driver)
        login_page.login(self.EMAIL, self.PASSWORD)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_play_first_track_unauthorized(self):
        self.home_page.topbar.log_out()
        tracks = self.home_page.tracks
        tracks.play_track()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            EC.presence_of_element_located((By.CLASS_NAME, Tracks.LOGIN_UI))
        ))

    def test_play_first_track(self):
        tracks = self.home_page.tracks
        tracks.play_track()
        self.assertEqual(tracks.get_track_id(), self.home_page.player.get_playing_track_id())

    def test_play_first_album(self):
        albums = self.home_page.albums
        albums.play_first_album()
        albums.open_first_album()
        self.assertEqual(self.home_page.tracks.get_track_id(), self.home_page.player.get_playing_track_id())

    def test_add_to_playlist_popup(self):
        tracks = self.home_page.tracks
        tracks.open_first_add_to_playlist()
        self.assertTrue(has_element(self.driver, Tracks.PLAYLISTS_MENU))

    def test_logout(self):
        topbar = self.home_page.topbar
        topbar.log_out()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                lambda d: len(d.find_elements(by=By.XPATH, value=Topbar.AVATAR)) == 0
        ))
