# -*- coding: utf-8 -*-

from cProfile import label
from lib2to3.pgen2 import driver
import os

import unittest
import selenium

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from sympy import proper_divisor_count

from tests import Page, Component
from tests.login_test import LoginPage


def has_element(driver, xpath):
    try:
        WebDriverWait(driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(xpath)
        )
    except NoSuchElementException:
        return False
    return True


class PlaylistPage(Page):
    path = 'playlist'

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
    def navbar(self):
        return Navbar(self.driver)


class PlaylistPageControls(Component):
    EDIT_BUTTON = '//div[contains(text(), "Edit playlist")]'

    def has_edit_button(self):
        return has_element(self.driver, self.EDIT_BUTTON)


class Sidebar(Component):
    LOGO = '//a[@class="sidebar__icon__logo"]'
    HOME = '//a[@class="sidebar__icon" and @href="/"]'
    FAVORITES = '//a[@class="sidebar__icon" and @href="/favorites"]'

    def go_home_by_logo(self):
        self.driver.find_element_by_xpath(self.LOGO).click()


class Playlists(Component):
    PLAYLIST = '//a[@class="pl-link"]'
    PUBLIC_PLAYLISTS_BUTTON = '//div[contains(text(), "Public playlists")]'
    TOP10_PUBLIC_PLAYLIST = '//div[@class="suggested-playlist-name" and contains(text(),"LostPointer top 10")]'
    CREATE_NEW = '//div[@class="suggested-playlist-name" and contains(text(), "Create new...")]'

    def get_first_playlist_href(self):
        return self.driver.find_element_by_xpath(self.PLAYLIST).get_attribute('href')

    def open_first_playlist(self):
        playlist = WebDriverWait(self.driver, 5, 0.1).until(
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


class Tracks(Component):
    FIRST_PLAY = '//img[@class="track-play"]'

    def play_first_track(self):
        play = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FIRST_PLAY)
        )
        print(play)
        print('play found')
        play.click()

    def get_first_track_id(self):
        return self.driver.find_element_by_xpath(self.FIRST_PLAY).get_attribute('data-id')


class Albums(Component):
    ALBUMS = '//div[@class="top-album"]'
    TITLE = '//div[@class="top-album__title"]'
    ARTIST = '//div[@class="top-album__artist"]'
    PLAY_ICON = 'i[class^=top-album__play]'

    def open_first_album(self):
        self.driver.find_element_by_xpath(self.ALBUMS).click()
    
    def get_first_album_id(self):
        id = self.driver.find_element_by_css_selector(self.PLAY_ICON).get_attribute('data-id')
        return id


class Player(Component):
    TRACK_LIKE = '//img[@class="player-fav"]'

    def get_playing_track_id(self):
        id = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TRACK_LIKE).get_attribute('data-id')
        )
        return id


class Navbar(Component):
    FAVORITES_BTN = '//img[@class="js-fav-link-icon"]'

    def open_favorites(self):
        self.driver.find_element_by_xpath(self.FAVORITES_BTN).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "favorites__description-title"))
        )


class MainPageTest(unittest.TestCase):
    EMAIL = os.environ['TESTUSERNAME']
    PASSWORD = os.environ['TESTPASSWORD']

    def setUp(self):
        browser = os.environ.get('TESTBROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        login_page = LoginPage(self.driver)
        login_page.open()

        login_form = login_page.form
        login_form.set_email(self.EMAIL)
        login_form.set_password(self.PASSWORD)
        login_form.login()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "avatar__img"))
        )

        main_page = MainPage(self.driver)

        albums = main_page.albums

        first_album = albums.get_first_album_id()
        albums.open_first_album()
        self.assertEqual(main_page.BASE_URL + f'album/{first_album}', self.driver.current_url)

        sidebar = main_page.sidebar

        sidebar.go_home_by_logo()
        self.assertEqual(main_page.BASE_URL, self.driver.current_url)

        playlists = main_page.playlists

        first_playlist_href = playlists.get_first_playlist_href()
        playlists.open_first_playlist()
        self.assertEqual(first_playlist_href, self.driver.current_url)
        main_page.open()

        playlist_page = PlaylistPage(self.driver)
        playlist_page_controls = playlist_page.controls
        playlists.create_new_playlist()
        self.assertTrue(playlist_page_controls.has_edit_button())

        main_page.open()

        playlists.open_public_playlists()
        self.assertTrue(playlists.get_top10_playlist_exists())

        tracks = main_page.tracks
        player = main_page.player

        first_track = tracks.get_first_track_id()
        tracks.play_first_track()
        self.driver.implicitly_wait(10)
        playing_track = player.get_playing_track_id()
        self.assertEqual(first_track, playing_track)
