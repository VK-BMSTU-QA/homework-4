import os
import re
import unittest

from Login.LoginPage import LoginPage
from Search.SearchComponents import MainLayout
from Search.SearchPage import SearchPage
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from tests.utils import has_element


class SearchPageTest(unittest.TestCase):
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

        self.search_page = SearchPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search_artist(self):
        search_artist = "Linkin Park"
        artists = self.search_page.artists
        self.search_page.search_bar.query(search_artist)
        artists.open_first_artist()
        self.assertEqual(search_artist.lower(), artists.get_artist_title().lower())

    def test_search_album(self):
        search_album = "Лучшее"
        albums = self.search_page.albums
        self.search_page.search_bar.query(search_album)
        result_album = albums.get_first_album_title()
        self.assertEqual(search_album.lower(), result_album.lower())

    def test_search_track(self):
        search_track = "Давай-наяривай"
        tracks = self.search_page.tracks
        self.search_page.search_bar.query(search_track)
        result_track = tracks.get_first_track_title()
        self.assertEqual(search_track.lower(), result_track.lower())

    def test_search_hides_content(self):
        self.search_page.search_bar.click()
        self.assertEqual(len(self.driver.find_elements(by=By.XPATH, value=MainLayout.LAY_CHILDREN)), 0)

    def test_search_ignores_case_and_returns_results(self):
        search_artist = "tWenTY           onE pilots"
        self.search_page.search_bar.query(search_artist)
        result_artist = self.search_page.tracks.get_track_artist()
        self.assertEqual(re.sub(" {2,}", " ", search_artist.lower()), result_artist.lower())

    def test_search_plays_first_track(self):
        tracks = self.search_page.tracks
        self.search_page.search_bar.query("tWenTY           onE pilots")
        first_track = tracks.get_track_id()
        tracks.play_track()
        self.assertEqual(first_track, self.search_page.player.get_playing_track_id())

    def test_search_add_to_playlist_popup(self):
        tracks = self.search_page.tracks
        self.search_page.search_bar.query("tWenTY           onE pilots")
        tracks.open_first_add_to_playlist()
        self.assertTrue(has_element(self.driver, tracks.PLAYLISTS_MENU))

    def test_search_shows_not_found(self):
        self.search_page.search_bar.query("Fhu3u8nf87#Gfd73Odhn8#HD78NG#Dn783gdo78g#")
        self.assertTrue(self.driver.find_element(by=By.XPATH, value=MainLayout.NOT_FOUND))

    def test_search_plays_first_album(self):
        albums = self.search_page.albums
        self.search_page.search_bar.query("blurry")
        albums.play_first_album()
        playing_track = self.search_page.player.get_playing_track_id()
        albums.open_first_album()
        self.assertEqual(self.search_page.tracks.get_track_id(), playing_track)
