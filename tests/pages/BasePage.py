from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

from ..urls import Urls


class BasePage(Urls):
    driver = None
    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver
        self.driver.implicitly_wait(10)

    def wait_render(self, selector, timeout=10):
        elem = self.wait_visible(selector)
        return WebDriverWait(self.driver, timeout, ignored_exceptions=self.ignored_exceptions).until(EC.element_to_be_clickable(elem))

    def wait_visible(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout, ignored_exceptions=self.ignored_exceptions).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_redirect(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout, ignored_exceptions=self.ignored_exceptions).until(EC.url_matches(url))

    def wait_any_redirect(self, url='some', timeout=10):
        return WebDriverWait(self.driver, timeout, ignored_exceptions=self.ignored_exceptions).until(EC.url_contains(url))

    def wait_until_innerhtml_changes_after_click(self, selector, timeout=10):
        elem = self.wait_render(selector)
        first_text = elem.get_attribute('innerHTML')
        self.wait_click(selector)
        WebDriverWait(self.driver, timeout, ignored_exceptions=self.ignored_exceptions).until(EC.none_of(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, selector), first_text)
        ))

    def wait_until_text_in_attribute(self, selector, attribute, value, timeout=10):
        try:
            WebDriverWait(self.driver, timeout, ignored_exceptions=self.ignored_exceptions).until(EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, selector), attribute, value))
        except TimeoutException:
            return False
        return True

    def wait_for_delete(self, elem, timeout=10):
        return WebDriverWait(self.driver, timeout, ignored_exceptions=self.ignored_exceptions).until(EC.staleness_of(elem))

    def is_exist(self, selector):
        try:
            self.wait_visible(selector, 1)
        except TimeoutException:
            return False
        return True

    def fill_input(self, selector, text):
        text_input = self.wait_render(selector)
        text_input.send_keys(text)

    def wait_click(self, selector):
        elem = self.wait_render(selector)
        elem.click()

    def get_innerhtml(self, selector):
        return self.wait_render(selector).get_attribute('innerHTML')
