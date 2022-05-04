from Base.BaseComponent import Component
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.utils import CHECK_FREQ, TIMEOUT


class RegisterForm(Component):
    NICKNAME = '//input[@name="nickname"]'
    EMAIL = '//input[@name="email"]'
    PASSWORD = '//input[@name="password"]'
    CONFIRM_PASSWORD = '//input[@name="confirm_password"]'
    REGISTER_BUTTON = '//input[@class="auth-form__submit"]'
    FRONTEND_WARNINGS = '//div[@class="auth-form__invalidities"]'
    BACKEND_WARNINGS_CLS = "auth-form__fail_msg"

    def set_nickname(self, nickname):
        input = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.NICKNAME)
        )
        input.send_keys(nickname)

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

    def set_confirm_password(self, password):
        input = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.CONFIRM_PASSWORD)
        )
        input.send_keys(password)

    def register(self):
        button = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.REGISTER_BUTTON)
        )
        button.click()

    def check_register(self):
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            EC.presence_of_element_located((By.CLASS_NAME, "avatar__img"))
        )

    def frontend_warnings(self):
        warnings = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.FRONTEND_WARNINGS)
        )
        return warnings

    def backend_warnings(self):
        warnings = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element_by_class_name(self.BACKEND_WARNINGS_CLS)
        )
        return warnings
