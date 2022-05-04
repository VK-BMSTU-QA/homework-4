from Base.BaseComponent import Component
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.utils import has_element


class HomePlaylists(Component):
    PLAYLIST = '//a[@class="pl-link"]'
    PUBLIC_PLAYLISTS_BUTTON = '//div[contains(text(), "Public playlists")]'
    TOP10_PUBLIC_PLAYLIST = '//div[@class="suggested-playlist-name" and contains(text(),"LostPointer top 10")]'
    CREATE_NEW = '//div[@class="suggested-playlist-name" and contains(text(), "Create new...")]'

    def get_first_playlist_href(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element(by=By.XPATH, value=self.PLAYLIST).get_attribute("href")
        )

    def open_first_playlist(self):
        playlist = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element(by=By.XPATH, value=self.PLAYLIST)
        )
        playlist.click()

    def open_public_playlists(self):
        public = WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element(by=By.XPATH, value=self.PUBLIC_PLAYLISTS_BUTTON)
        )
        public.click()

    def get_top10_playlist_exists(self):
        return has_element(self.driver, self.TOP10_PUBLIC_PLAYLIST)

    def create_new_playlist(self):
        create = WebDriverWait(self.driver, 5, 0.1).until(lambda d: d.find_element(by=By.XPATH, value=self.CREATE_NEW))
        create.click()
