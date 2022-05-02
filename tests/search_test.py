from cProfile import label
import os
import re
import time
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from tests.common import Page

from tests.login_test import Component, LoginPage
from tests.main_test import MainPage

class SearchBar(Component):
    SEARCHBAR = '//input[@class="topbar__search-input"]'

    def click(self):
        bar = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SEARCHBAR)
        )
        bar.click()

    def query(self, query):
        self.driver.find_element_by_xpath(self.SEARCHBAR).send_keys(query)

class MainLayout(Component):
    LAY = '//div[@class="main-layout__content"]'
    LAY_CHILDREN = LAY + '/*'

    def has_no_content(self):
        return len(self.driver.find_elements_by_xpath(self.LAY_CHILDREN)) == 0

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
    def artists(self):
        return Artists(self.driver)
    
class Tracks(Component):
    FIRST_TRACK_ARTIST = '//div[@class="track__container__artist"]'

    def get_first_track_artist(self):
        artist = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FIRST_TRACK_ARTIST).text
        )
        return artist

class Albums(Component):
    FIRST_ALBUM_ARTIST = '//'

class Artists(Component):
    FIRST_ARTIST = '//'

class SearchPageTest(unittest.TestCase):
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

        search_page = SearchPage(self.driver)
        search_bar = search_page.search_bar
        main_layout = search_page.main_layout
        tracks = search_page.tracks
        albums = search_page.albums
        artists = search_page.artists
        
        search_bar.click()
        time.sleep(0.5) # !!!УБРАТЬб
        self.assertTrue(main_layout.has_no_content())
        
        search_artist = 'tWenTY           onE pilots'
        search_bar.query(search_artist)
        result_artist = tracks.get_first_track_artist()
        self.assertEqual(re.sub(' {2,}', ' ', search_artist.lower()), result_artist.lower())
