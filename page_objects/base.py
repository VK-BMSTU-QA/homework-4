import urlparse


class Page(object):
    BASE_URL = 'http://pyaterochka-team.site/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)
