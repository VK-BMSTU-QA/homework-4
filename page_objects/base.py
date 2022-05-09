import urllib.parse as urlparse

from selenium_utils.utils_object import SeleniumBaseObject

import setup.setup as stp


class Page(SeleniumBaseObject):
    PATH = ''

    def open(self):
        url = urlparse.urljoin(stp.BASE_URL, self.PATH)
        self.driver.get(url)

        self.driver.maximize_window()

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)
