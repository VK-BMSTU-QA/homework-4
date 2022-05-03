# -*- coding: utf-8 -*-

import os

import unittest
import selenium

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
    BACKEND_WARNINGS = 'auth-form__fail_msg'

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.EMAIL).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def login(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def frontend_warnings_text(self):
        warnings = self.driver.find_element_by_xpath(self.FRONTEND_WARNINGS)
        return warnings.text

    def backend_warnings_text(self):
        warnings = self.driver.find_element_by_class_name(self.BACKEND_WARNINGS)
        return warnings.text


class LoginTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TESTBROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.open()
        self.login_form = self.login_page.form


class PositiveLoginTest(LoginTest):
    EMAIL = os.environ['TESTUSERNAME']
    PASSWORD = os.environ['TESTPASSWORD']

    def test(self):
        super().test()

        self.login_form.set_email(self.EMAIL)
        self.login_form.set_password(self.PASSWORD)

        # Отсутсвие ошибок при вводе верных реквизитов
        assert not self.login_form.frontend_warnings_text()
        assert not self.login_form.backend_warnings_text()

        self.login_form.login()

        # Успешный логин при вводе верных реквизитов
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "avatar__img"))
        )


class NegativeLoginTest(LoginTest):
    EMAIL = "test@test.com"
    PASSWORD = "djqowjdl12"

    def test(self):
        super().test()

        # Ошибка при submit'е пустой формы
        self.login_form.login()
        assert self.login_form.backend_warnings_text()

        # Ошибка при незаполнении одного из двух полей
        self.login_form.set_password(self.PASSWORD)
        self.login_form.login()
        assert self.login_form.backend_warnings_text()

        # Ошибка при вводе некорректного email-адреса
        self.login_form.set_email(self.EMAIL.replace(".", ""))
        self.login_form.login()
        assert self.login_form.frontend_warnings_text()

        # Ошибка при вводе неверных реквизитов
        self.login_form.set_email(self.EMAIL)
        self.login_form.set_password(self.PASSWORD)
        self.login_form.login()
        assert self.login_form.backend_warnings_text()
