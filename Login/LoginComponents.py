from Base.BaseComponent import Component
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginForm(Component):
    EMAIL = '//input[@name="email"]'
    PASSWORD = '//input[@name="password"]'
    LOGIN_BUTTON = '//input[@class="auth-form__submit"]'
    FRONTEND_WARNINGS = '//div[@class="auth-form__invalidities form__invalidities"]'
    BACKEND_WARNINGS_CLS = "auth-form__fail_msg"

    def set_email(self, email):
        input = WebDriverWait(self.driver, 10, 0.1).until(lambda d: d.find_element_by_xpath(self.EMAIL))
        input.send_keys(email)

    def set_password(self, password):
        input = WebDriverWait(self.driver, 10, 0.1).until(lambda d: d.find_element_by_xpath(self.PASSWORD))
        input.send_keys(password)

    def login(self):
        button = WebDriverWait(self.driver, 10, 0.1).until(lambda d: d.find_element_by_xpath(self.LOGIN_BUTTON))
        button.click()

    def check_login(self):
        WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, "avatar__img")))

    def frontend_warnings(self):
        warnings = WebDriverWait(self.driver, 10, 0.1).until(lambda d: d.find_element_by_xpath(self.FRONTEND_WARNINGS))
        return warnings

    def backend_warnings(self):
        warnings = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_class_name(self.BACKEND_WARNINGS_CLS)
        )
        return warnings
