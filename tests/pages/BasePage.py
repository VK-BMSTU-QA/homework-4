from lib2to3.pgen2 import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from ..urls import Urls

class BasePage(Urls):
    driver = None

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver
    
    def wait_render(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def wait_visible(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_redirect(self, url, timeout=60):
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))

    def wait_any_redirect(self, timeout=60):
        return WebDriverWait(self.driver, timeout).until(EC.url_changes('some'))

    def is_exist(self, selector):
        try:
            self.wait_visible(selector, 3)
        except TimeoutException:
            return False
        return True

    def fill_input(self, selector, text):
        text_input = self.wait_render(selector)
        text_input.send_keys(text)

    def wait_click(self, selector):
        elem = self.wait_render(selector)
        elem.click()