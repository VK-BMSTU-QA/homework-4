from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base import Component
from page_objects.base import Page


class LoginPage(Page):
    BASE_URL = 'http://pyaterochka-team.site/'
    PATH = 'signin'

    USERNAME = 'input[type="email"]'
    PASSWORD = 'input[type="password"]'
    SUBMIT = 'button[class="btn btn_primary btn_rounded"]'
    EMAIL_HEADER = '.profile-card__username'
    INVALID_LOGIN_OR_PASSWORD = '.error'
    BTN_OPEN_NAVBAR = '.navbar__profile-name'
    BTN_LOGOUT_NAVBAR = '.navbar__popup > a[router-go="/logout"]'
    PAGE_NAME = '.auth-block > h1[key="null"]'

    def __init__(self, driver):
        super().__init__(driver)

    def fill_login(self, login):
        element = self._wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.USERNAME))
        )
        element.clear()
        element.send_keys(login)

    def fill_password(self, password):
        pswd_elem = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.PASSWORD))
        )
        pswd_elem.send_keys(password)

    def submit(self):
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.SUBMIT))
        )
        submit.click()

    def login(self, login, password):
        self.fill_login(login)
        self.fill_password(password)
        self.submit()

