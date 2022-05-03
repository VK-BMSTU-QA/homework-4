import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from tests import Page, Component


class LoginPage(Page):
    PATH = 'signin'

    @property
    def form(self):
        return LoginForm(self.driver)


class LoginForm(Component):
    EMAIL = '//input[@name="email"]'
    PASSWORD = '//input[@name="password"]'
    LOGIN_BUTTON = '//input[@class="auth-form__submit"]'
    FRONTEND_WARNINGS = '//div[@class="auth-form__invalidities form__invalidities"]'
    BACKEND_WARNINGS_CLS = 'auth-form__fail_msg'

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

    def login(self):
        button = WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOGIN_BUTTON)
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


class LoginTest(unittest.TestCase):
    EMAIL = os.environ['TESTUSERNAME']
    PASSWORD = os.environ['TESTPASSWORD']
    WRONG_PASSWORD = "djqowjdl12"

    def setUp(self):
        browser = os.environ.get('TESTBROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.login_page = LoginPage(self.driver)
        self.login_page.open()
        self.login_form = self.login_page.form

    def tearDown(self):
        self.driver.quit()

    def test_positive(self):
        self.login_form.set_email(self.EMAIL)
        self.login_form.set_password(self.PASSWORD)

        assert not self.login_form.frontend_warnings().text
        assert not self.login_form.backend_warnings().text

        self.login_form.login()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "avatar__img"))
        )

    def test_empty_form(self):
        self.login_form.login()
        assert self.login_form.backend_warnings()

    def test_empty_password(self):
        self.login_form.set_email(self.EMAIL)
        self.login_form.login()
        assert self.login_form.backend_warnings()

    def test_empty_email(self):
        self.login_form.set_password(self.PASSWORD)
        self.login_form.login()
        assert self.login_form.backend_warnings()

    def test_invalid_email(self):
        self.login_form.set_email(self.EMAIL.replace(".", ""))
        self.login_form.set_password(self.PASSWORD)
        self.login_form.login()
        assert self.login_form.frontend_warnings()

    def test_wrong_credentials(self):
        self.login_form.set_email(self.EMAIL)
        self.login_form.set_password(self.WRONG_PASSWORD)
        self.login_form.login()
        assert self.login_form.backend_warnings()
