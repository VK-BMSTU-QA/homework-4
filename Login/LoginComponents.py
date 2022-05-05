import selenium.common.exceptions

from Base.BaseComponent import Component
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.utils import CHECK_FREQ, TIMEOUT


class LoginForm(Component):
    EMAIL = '//input[@name="email"]'
    PASSWORD = '//input[@name="password"]'
    LOGIN_BUTTON = '//input[@class="auth-form__submit"]'
    FRONTEND_ERRORS = '//div[@class="auth-form__invalidities form__invalidities"]'
    BACKEND_ERRORS_CLS = "auth-form__fail_msg"
    AVATAR = "avatar__img"

    def set_email(self, email):
        input = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.EMAIL)
        )
        input.send_keys(email)

    def set_password(self, password):
        input = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.PASSWORD)
        )
        input.send_keys(password)

    def login(self):
        button = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.LOGIN_BUTTON)
        )
        button.click()

    def check_login(self):
        try:
            WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.AVATAR))
            )
        except selenium.common.exceptions.TimeoutException:
            return False
        return True

    def frontend_errors(self):
        warnings = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.FRONTEND_ERRORS)
        )
        return warnings

    def backend_errors(self):
        warnings = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element_by_class_name(self.BACKEND_ERRORS_CLS)
        )
        return warnings
