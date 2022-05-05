import os
import unittest

from Home.HomePage import HomePage
from Login.LoginPage import LoginPage
from Playlist.PlaylistPage import PlaylistPage
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options


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

    def tearDown(self):
        self.driver.quit()

    def test_open_first_album(self):
        home_page = HomePage(self.driver)

        albums = home_page.albums

        first_album = albums.get_first_album_id()
        albums.open_first_album()
        self.assertEqual(home_page.BASE_URL + f"album/{first_album}", self.driver.current_url)

    def test_go_home_from_profile(self):
        home_page = HomePage(self.driver)
        sidebar = home_page.sidebar
        sidebar.go_home_by_logo()
        self.assertEqual(home_page.BASE_URL, self.driver.current_url)

    def test_open_first_playlist(self):
        home_page = HomePage(self.driver)
        playlists = home_page.playlists
        first_playlist_href = playlists.get_first_playlist_href()
        playlists.open_first_playlist()
        self.assertEqual(first_playlist_href, self.driver.current_url)

    def test_create_new_playlist(self):
        home_page = HomePage(self.driver)
        playlists = home_page.playlists
        playlist_page = PlaylistPage(self.driver)
        playlist_page_controls = playlist_page.controls
        playlists.create_new_playlist()
        self.assertTrue(playlist_page_controls.has_edit_button())

    def test_open_public_playlist(self):
        home_page = HomePage(self.driver)
        playlists = home_page.playlists
        playlists.open_public_playlists()
        self.assertTrue(playlists.get_top10_playlist_exists())

    def test_play_first_track_unauthorized(self):
        home_page = HomePage(self.driver)
        home_page.topbar.log_out()
        tracks = home_page.tracks
        tracks.play_track()
        tracks.check_redirect_to_login()

    def test_play_first_track(self):
        home_page = HomePage(self.driver)
        tracks = home_page.tracks
        player = home_page.player
        first_track = tracks.get_track_id()
        tracks.play_track()
        playing_track = player.get_playing_track_id()
        self.assertEqual(first_track, playing_track)

    def test_play_first_album(self):
        home_page = HomePage(self.driver)
        player = home_page.player
        tracks = home_page.tracks
        albums = home_page.albums
        albums.play_first_album()
        playing_track = player.get_playing_track_id()
        albums.open_first_album()
        first_track = tracks.get_track_id()
        self.assertEqual(first_track, playing_track)

    def test_add_to_playlist_popup(self):
        tracks = HomePage(self.driver).tracks
        tracks.open_first_add_to_playlist()
        self.assertTrue(tracks.playlist_menu_exists())

    def test_open_profile_via_settings(self):
        home_page = HomePage(self.driver)
        topbar = home_page.topbar
        topbar.click_settings()
        self.assertEqual(self.driver.current_url, home_page.BASE_URL + "profile")

    def test_open_profile_via_avatar(self):
        home_page = HomePage(self.driver)
        topbar = home_page.topbar
        topbar.click_avatar()
        self.assertEqual(self.driver.current_url, home_page.BASE_URL + "profile")

    def test_logout(self):
        home_page = HomePage(self.driver)
        topbar = home_page.topbar
        topbar.log_out()
        self.assertTrue(topbar.logged_out())
