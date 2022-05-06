from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import setup.setup as stp


class SeleniumBaseObject(object):
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, stp.TIMEOUT_WAIT, stp.POLL_FREQUENCY)
        self.actions = ActionChains(self.driver)

    def _wait_with_timeout(self, timeout):
        return WebDriverWait(self.driver, timeout, stp.POLL_FREQUENCY)

    def _get_dom_element(self, css_selector):
        return self._wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )

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
        if value != "":
            element.send_keys(value)

    def _get_element(self, css_selector):
        element = self._wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        return element

    def _get_elements(self, css_selector):
        element = self._wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, css_selector))
        )
        return element

    def _check_elem_not_exists(self, css_selector):
        try:
            self._wait_with_timeout(stp.TIMEOUT_DRAWABLE_WAIT).\
                until(EC.invisibility_of_element_located((By.CSS_SELECTOR, css_selector)))
        except TimeoutException:
            return False
        return True

    def _check_drawable(self, css_selector):
        try:
            elem = self._wait_with_timeout(stp.TIMEOUT_DRAWABLE_WAIT).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
            )
        except TimeoutException:
            return False
        return True

    def _check_disappear(self, css_selector):
        try:
            self._wait_with_timeout(stp.TIMEOUT_DRAWABLE_WAIT).until(
                EC.invisibility_of_element((By.CSS_SELECTOR, css_selector))
            )
        except TimeoutException:
            return False
        return True
