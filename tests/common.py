# -*- coding: utf-8 -*-

from urllib.parse import urljoin

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class Page(object):
    BASE_URL = 'https://lostpointer.site/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


def has_element(driver, xpath):
    try:
        WebDriverWait(driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(xpath)
        )
    except NoSuchElementException:
        return False
    return True


class Player(Component):
    TRACK_LIKE = '//img[@class="player-fav"]'

    def get_playing_track_id(self):
        id = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.TRACK_LIKE).get_attribute('data-id')
        )
        return id


class Albums(Component):
    ALBUMS = '//div[@class="top-album"]'
    TITLE = '//div[@class="top-album__title"]'
    ARTIST = '//div[@class="top-album__artist"]'
    PLAY_ICON = 'i[class^=top-album__play]'

    def open_first_album(self):
        self.driver.find_element_by_xpath(self.ALBUMS).click()

    def get_first_album_id(self):
        id = self.driver.find_element_by_css_selector(
            self.PLAY_ICON).get_attribute('data-id')
        return id

    def play_first_album(self):
        play = WebDriverWait(self.driver, 10, 0, 1).until(
            lambda d: d.find_element_by_css_selector(self.PLAY_ICON)
        )
        play.click()


class Topbar(Component):
    SETTINGS = '//i[@class="topbar-icon fa-solid fa-gear"]'
    AVATAR = '//img[@class="avatar__img"]'

    def click_settings(self):
        settings = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SETTINGS)
        )
        settings.click()

    def click_avatar(self):
        avatar = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.AVATAR)
        )
        avatar.click()


class TopArtists(Component):
    FIRST_ARTIST = '//img[@class="suggested-artist__img"]'

    def get_first_artist_id(self):
        return self.driver.find_element_by_xpath(self.FIRST_ARTIST).get_attribute('data-id')


class Tracks(Component):
    FIRST_PLAY = '//img[@class="track-play"]'
    FIRST_PLAYLIST = '//img[@class="track-list-item-playlist"]'
    PLAYLISTS_MENU = '//div[@class="menu"]'
    FIRST_TRACK_ARTIST = '//div[@class="track__container__artist"]'

    def get_first_track_artist(self):
        artist = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FIRST_TRACK_ARTIST).text
        )
        return artist

    def play_first_track(self):
        play = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FIRST_PLAY)
        )
        play.click()

    def get_first_track_id(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.FIRST_PLAY).get_attribute('data-id')
        )

    def open_first_add_to_playlist(self):
        playlist = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FIRST_PLAYLIST)
        )
        playlist.click()

    def playlist_menu_exists(self):
        return has_element(self.driver, self.PLAYLISTS_MENU)


class Sidebar(Component):
    LOGO = '//a[@class="sidebar__icon__logo"]'
    HOME = '//a[@class="sidebar__icon" and @href="/"]'
    FAVORITES = '//a[@class="sidebar__icon" and @href="/favorites"]'

    def go_home_by_logo(self):
        self.driver.find_element_by_xpath(self.LOGO).click()
