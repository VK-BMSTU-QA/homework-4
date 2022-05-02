from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import urljoin

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