import time

from selenium import webdriver
import unittest
from random_username.generate import generate_username
from signin.page import SignInPage
from profile.page import ProfilePage
from signup.page import SignUpPage
from navbar.page import NavbarPage
from signup.utils import TestUtils

url = "https://goodvibesazot.tk/signup"

LOGIN = generate_username(1)[0]
LOGIN_USER_EXISTS = '12345'
EMAIL = LOGIN + '@mail.ru'
EMAIL_WRONG = LOGIN + '@mailu'
PASSWORD = '12345'
PASSWORD_CONFIRM = '12345'
PASSWORD_CONFIRM_NOT_MATCH = '12346'


class Signup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.signinPage = SignInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.signupPage = SignUpPage(self.driver)
        self.navbarPage = NavbarPage(self.driver)
        self.testUtils = TestUtils(driver=self.driver)
        self.driver.get(url=url)

    def test_signup_positive(self):
        self.testUtils.fill_login(LOGIN)

        self.testUtils.fill_email(EMAIL)

        self.testUtils.fill_password(PASSWORD)

        self.testUtils.fill_password_confirm(PASSWORD_CONFIRM)

        self.testUtils.click_button()

        user_name = self.testUtils.check_authorization()
        self.assertEqual(LOGIN, user_name)

    def test_signup_empty_field(self):
        self.testUtils.fill_login(LOGIN)

        self.testUtils.click_button()

        error = self.testUtils.wait_error()
        self.assertEqual(error, 'Заполните все поля')

    def test_signup_user_exists(self):
        self.testUtils.fill_login(LOGIN)

        self.testUtils.fill_email(EMAIL)

        self.testUtils.fill_password(PASSWORD)

        self.testUtils.fill_password_confirm(PASSWORD_CONFIRM)

        self.testUtils.click_button()

        error = self.testUtils.wait_error()
        self.assertEqual(error, 'Пользователь уже существует')

    def test_signup_passwords_not_match(self):
        self.testUtils.fill_login(LOGIN)

        self.testUtils.fill_email(EMAIL)

        self.testUtils.fill_password(PASSWORD)

        self.testUtils.fill_password_confirm(PASSWORD_CONFIRM_NOT_MATCH)

        self.testUtils.click_button()

        error = self.testUtils.wait_error()
        self.assertEqual(error, 'Пароли не одинаковые')

    def test_signup_wrong_email_wrong(self):
        self.testUtils.fill_login(LOGIN)

        self.testUtils.fill_email(EMAIL_WRONG)

        self.testUtils.fill_password(PASSWORD)

        self.testUtils.fill_password_confirm(PASSWORD)

        self.testUtils.click_button()

        error = self.testUtils.wait_error()
        self.assertEqual(error, 'Неправильный формат данных')

    def test_signup_redirect_to_signin(self):
        self.testUtils.click_on_signin_link()

        signin_title = self.testUtils.check_signup_redirect()
        self.assertEqual(signin_title, 'Вход')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
