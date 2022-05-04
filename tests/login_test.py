import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from Login.LoginPage import LoginPage


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
        self.login_form.check_login()

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
