from urllib.parse import urljoin

from selenium.common.exceptions import InvalidSelectorException, StaleElementReferenceException
from selenium.webdriver.support.expected_conditions import element_attribute_to_include


def element_attribute_not_to_include(locator, attribute_):
    """ An expectation for checking if the given attribute is not included in the
    specified element.
    locator, attribute
    """

    def _predicate(driver):
        try:
            element_attribute = driver.find_element(*locator).get_attribute(attribute_)
            return element_attribute is None
        except InvalidSelectorException as e:
            raise e
        except StaleElementReferenceException:
            return False

    return _predicate


class Page:
    BASE_URL = 'https://lostpointer.site/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class Component:
    def __init__(self, driver):
        self.driver = driver
