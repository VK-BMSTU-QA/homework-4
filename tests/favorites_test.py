import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from tests import Page, Tracks
from tests.login_test import LoginPage
from tests.main_test import MainPage


class FavoritesPage(Page):
    PATH = 'favorites'

    @property
    def track_list(self):
        return Tracks(self.driver)


class FavoritesTest(unittest.TestCase):
    EMAIL = os.environ['TESTUSERNAME']
    PASSWORD = os.environ['TESTPASSWORD']

    def setUp(self):
        browser = os.environ.get('TESTBROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.login_page = LoginPage(self.driver)
        self.login_page.open()
        self.login_form = self.login_page.form
        self.login_form.set_email(self.EMAIL)
        self.login_form.set_password(self.PASSWORD)
        self.login_form.login()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "avatar__img"))
        )

        self.favorites_page = FavoritesPage(self.driver)
        self.favorites_page.open()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "favorites__description-title"))
        )

    def tearDown(self):
        self.driver.quit()

    def test_album_opening(self):
        self.favorites_page.track_list.open_first_album()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "album"))
        )

    def test_artist_opening(self):
        self.favorites_page.track_list.open_first_artist()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "artist"))
        )

    def test_toggle_favor(self):
        track_id = self.favorites_page.track_list.get_first_track_id()
        
        self.favorites_page.track_list.remove_favor(track_id)
        assert not self.favorites_page.track_list.track_is_in_favor(track_id)

        self.favorites_page.track_list.get_fav_btn(track_id)

        self.favorites_page.track_list.add_to_favorites(track_id)
        assert self.favorites_page.track_list.track_is_in_favor(track_id)

    # def test_toggle_player_favor(self):
    #     pass

    def test_favorites_opening_from_navbar(self):
        self.main_page = MainPage(self.driver)
        self.main_page.sidebar.go_favorites()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "favorites__description-title"))
        )

