from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import setup.setup as stp


class SeleniumBaseObject(object):
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, stp.TIMEOUT_WAIT, stp.POLL_FREQUENCY)

    def _wait_with_timeout(self, timeout):
        return WebDriverWait(self.driver, timeout, stp.POLL_FREQUENCY)

    def _click_button(self, css_selector):
        submit = self._wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        submit.click()

    def _set_text(self, css_selector, value):
        element = self._wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        element.clear()
        element.send_keys(value)

    def _get_element(self, css_selector):
        element = self._wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        return element

    def _check_drawable(self, css_selector):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        except TimeoutException:
            return False
        return True