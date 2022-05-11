import os
import unittest

from Login.LoginComponents import LoginForm
from Login.LoginPage import LoginPage
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.utils import CHECK_FREQ, TIMEOUT


class LoginTest(unittest.TestCase):
    EMAIL = os.environ["TESTUSERNAME"]
    PASSWORD = os.environ["TESTPASSWORD"]
    WRONG_PASSWORD = "djqowjdl12"

    def setUp(self):
        browser = os.environ.get("TESTBROWSER", "CHROME")
        options = Options()
        options.headless = bool(os.environ.get("HEADLESS", False))
        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            options=options
        )
        self.login_page = LoginPage(self.driver)
        self.login_page.open()
        self.login_form = self.login_page.form

    def tearDown(self):
        self.driver.quit()

    def test_positive(self):
        self.login_form.set_email(self.EMAIL)
        self.login_form.set_password(self.PASSWORD)
        self.assertFalse(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=LoginForm.FRONTEND_ERRORS)
        ).text)
        self.assertFalse(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.CLASS_NAME, value=LoginForm.BACKEND_ERRORS_CLS)
        ).text)

        self.login_form.login()
        self.assertTrue(self.login_form.check_login())

    def test_empty_form(self):
        self.login_form.login()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element_by_class_name(LoginForm.BACKEND_ERRORS_CLS)
        ))

    def test_empty_password(self):
        self.login_form.set_email(self.EMAIL)
        self.login_form.login()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element_by_class_name(LoginForm.BACKEND_ERRORS_CLS)
        ))

    def test_empty_email(self):
        self.login_form.set_password(self.PASSWORD)
        self.login_form.login()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element_by_class_name(LoginForm.BACKEND_ERRORS_CLS)
        ))

    def test_invalid_email(self):
        self.login_form.set_email(self.EMAIL.replace(".", ""))
        self.login_form.set_password(self.PASSWORD)
        self.login_form.login()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=LoginForm.FRONTEND_ERRORS)
        ))

    def test_wrong_credentials(self):
        self.login_form.set_email(self.EMAIL)
        self.login_form.set_password(self.WRONG_PASSWORD)
        self.login_form.login()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element_by_class_name(LoginForm.BACKEND_ERRORS_CLS)
        ))
