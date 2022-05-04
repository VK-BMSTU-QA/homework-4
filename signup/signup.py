import time

from selenium import webdriver
import unittest
from random_username.generate import generate_username
from signin.page import SignInPage
from profile.page import ProfilePage
from signup.page import SignUpPage
from navbar.page import NavbarPage

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

    def test_signup_positive(self):
        driver = self.driver
        driver.get(url=url)
        element_login = self.signupPage.get_login_element()
        element_login.send_keys(LOGIN)

        element_email = self.signupPage.get_email_element()
        element_email.send_keys(EMAIL)

        element_password = self.signupPage.get_password_element()
        element_password.send_keys(PASSWORD)

        element_password_repeat = self.signupPage.get_password_confirm_element()
        element_password_repeat.send_keys(PASSWORD_CONFIRM)

        element_button = self.signupPage.get_button_element()
        element_button.click()

        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

        profile_link = self.navbarPage.get_profile_link()
        profile_link.click()

        user_name = self.profilePage.get_username_element()
        self.assertEqual(LOGIN, user_name.text)

    def test_signup_empty_field(self):
        driver = self.driver
        driver.get(url=url)

        element_login = self.signupPage.get_login_element()
        element_login.send_keys(LOGIN)

        element_button = self.signupPage.get_button_element()
        element_button.click()

        error = self.signupPage.get_error_element()
        self.assertEqual(error.text, 'Заполните все поля')

    def test_signup_user_exists(self):
        driver = self.driver
        driver.get(url=url)
        element_login = self.signupPage.get_login_element()
        element_login.send_keys(LOGIN_USER_EXISTS)

        element_email = self.signupPage.get_email_element()
        element_email.send_keys(EMAIL)

        element_password = self.signupPage.get_password_element()
        element_password.send_keys(PASSWORD)

        element_password_repeat = self.signupPage.get_password_confirm_element()
        element_password_repeat.send_keys(PASSWORD_CONFIRM)

        element_button = self.signupPage.get_button_element()
        element_button.click()

        error = self.signupPage.get_error_element()
        self.assertEqual(error.text, 'Пользователь уже существует')

    def test_signup_passwords_not_match(self):
        driver = self.driver
        driver.get(url=url)
        element_login = self.signupPage.get_login_element()
        element_login.send_keys(LOGIN_USER_EXISTS)

        element_email = self.signupPage.get_email_element()
        element_email.send_keys(EMAIL)

        element_password = self.signupPage.get_password_element()
        element_password.send_keys(PASSWORD)

        element_password_repeat = self.signupPage.get_password_confirm_element()
        element_password_repeat.send_keys(PASSWORD_CONFIRM_NOT_MATCH)

        element_button = self.signupPage.get_button_element()
        element_button.click()

        error = self.signupPage.get_error_element()
        self.assertEqual(error.text, 'Пароли не одинаковые')

    def test_signup_wrong_email_wrong(self):
        driver = self.driver
        driver.get(url=url)
        element_login = self.signupPage.get_login_element()
        element_login.send_keys(LOGIN_USER_EXISTS)

        element_email = self.signupPage.get_email_element()
        element_email.send_keys(EMAIL_WRONG)

        element_password = self.signupPage.get_password_element()
        element_password.send_keys(PASSWORD)

        element_password_repeat = self.signupPage.get_password_confirm_element()
        element_password_repeat.send_keys(PASSWORD_CONFIRM)

        element_button = self.signupPage.get_button_element()
        element_button.click()

        error = self.signupPage.get_error_element()
        self.assertEqual(error.text, 'Неправильный формат данных')

    def test_signup_redirect_to_signin(self):
        driver = self.driver
        driver.get(url=url)
        element_signup_link = self.signupPage.get_signin_link()
        element_signup_link.click()

        signin_title = self.signinPage.get_signin_title()
        self.assertEqual(signin_title.text, 'Вход')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
