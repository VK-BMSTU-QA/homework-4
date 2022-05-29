import time

from selenium import webdriver

from navbar.page import NavbarPage
from .page import SignInPage
from profile.page import ProfilePage
from signup.page import SignUpPage
from signin.utils import TestUtils

import unittest

url = "https://goodvibesazot.tk/signin"

LOGIN = '12345'
PASSWORD = '12345'
LOGIN_NO_USER = 'adasdasdasd'
PASSWORD_INCORRECT = 'sdfsdfsdfsf'
PASSWORD_SHORT = '123'


class SignIn(unittest.TestCase):
    def setUp(self):
        # EXE_PATH = r'C:\chromedriver.exe'
        # self.driver = webdriver.Chrome(executable_path=EXE_PATH)
        self.driver = webdriver.Chrome()
        self.signinPage = SignInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.signupPage = SignUpPage(self.driver)
        self.navbarPage = NavbarPage(self.driver)
        self.testUtils = TestUtils(driver=self.driver)
        self.driver.get(url=url)

    def test_signin_positive(self):
        self.testUtils.fill_login(LOGIN)

        self.testUtils.fill_password(PASSWORD)

        self.testUtils.click_button()

        self.testUtils.check_authorization()

        user_name = self.testUtils.check_authorization()
        self.assertEqual(LOGIN, user_name)

    def test_signin_empty_field(self):
        self.testUtils.fill_login(LOGIN)

        self.testUtils.click_button()

        error = self.testUtils.wait_error()
        self.assertEqual(error, 'Заполните все поля')

    def test_signin_no_user(self):
        self.testUtils.fill_login(LOGIN_NO_USER)

        self.testUtils.fill_password(PASSWORD)

        self.testUtils.click_button()

        error = self.testUtils.wait_error()
        self.assertEqual(error, 'Пользователя не существует')

    def test_signin_incorrect_password(self):
        self.testUtils.fill_login(LOGIN)

        self.testUtils.fill_password(PASSWORD_INCORRECT)

        self.testUtils.click_button()

        error = self.testUtils.wait_error()
        self.assertEqual(error, 'Неверный пароль')

    def test_signin_short_password(self):
        self.testUtils.fill_login(LOGIN)

        self.testUtils.fill_password(PASSWORD_SHORT)

        self.testUtils.click_button()

        error = self.testUtils.wait_error()
        self.assertEqual(error, 'Неверный формат пароля')

    def test_signin_redirect_to_signup(self):
        self.testUtils.click_on_signup_link()

        signup_title = self.testUtils.check_signup_redirect()
        self.assertEqual(signup_title, 'Создать аккаунт')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
