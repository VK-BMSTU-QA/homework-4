from selenium import webdriver

from navbar.page import NavbarPage
from .page import SignInPage
from profile.page import ProfilePage
from signup.page import SignUpPage

import unittest

url = "https://goodvibesazot.tk/signin"

LOGIN = '12345'
PASSWORD = '12345'
LOGIN_NO_USER = 'adasdasdasd'
PASSWORD_INCORRECT = 'sdfsdfsdfsf'
PASSWORD_SHORT = '123'


class SignIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.signinPage = SignInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.signupPage = SignUpPage(self.driver)
        self.navbarPage = NavbarPage(self.driver)

    def test_signin_positive(self):
        driver = self.driver
        driver.get(url=url)

        element_login = self.signinPage.get_login_element()
        element_login.send_keys(LOGIN)

        element_password = self.signinPage.get_password_element()
        element_password.send_keys(PASSWORD)

        element_button = self.signinPage.get_button_element()
        element_button.click()

        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

        profile_link = self.navbarPage.get_profile_link()
        profile_link.click()

        user_name = self.profilePage.get_username_element()
        self.assertEqual(LOGIN, user_name.text)

    def test_signin_empty_field(self):
        driver = self.driver
        driver.get(url=url)
        element_login = self.signinPage.get_login_element()
        element_login.send_keys(LOGIN)
        element_button = self.signinPage.get_button_element()
        element_button.click()

        error = self.signinPage.get_error_element()
        self.assertEqual(error.text, 'Заполните все поля')

    def test_signin_no_user(self):
        driver = self.driver
        driver.get(url=url)
        element_login = self.signinPage.get_login_element()
        element_login.send_keys(LOGIN_NO_USER)
        element_password = self.signinPage.get_password_element()
        element_password.send_keys(PASSWORD)
        element_button = self.signinPage.get_button_element()
        element_button.click()

        error = self.signinPage.get_error_element()
        self.assertEqual(error.text, 'Пользователя не существует')

    def test_signin_incorrect_password(self):
        driver = self.driver
        driver.get(url=url)
        element_login = self.signinPage.get_login_element()
        element_login.send_keys(LOGIN)
        element_password = self.signinPage.get_password_element()
        element_password.send_keys(PASSWORD_INCORRECT)
        element_button = self.signinPage.get_button_element()
        element_button.click()

        error = self.signinPage.get_error_element()
        self.assertEqual(error.text, 'Неверный пароль')

    def test_signin_short_password(self):
        driver = self.driver
        driver.get(url=url)
        element_login = self.signinPage.get_login_element()
        element_login.send_keys(LOGIN)
        element_password = self.signinPage.get_password_element()
        element_password.send_keys(PASSWORD_SHORT)
        element_button = self.signinPage.get_button_element()
        element_button.click()

        error = self.signinPage.get_error_element()
        self.assertEqual(error.text, 'Неверный формат пароля')

    def test_signin_redirect_to_signup(self):
        driver = self.driver
        driver.get(url=url)
        element_signup_link = self.signinPage.get_signup_link()
        element_signup_link.click()

        signup_title = self.signupPage.get_signup_title()
        self.assertEqual(signup_title.text, 'Создать аккаунт')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
