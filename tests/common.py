# -*- coding: utf-8 -*-

from urllib.parse import urljoin

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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
    CURRENT_TIME = '//div[@class="player__time"]'
    PREV_TRACK = '//img[@id="player-left"]'
    PREV_TRACK_CLASS = '//img[@class="player-skip-left"]'
    PLAY = '//img[@id="player-play"]'
    NEXT_TRACK = '//img[@id="player-right"]'
    NEXT_TRACK_CLASS = '//img[@class="player-skip-right"]'
    PLAYER = '//div[@class="player"]'
    MUTE = 'img[class^="mute"]'
    MUTE_XPATH = '//img[@class="mute"]'

    def prev_disabled(self):
        return len(self.driver.find_elements_by_xpath(self.PREV_TRACK_CLASS)) == 0
    
    def next_disabled(self):
        return len(self.driver.find_elements_by_xpath(self.NEXT_TRACK_CLASS)) == 0

    def mute(self):
        self.driver.find_element_by_css_selector(self.MUTE).click()

    def muted(self):
        return len(self.driver.find_elements_by_xpath(self.MUTE_XPATH)) == 0

    def hidden(self):
        return len(self.driver.find_elements_by_xpath(self.PLAYER)) == 0

    def get_playing_track_id(self):
        id = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.TRACK_LIKE).get_attribute('data-id')
        )
        return id

    def prev_track(self):
        prev = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PREV_TRACK)
        )
        prev.click()

    def next_track(self):
        next = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NEXT_TRACK)
        )
        next.click()

    def toggle_play(self):
        pause = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PLAY)
        )
        pause.click()


class Albums(Component):
    FIRST_ALBUM = '//div[@class="top-album"]'
    TITLE = '//div[@class="top-album__title"]'
    ARTIST = '//div[@class="top-album__artist"]'
    PLAY_ICON = 'i[class^=top-album__play]'
    ALBUM_LABEL = '//div[@class="album__description-label"]'

    def open_first_album(self):
        self.driver.find_element_by_xpath(self.FIRST_ALBUM).click()
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ALBUM_LABEL).text == 'album'
        )

    def get_first_album_id(self):
        id = self.driver.find_element_by_css_selector(
            self.PLAY_ICON).get_attribute('data-id')
        return id

    def play_first_album(self):
        play = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PLAY_ICON)
        )
        play.click()
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(
                Player.CURRENT_TIME).text == '0:01'
        )


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
    PLAY = '//img[@class="track-play"]'
    PLAYLIST = '//img[@class="track-list-item-playlist"]'
    PLAYLISTS_MENU = '//div[@class="menu"]'
    FIRST_TRACK_ARTIST = '//div[@class="track__container__artist"]'

    def get_track_artist(self, i=0):
        artist = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_elements_by_xpath(self.FIRST_TRACK_ARTIST)[i].text
        )
        return artist

    def play_track(self, i=0, last=False):
        play = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_elements_by_xpath(self.PLAY)
        )
        if last:
            i = len(play) - 1
        play[i].click()

    def get_track_id(self, i=0):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_elements_by_xpath(
                self.PLAY)[i].get_attribute('data-id')
        )

    def open_first_add_to_playlist(self):
        playlist = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PLAYLIST)
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
