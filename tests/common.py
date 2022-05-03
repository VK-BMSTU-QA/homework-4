from urllib.parse import urljoin

from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Component:
    def __init__(self, driver):
        self.driver = driver


class Page:
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


def element_attribute_not_to_include(locator, attribute_):
    """ An expectation for checking if the given attribute is not included in the
    specified element.
    locator, attribute
    """

    def _predicate(driver):
        try:
            element_attribute = driver.find_element(
                *locator).get_attribute(attribute_)
            return element_attribute is None
        except InvalidSelectorException as e:
            raise e
        except StaleElementReferenceException:
            return False

    return _predicate


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

    def paused(self):
        play = self.driver.find_element_by_xpath(self.PLAY)
        return 'pause' in play.get_attribute('src')

    def prev_disabled(self):
        return len(self.driver.find_elements_by_xpath(self.PREV_TRACK_CLASS)) == 0

    def next_disabled(self):
        return len(self.driver.find_elements_by_xpath(self.NEXT_TRACK_CLASS)) == 0

    def mute(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.MUTE))
        )
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

    def get_like_btn(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TRACK_LIKE)
        )

    def remove_like(self):
        self.get_like_btn().click()
        WebDriverWait(self.driver, 10).until(
            element_attribute_not_to_include(
                (By.XPATH, self.TRACK_LIKE), "data-in_favorites")
        )

    def add_like(self):
        self.get_like_btn().click()
        WebDriverWait(self.driver, 10).until(
            EC.element_attribute_to_include(
                (By.XPATH, self.TRACK_LIKE), "data-in_favorites")
        )

    def track_is_liked(self):
        return bool(
            self.get_like_btn().get_attribute("data-in_favorites")
        )

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
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.PLAY))
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
    LOGOUT = '//i[@class="topbar-icon js-logout fa-solid fa-right-from-bracket"]'

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

    def log_out(self):
        logout = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOGOUT)
        )
        logout.click()

    def logged_out(self):
        try:
            WebDriverWait(self.driver, 10, 0.1).until(
                lambda d: len(d.find_elements_by_xpath(self.AVATAR)) == 0
            )
        except:
            return False
        return True


class TopArtists(Component):
    FIRST_ARTIST = '//img[@class="suggested-artist__img"]'

    def get_first_artist_id(self):
        return self.driver.find_element_by_xpath(self.FIRST_ARTIST).get_attribute('data-id')


class Sidebar(Component):
    LOGO = '//a[@class="sidebar__icon__logo"]'
    HOME = '//a[@class="sidebar__icon" and @href="/"]'
    FAVORITES = '//a[@class="sidebar__icon" and @href="/favorites"]'

    def go_home_by_logo(self):
        self.driver.find_element_by_xpath(self.LOGO).click()

    def go_favorites(self):
        self.driver.find_element_by_xpath(self.FAVORITES).click()


class Tracks(Component):
    PLAY = '//img[@class="track-play"]'
    PLAYLIST = '//img[@class="track-list-item-playlist"]'
    PLAYLISTS_MENU = '//div[@class="menu"]'
    FIRST_TRACK_ARTIST = '//div[@class="track__container__artist"]'
    FIRST_TRACK_ALBUM = '//img[@class="track__artwork__img"]'
    TRACK_LIKE_BTN = '//img[@class="track-fav" and @data-id="{}"]'

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
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_to_be_clickable(play[i])
        )
        play[i].click()

    def pause_track(self):
        self.play_track()

    def get_track_id(self, i=0):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_elements_by_xpath(
                self.PLAY)[i].get_attribute('data-id')
        )

    def open_first_add_to_playlist(self):
        playlist = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PLAYLIST)
        )
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.PLAYLIST))
        )
        playlist.click()

    def playlist_menu_exists(self):
        return has_element(self.driver, self.PLAYLISTS_MENU)

    def open_first_album(self):
        album = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FIRST_TRACK_ALBUM)
        )
        album.click()

    def open_first_artist(self):
        artist = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FIRST_TRACK_ARTIST)
        )
        artist.click()

    def get_like_btn(self, track_id):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.TRACK_LIKE_BTN.format(track_id))
        )

    def remove_like(self, track_id):
        self.get_like_btn(track_id).click()
        WebDriverWait(self.driver, 10).until(
            element_attribute_not_to_include(
                (By.XPATH, self.TRACK_LIKE_BTN.format(track_id)), "data-in_favorites")
        )

    def add_like(self, track_id):
        self.get_like_btn(track_id).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_attribute_to_include(
                (By.XPATH, self.TRACK_LIKE_BTN.format(track_id)), "data-in_favorites")
        )

    def track_is_liked(self, track_id):
        return bool(
            self.get_like_btn(track_id).get_attribute("data-in_favorites")
        )
