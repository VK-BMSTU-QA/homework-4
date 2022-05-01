# -*- coding: utf-8 -*-

import os

import unittest
from urllib.parse import urljoin
import selenium

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from tests.login_test import LoginPage

class Page(object):
    BASE_URL = 'https://lostpointer.site/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

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

class Component(object):
    def __init__(self, driver):
        self.driver = driver

class Sidebar(Component):
    LOGO = '//a[@class="sidebar__icon__logo"]'
    HOME = '//a[@class="sidebar__icon" and @href="/"]'
    FAVORITES = '//a[@class="sidebar__icon" and @href="/favorites"]'

    def go_home_by_logo(self):
        self.driver.find_element_by_xpath(self.LOGO).click()

class Playlists(Component):
    PLAYLIST = '//a[@class="pl-link"]'

    def get_first_playlist_href(self):
        return self.driver.find_element_by_xpath(self.PLAYLIST).get_attribute('href')

    def open_first_playlist(self):
        playlist = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PLAYLIST)
        )
        playlist.click()

class Albums(Component):
    ALBUMS = '//div[@class="top-album"]'
    TITLE = '//div[@class="top-album__title"]'
    ARTIST = '//div[@class="top-album__artist"]'
    PLAY_ICON = 'i[class^=top-album__play]'

    def open_first_album(self):
        album = self.driver.find_element_by_xpath(self.ALBUMS).click()
    
    def get_first_album_id(self):
        return self.driver.find_element_by_css_selector(self.PLAY_ICON).get_attribute('data-id')

class MainPageTest(unittest.TestCase):
    EMAIL = os.environ['TESTUSERNAME']
    PASSWORD = os.environ['TESTPASSWORD']

    def setUp(self):
        browser = os.environ.get('TESTBROWSER', 'CHROME')

        self.driver = Remote(
            command_executor = 'http://127.0.0.1:4444/wd/hub',
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
