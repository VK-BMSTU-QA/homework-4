# -*- coding: utf-8 -*-

import os
import re
import time
import unittest
from cProfile import label

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.common import Page, Player
from tests.login_test import Component, LoginPage
from tests.main_test import Albums, MainPage, Tracks


class SearchBar(Component):
    SEARCHBAR = '//input[@class="topbar__search-input"]'

    def click(self):
        bar = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SEARCHBAR)
        )
        bar.click()

    def query(self, query):
        input = self.driver.find_element_by_xpath(self.SEARCHBAR)
        input.clear()
        # Хак, потому что есть дебаунс и он срабатывает только на физ. нажатие кнопки
        input.send_keys(' ')
        input.send_keys(Keys.BACKSPACE)
        WebDriverWait(self.driver, 10, 0, 1).until(
            lambda d: len(d.find_elements_by_xpath(
                MainLayout.LAY_CHILDREN)) == 0
        )
        input.send_keys(query)
        WebDriverWait(self.driver, 10, 0, 1).until(
            lambda d: len(d.find_elements_by_xpath(
                MainLayout.LAY_CHILDREN)) != 0
        )


class MainLayout(Component):
    LAY = '//div[@class="main-layout__content"]'
    LAY_CHILDREN = LAY + '/*'
    NOT_FOUND = '//div[@class="search__content__not-found"]'

    def has_no_content(self):
        return len(self.driver.find_elements_by_xpath(self.LAY_CHILDREN)) == 0

    def not_found(self):
        return len(self.driver.find_elements_by_xpath(self.NOT_FOUND)) == 1


class SearchPage(Page):
    path = 'search'

    @property
    def search_bar(self):
        return SearchBar(self.driver)

    @property
    def main_layout(self):
        return MainLayout(self.driver)

    @property
    def tracks(self):
        return Tracks(self.driver)

    @property
    def albums(self):
        return Albums(self.driver)

    @property
    def player(self):
        return Player(self.driver)

    # @property
    # def artists(self):
    #     return Artists(self.driver)


class SearchPageTest(unittest.TestCase):
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

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "avatar__img"))
        )

    def tearDown(self):
        self.driver.quit()

    def test_search_hides_content(self):
        search_page = SearchPage(self.driver)
        search_bar = search_page.search_bar
        main_layout = search_page.main_layout

        search_bar.click()
        time.sleep(0.5)  # !!!УБРАТЬб
        self.assertTrue(main_layout.has_no_content())

    def test_search_ignores_case_and_returns_results(self):
        search_page = SearchPage(self.driver)
        search_bar = search_page.search_bar
        main_layout = search_page.main_layout
        tracks = search_page.tracks
        search_artist = 'tWenTY           onE pilots'
        search_bar.query(search_artist)
        result_artist = tracks.get_track_artist()
        self.assertEqual(
            re.sub(' {2,}', ' ', search_artist.lower()), result_artist.lower())

    def test_search_plays_first_track(self):
        search_page = SearchPage(self.driver)
        search_bar = search_page.search_bar
        tracks = search_page.tracks
        player = search_page.player
        search_artist = 'tWenTY           onE pilots'
        search_bar.query(search_artist)
        first_track = tracks.get_track_id()
        tracks.play_track()
        playing_track = player.get_playing_track_id()
        self.assertEqual(first_track, playing_track)

    def test_search_add_to_playlist_popup(self):
        search_page = SearchPage(self.driver)
        search_bar = search_page.search_bar
        tracks = search_page.tracks
        search_artist = 'tWenTY           onE pilots'
        search_bar.query(search_artist)
        tracks.open_first_add_to_playlist()
        self.assertTrue(tracks.playlist_menu_exists())

    def test_search_shows_not_found(self):
        search_page = SearchPage(self.driver)
        search_bar = search_page.search_bar
        main_layout = search_page.main_layout
        search_bar.query('Fhu3u8nf87#Gfd73Odhn8#HD78NG#Dn783gdo78g#')
        self.assertTrue(main_layout.not_found())

    def test_search_plays_first_album(self):
        search_page = SearchPage(self.driver)
        search_bar = search_page.search_bar
        albums = search_page.albums
        player = search_page.player
        tracks = search_page.tracks
        search_album = 'blurry'
        search_bar.query(search_album)
        albums.play_first_album()
        playing_track = player.get_playing_track_id()
        albums.open_first_album()
        first_track = tracks.get_track_id()
        self.assertEqual(first_track, playing_track)
