# -*- coding: utf-8 -*-

import os

import unittest
from urllib.parse import urljoin
import selenium

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Page(object):
    BASE_URL = 'https://lostpointer.site/'
    PATH = 'signin'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class LoginPage(Page):
    PATH = 'signin'

    @property
    def form(self):
        return LoginForm(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver


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
    EMAIL = os.environ['TESTUSERNAME']
    PASSWORD = os.environ['TESTPASSWORD']

    def setUp(self):
        browser = os.environ.get('TESTBROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()


class PositiveLoginTest(LoginTest):
    def test(self):
        login_page = LoginPage(self.driver)
        login_page.open()

        login_form = login_page.form
        login_form.set_email(self.EMAIL)
        login_form.set_password(self.PASSWORD)

        # Отсутсвие ошибок при вводе верных реквизитов
        assert not login_form.frontend_warnings_text()
        assert not login_form.backend_warnings_text()

        login_form.login()

        # Успешный логин при вводе верных реквизитов
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "avatar__img"))
        )


class NegativeLoginTest(LoginTest):
    EMAIL = "test@test.com"
    PASSWORD = "djqowjdl12"

    def test(self):
        login_page = LoginPage(self.driver)
        login_page.open()

        # Ошибка при submit'е пустой формы
        login_form = login_page.form
        login_form.login()
        assert login_form.backend_warnings_text()

        # Ошибка при незаполнении одного из двух полей
        login_form.set_password(self.PASSWORD)
        login_form.login()
        assert login_form.backend_warnings_text()

        # Ошибка при вводе некорректного email-адреса
        login_form.set_email(self.EMAIL.replace(".", ""))
        login_form.login()
        assert login_form.frontend_warnings_text()

        # Ошибка при вводе неверных реквизитов
        login_form.set_email(self.EMAIL)
        login_form.set_password(self.PASSWORD)
        login_form.login()
        assert login_form.backend_warnings_text()
