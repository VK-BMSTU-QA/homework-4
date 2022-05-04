import os
import re
import unittest

from Login.LoginPage import LoginPage
from Search.SearchPage import SearchPage
from selenium.webdriver import DesiredCapabilities, Remote


class SearchPageTest(unittest.TestCase):
    EMAIL = os.environ["TESTUSERNAME"]
    PASSWORD = os.environ["TESTPASSWORD"]

    def setUp(self):
        browser = os.environ.get("TESTBROWSER", "CHROME")

        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
        )

        login_page = LoginPage(self.driver)
        login_page.login(self.EMAIL, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_search_hides_content(self):
        search_page = SearchPage(self.driver)
        search_bar = search_page.search_bar
        main_layout = search_page.main_layout

        search_bar.click()
        self.assertTrue(main_layout.has_no_content())

    def test_search_ignores_case_and_returns_results(self):
        search_page = SearchPage(self.driver)
        search_bar = search_page.search_bar
        main_layout = search_page.main_layout
        tracks = search_page.tracks
        search_artist = "tWenTY           onE pilots"
        search_bar.query(search_artist)
        result_artist = tracks.get_track_artist()
        self.assertEqual(re.sub(" {2,}", " ", search_artist.lower()), result_artist.lower())

    def test_search_plays_first_track(self):
        search_page = SearchPage(self.driver)
        search_bar = search_page.search_bar
        tracks = search_page.tracks
        player = search_page.player
        search_artist = "tWenTY           onE pilots"
        search_bar.query(search_artist)
        first_track = tracks.get_track_id()
        tracks.play_track()
        playing_track = player.get_playing_track_id()
        self.assertEqual(first_track, playing_track)

    def test_search_add_to_playlist_popup(self):
        search_page = SearchPage(self.driver)
        search_bar = search_page.search_bar
        tracks = search_page.tracks
        search_artist = "tWenTY           onE pilots"
        search_bar.query(search_artist)
        tracks.open_first_add_to_playlist()
        self.assertTrue(tracks.playlist_menu_exists())

    def test_search_shows_not_found(self):
        search_page = SearchPage(self.driver)
        search_bar = search_page.search_bar
        main_layout = search_page.main_layout
        search_bar.query("Fhu3u8nf87#Gfd73Odhn8#HD78NG#Dn783gdo78g#")
        self.assertTrue(main_layout.not_found())

    def test_search_plays_first_album(self):
        search_page = SearchPage(self.driver)
        search_bar = search_page.search_bar
        albums = search_page.albums
        player = search_page.player
        tracks = search_page.tracks
        search_album = "blurry"
        search_bar.query(search_album)
        albums.play_first_album()
        playing_track = player.get_playing_track_id()
        albums.open_first_album()
        first_track = tracks.get_track_id()
        self.assertEqual(first_track, playing_track)
