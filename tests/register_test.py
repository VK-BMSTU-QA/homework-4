import os
import random
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
    BACKEND_WARNINGS = 'auth-form__fail_msg'

    def set_nickname(self, nickname):
        self.driver.find_element_by_xpath(self.NICKNAME).send_keys(nickname)

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.EMAIL).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def set_confirm_password(self, password):
        self.driver.find_element_by_xpath(self.CONFIRM_PASSWORD).send_keys(password)

    def register(self):
        self.driver.find_element_by_xpath(self.REGISTER_BUTTON).click()

    def frontend_warnings_text(self):
        warnings = self.driver.find_element_by_xpath(self.FRONTEND_WARNINGS)
        return warnings.text

    def backend_warnings_text(self):
        warnings = self.driver.find_element_by_class_name(self.BACKEND_WARNINGS)
        return warnings.text


class RegisterTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TESTBROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        self.register_page = RegisterPage(self.driver)
        self.register_page.open()
        self.register_form = self.register_page.form


class PositiveRegisterTest(RegisterTest):
    NICKNAME = "test_{}".format(random.randint(0, 1000))
    EMAIL = "test{}@test.com".format(random.randint(0, 1000))
    PASSWORD = "djqowjdl12"

    def test(self):
        super().test()

        # Отсутствие ошибок при вводе верных реквизитов
        self.register_form.set_nickname(self.NICKNAME)
        self.register_form.set_email(self.EMAIL)
        self.register_form.set_password(self.PASSWORD)
        self.register_form.set_confirm_password(self.PASSWORD)

        assert not self.register_form.frontend_warnings_text()
        assert not self.register_form.backend_warnings_text()

        self.register_form.register()

        # Успешная регистрация при вводе верных реквизитов
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "avatar__img"))
        )


class NegativeRegisterTest(RegisterTest):
    NICKNAME = "test_nickname"
    EMAIL = "test@test.com"
    SHORT_PASSWORD = "123"
    PASSWORD = "djqowjdl12"

    def test(self):
        super().test()

        # Ошибка при submit'е пустой формы
        self.register_form.register()
        assert self.register_form.backend_warnings_text()

        self.register_form.set_nickname(self.NICKNAME)

        # Ошибка при вводе некорректного email-адреса
        self.register_form.set_email(self.EMAIL.replace(".", ""))
        self.register_form.register()
        assert self.register_form.frontend_warnings_text()

        # Ошибка при вводе пароля короче 8 символов
        self.register_form.set_email(self.EMAIL)
        self.register_form.set_password(self.SHORT_PASSWORD)
        self.register_form.set_confirm_password(self.SHORT_PASSWORD)
        self.register_form.register()
        assert self.register_form.frontend_warnings_text()

        # Ошибка при вводе несовпадающих паролей
        self.register_form.set_password(self.PASSWORD)
        self.register_form.register()
        assert self.register_form.frontend_warnings_text()
