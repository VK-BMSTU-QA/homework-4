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

    def _get_element_by_xpath(self, x_path):
        element = self._wait.until(
            EC.visibility_of_element_located((By.XPATH, x_path))
        )
        return element

    def _get_input(self, css_selector):
        element = self._wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
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

    def _check_disappear_by_xpath(self, x_path):
        try:
            self._wait_with_timeout(stp.TIMEOUT_DRAWABLE_WAIT).until(
                EC.invisibility_of_element((By.XPATH, x_path))
            )
        except TimeoutException:
            return False

        return True

    def _check_request_errors(self, end_of_url):
        is_error = False
        for request in self.driver.requests:
            end_req_url = str.split(request.url, "/")[-1]
            if request.response and end_req_url == end_of_url:
                first_symbol = str(request.response.status_code)[0]
                if first_symbol != "2" or first_symbol != "3":
                   is_error = True

        return is_error
    def _check_current_url(self, desired_url):
        try:
            self._wait_with_timeout(stp.TIMEOUT_WAIT).until(
                EC.url_changes(desired_url)
            )
        except TimeoutException:
            return False
        return True

    def _go_to_previous_page(self):
        self.driver.back()
