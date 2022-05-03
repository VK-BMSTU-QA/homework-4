
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests import Page, Albums, Tracks, Player, Topbar, has_element, Sidebar
from tests.login_test import Component, LoginPage


class PlaylistPage(Page):
    PATH = 'playlist'

    @property
    def controls(self):
        return PlaylistPageControls(self.driver)


class MainPage(Page):
    PATH = ''

    @property
    def albums(self):
        return Albums(self.driver)

    @property
    def sidebar(self):
        return Sidebar(self.driver)

    @property
    def playlists(self):
        return Playlists(self.driver)

    @property
    def tracks(self):
        return Tracks(self.driver)

    @property
    def player(self):
        return Player(self.driver)

    @property
    def topbar(self):
        return Topbar(self.driver)


class PlaylistPageControls(Component):
    EDIT_BUTTON = '//div[contains(text(), "Edit playlist")]'

    def has_edit_button(self):
        return has_element(self.driver, self.EDIT_BUTTON)


class Playlists(Component):
    PLAYLIST = '//a[@class="pl-link"]'
    PUBLIC_PLAYLISTS_BUTTON = '//div[contains(text(), "Public playlists")]'
    TOP10_PUBLIC_PLAYLIST = '//div[@class="suggested-playlist-name" and contains(text(),"LostPointer top 10")]'
    CREATE_NEW = '//div[@class="suggested-playlist-name" and contains(text(), "Create new...")]'

    def get_first_playlist_href(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.PLAYLIST).get_attribute('href')
        )

    def open_first_playlist(self):
        playlist = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PLAYLIST)
        )
        playlist.click()

    def open_public_playlists(self):
        public = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PUBLIC_PLAYLISTS_BUTTON)
        )
        public.click()

    def get_top10_playlist_exists(self):
        return has_element(self.driver, self.TOP10_PUBLIC_PLAYLIST)

    def create_new_playlist(self):
        create = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CREATE_NEW)
        )
        create.click()


class MainPageTest(unittest.TestCase):
    EMAIL = os.environ['TESTUSERNAME']
    PASSWORD = os.environ['TESTPASSWORD']

    def setUp(self):
        browser = os.environ.get('TESTBROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        login_page = LoginPage(self.driver)
        login_page.open()

        login_form = login_page.form
        login_form.set_email(self.EMAIL)
        login_form.set_password(self.PASSWORD)
        login_form.login()

        WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "avatar__img"))
        )

    def tearDown(self):
        self.driver.quit()

    def test_open_first_album(self):
        main_page = MainPage(self.driver)

        albums = main_page.albums

        first_album = albums.get_first_album_id()
        albums.open_first_album()
        self.assertEqual(main_page.BASE_URL +
                         f'album/{first_album}', self.driver.current_url)

    def test_go_home_from_profile(self):
        main_page = MainPage(self.driver)
        sidebar = main_page.sidebar
        sidebar.go_home_by_logo()
        self.assertEqual(main_page.BASE_URL, self.driver.current_url)

    def test_open_first_playlist(self):
        main_page = MainPage(self.driver)
        playlists = main_page.playlists
        first_playlist_href = playlists.get_first_playlist_href()
        playlists.open_first_playlist()
        self.assertEqual(first_playlist_href, self.driver.current_url)

    def test_create_new_playlist(self):
        main_page = MainPage(self.driver)
        playlists = main_page.playlists
        playlist_page = PlaylistPage(self.driver)
        playlist_page_controls = playlist_page.controls
        playlists.create_new_playlist()
        self.assertTrue(playlist_page_controls.has_edit_button())

    def test_open_public_playlist(self):
        main_page = MainPage(self.driver)
        playlists = main_page.playlists
        playlists.open_public_playlists()
        self.assertTrue(playlists.get_top10_playlist_exists())

    def test_play_first_track_unauthorized(self):
        main_page = MainPage(self.driver)
        main_page.topbar.log_out()
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_attribute_to_include((By.ID, "signin-button"), "href")
        )
        tracks = main_page.tracks
        tracks.play_track()

        WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "login-ui"))
        )

    def test_play_first_track(self):
        main_page = MainPage(self.driver)
        tracks = main_page.tracks
        player = main_page.player
        first_track = tracks.get_track_id()
        tracks.play_track()
        playing_track = player.get_playing_track_id()
        self.assertEqual(first_track, playing_track)

    def test_play_first_album(self):
        main_page = MainPage(self.driver)
        player = main_page.player
        tracks = main_page.tracks
        albums = main_page.albums
        albums.play_first_album()
        playing_track = player.get_playing_track_id()
        albums.open_first_album()
        first_track = tracks.get_track_id()
        self.assertEqual(first_track, playing_track)

    def test_add_to_playlist_popup(self):
        tracks = MainPage(self.driver).tracks
        tracks.open_first_add_to_playlist()
        self.assertTrue(tracks.playlist_menu_exists())

    def test_open_profile_via_settings(self):
        main_page = MainPage(self.driver)
        topbar = main_page.topbar
        topbar.click_settings()
        self.assertEqual(self.driver.current_url,
                         main_page.BASE_URL + 'profile')

    def test_open_profile_via_avatar(self):
        main_page = MainPage(self.driver)
        topbar = main_page.topbar
        topbar.click_avatar()
        self.assertEqual(self.driver.current_url,
                         main_page.BASE_URL + 'profile')

    def test_logout(self):
        main_page = MainPage(self.driver)
        topbar = main_page.topbar
        topbar.log_out()
        self.assertTrue(topbar.logged_out())
    