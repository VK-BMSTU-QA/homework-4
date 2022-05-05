import os
import unittest

from Home.HomePage import HomePage
from Login.LoginPage import LoginPage
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options

class PlayerTest(unittest.TestCase):
    EMAIL = os.environ["TESTUSERNAME"]
    PASSWORD = os.environ["TESTPASSWORD"]

    def setUp(self):
        browser = os.environ.get("TESTBROWSER", "CHROME")
        options = Options()
        options.headless = bool(os.environ.get("HEADLESS", False))
        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            options=options
        )

        self.login_page = LoginPage(self.driver)
        self.login_page.login(self.EMAIL, self.PASSWORD)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_next_track(self):
        player = self.home_page.player
        tracks = self.home_page.tracks
        second_track = tracks.get_track_id(1)
        tracks.play_track()
        player.next_track()
        playing_track = player.get_playing_track_id()
        self.assertEqual(second_track, playing_track)

    def test_player_hidden(self):
        self.assertTrue(self.home_page.player.hidden())

    def test_mute(self):
        player = self.home_page.player
        self.home_page.tracks.play_track()
        player.mute()
        self.assertTrue(player.muted())

    def test_unmute(self):
        player = self.home_page.player
        self.home_page.tracks.play_track()
        player.mute()
        player.mute()
        self.assertFalse(player.muted())

    def test_prev_disabled(self):
        self.home_page.tracks.play_track()
        self.assertTrue(self.home_page.player.prev_disabled())

    def test_next_enabled(self):
        self.home_page.tracks.play_track()
        self.assertFalse(self.home_page.player.next_disabled())

    def test_next_disabled(self):
        self.home_page.tracks.play_track(last=True)
        self.assertTrue(self.home_page.player.next_disabled())

    def test_prev_enabled(self):
        self.home_page.tracks.play_track(last=True)
        self.assertFalse(self.home_page.player.prev_disabled())

    def test_pause(self):
        self.home_page.tracks.play_track()
        player = self.home_page.player
        player.toggle_play()
        self.assertTrue(player.paused())

    def test_resume(self):
        player = self.home_page.player
        tracks = self.home_page.tracks
        tracks.play_track()
        player.toggle_play()
        player.toggle_play()
        self.assertFalse(player.paused())
