import os
import random
import unittest

from Register.RegisterComponents import RegisterForm
from Register.RegisterPage import RegisterPage
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.utils import CHECK_FREQ, TIMEOUT


class RegisterTest(unittest.TestCase):
    NICKNAME = "test_{}".format(random.randint(0, 1000))
    EMAIL = "test{}@test.com".format(random.randint(0, 1000))
    SHORT_PASSWORD = "123"
    PASSWORD = "djqowjdl12"

    def setUp(self):
        browser = os.environ.get("TESTBROWSER", "CHROME")
        options = Options()
        options.headless = bool(os.environ.get("HEADLESS", False))
        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
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

        self.assertFalse(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=RegisterForm.FRONTEND_ERRORS)
        ))
        self.assertFalse(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element_by_class_name(RegisterForm.BACKEND_ERRORS_CLS)
        ))

        self.register_form.register()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.AVATAR))
            ))

    def test_empty_form(self):
        self.register_form.register()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element_by_class_name(RegisterForm.BACKEND_ERRORS_CLS)
        ))

    def test_empty_password(self):
        self.register_form.set_email(self.EMAIL)
        self.register_form.register()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element_by_class_name(RegisterForm.BACKEND_ERRORS_CLS)
        ))

    def test_empty_email(self):
        self.register_form.set_password(self.PASSWORD)
        self.register_form.register()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element_by_class_name(RegisterForm.BACKEND_ERRORS_CLS)
        ))

    def test_invalid_email(self):
        self.register_form.set_email(self.EMAIL.replace(".", ""))
        self.register_form.set_password(self.PASSWORD)
        self.register_form.register()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=RegisterForm.FRONTEND_ERRORS)
        ))

    def test_invalid_password(self):
        self.register_form.set_email(self.EMAIL)
        self.register_form.set_password(self.SHORT_PASSWORD)
        self.register_form.set_confirm_password(self.SHORT_PASSWORD)
        self.register_form.register()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=RegisterForm.FRONTEND_ERRORS)
        ))

    def test_non_similar_passwords(self):
        self.register_form.set_password(self.PASSWORD)
        self.register_form.register()
        self.assertTrue(WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=RegisterForm.FRONTEND_ERRORS)
        ))
