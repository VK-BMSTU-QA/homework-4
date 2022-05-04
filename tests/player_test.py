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

        login_page = LoginPage(self.driver)
        login_page.login(self.EMAIL, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_next_track(self):
        home_page = HomePage(self.driver)
        player = home_page.player
        tracks = home_page.tracks
        second_track = tracks.get_track_id(1)
        tracks.play_track()
        player.next_track()
        playing_track = player.get_playing_track_id()
        self.assertEqual(second_track, playing_track)

    def test_player_hidden(self):
        home_page = HomePage(self.driver)
        player = home_page.player
        self.assertTrue(player.hidden())

    def test_mute(self):
        home_page = HomePage(self.driver)
        player = home_page.player
        tracks = home_page.tracks
        tracks.play_track()
        player.mute()
        self.assertTrue(player.muted())

    def test_unmute(self):
        home_page = HomePage(self.driver)
        player = home_page.player
        tracks = home_page.tracks
        tracks.play_track()
        player.mute()
        player.mute()
        self.assertFalse(player.muted())

    def test_prev_disabled(self):
        home_page = HomePage(self.driver)
        player = home_page.player
        tracks = home_page.tracks
        tracks.play_track()
        self.assertTrue(player.prev_disabled())

    def test_next_enabled(self):
        home_page = HomePage(self.driver)
        player = home_page.player
        tracks = home_page.tracks
        tracks.play_track()
        self.assertFalse(player.next_disabled())

    def test_next_disabled(self):
        home_page = HomePage(self.driver)
        player = home_page.player
        tracks = home_page.tracks
        tracks.play_track(last=True)
        self.assertTrue(player.next_disabled())

    def test_prev_enabled(self):
        home_page = HomePage(self.driver)
        player = home_page.player
        tracks = home_page.tracks
        tracks.play_track(last=True)
        self.assertFalse(player.prev_disabled())

    def test_pause(self):
        home_page = HomePage(self.driver)
        player = home_page.player
        tracks = home_page.tracks
        tracks.play_track()
        player.toggle_play()
        self.assertTrue(player.paused())

    def test_resume(self):
        home_page = HomePage(self.driver)
        player = home_page.player
        tracks = home_page.tracks
        tracks.play_track()
        player.toggle_play()
        player.toggle_play()
        self.assertFalse(player.paused())
