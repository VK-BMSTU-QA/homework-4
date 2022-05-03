from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ..urls import *


class BasePage(Urls):
    # блок ключевых элементов
    login_btn = '#login'
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    def wait_visible(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout, ignored_exceptions=self.ignored_exceptions).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_render(self, selector, timeout=10):
        elem = self.wait_visible(selector)
        return WebDriverWait(self.driver, timeout, ignored_exceptions=self.ignored_exceptions).until(
            EC.element_to_be_clickable(elem))
