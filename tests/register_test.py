import os
import random
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from tests import Page, Component


class RegisterPage(Page):
    PATH = 'signup'

    @property
    def form(self):
        return RegisterForm(self.driver)


class RegisterForm(Component):
    NICKNAME = '//input[@name="nickname"]'
    EMAIL = '//input[@name="email"]'
    PASSWORD = '//input[@name="password"]'
    CONFIRM_PASSWORD = '//input[@name="confirm_password"]'
    REGISTER_BUTTON = '//input[@class="auth-form__submit"]'
    FRONTEND_WARNINGS = '//div[@class="auth-form__invalidities"]'
    BACKEND_WARNINGS_CLS = 'auth-form__fail_msg'

    def set_nickname(self, nickname):
        input = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NICKNAME)
        )
        input.send_keys(nickname)

    def set_email(self, email):
        input = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EMAIL)
        )
        input.send_keys(email)

    def set_password(self, password):
        input = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PASSWORD)
        )
        input.send_keys(password)

    def set_confirm_password(self, password):
        input = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CONFIRM_PASSWORD)
        )
        input.send_keys(password)

    def register(self):
        button = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.REGISTER_BUTTON)
        )
        button.click()

    def frontend_warnings(self):
        warnings = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FRONTEND_WARNINGS)
        )
        return warnings

    def backend_warnings(self):
        warnings = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_class_name(self.BACKEND_WARNINGS_CLS)
        )
        return warnings


class RegisterTest(unittest.TestCase):
    NICKNAME = "test_{}".format(random.randint(0, 1000))
    EMAIL = "test{}@test.com".format(random.randint(0, 1000))
    SHORT_PASSWORD = "123"
    PASSWORD = "djqowjdl12"

    def setUp(self):
        browser = os.environ.get('TESTBROWSER', 'CHROME')
        options = Options()
        options.headless = bool(os.environ.get('HEADLESS', False))
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            options=options
        )
        self.register_page = RegisterPage(self.driver)
        self.register_page.open()
        self.register_form = self.register_page.form

    def tearDown(self):
        self.driver.quit()

    def positive_test(self):
        self.register_form.set_nickname(self.NICKNAME)
        self.register_form.set_email(self.EMAIL)
        self.register_form.set_password(self.PASSWORD)
        self.register_form.set_confirm_password(self.PASSWORD)

        assert not self.register_form.frontend_warnings().text
        assert not self.register_form.backend_warnings().text

        self.register_form.register()

        WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "avatar__img"))
        )

    def test_empty_form(self):
        self.register_form.register()
        assert self.register_form.backend_warnings()

    def test_empty_password(self):
        self.register_form.set_email(self.EMAIL)
        self.register_form.register()
        assert self.register_form.backend_warnings()

    def test_empty_email(self):
        self.register_form.set_password(self.PASSWORD)
        self.register_form.register()
        assert self.register_form.backend_warnings()

    def test_invalid_email(self):
        self.register_form.set_email(self.EMAIL.replace(".", ""))
        self.register_form.set_password(self.PASSWORD)
        self.register_form.register()
        assert self.register_form.frontend_warnings()

    def test_invalid_password(self):
        self.register_form.set_email(self.EMAIL)
        self.register_form.set_password(self.SHORT_PASSWORD)
        self.register_form.set_confirm_password(self.SHORT_PASSWORD)
        self.register_form.register()
        assert self.register_form.frontend_warnings()

    def test_non_similar_passwords(self):
        self.register_form.set_password(self.PASSWORD)
        self.register_form.register()
        assert self.register_form.frontend_warnings()
