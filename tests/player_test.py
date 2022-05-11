import os
import unittest

from Common.CommonComponents import Player
from Home.HomePage import HomePage
from Login.LoginPage import LoginPage
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.utils import CHECK_FREQ, TIMEOUT


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

    def test_mute_unmute(self):
        player = self.home_page.player
        self.home_page.tracks.play_track()
        player.mute()
        self.assertEqual(len(self.driver.find_elements(by=By.XPATH, value=Player.MUTE_XPATH)), 0)
        player.mute()
        self.assertEqual(len(self.driver.find_elements(by=By.XPATH, value=Player.MUTE_XPATH)), 1)

    def test_no_prev_for_first_track(self):
        self.home_page.tracks.play_track()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: len(d.find_elements(by=By.XPATH, value=Player.PREV_TRACK_CLASS)) == 0
        ))
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=Player.NEXT_TRACK_CLASS)
        ))

    def test_no_next_for_last_track(self):
        self.home_page.tracks.play_track(last=True)
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: len(d.find_elements(by=By.XPATH, value=Player.NEXT_TRACK_CLASS)) == 0
        ))
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=Player.PREV_TRACK_CLASS)
        ))

    def test_play_pause(self):
        self.home_page.tracks.play_track()
        player = self.home_page.player
        player.toggle_play()
        self.assertTrue(Player.PLAYER_PAUSED in self.driver.find_element(by=By.XPATH, value=Player.PLAY).get_attribute("src"))
        player.toggle_play()
        self.assertFalse(Player.PLAYER_PAUSED in self.driver.find_element(by=By.XPATH, value=Player.PLAY).get_attribute("src"))
