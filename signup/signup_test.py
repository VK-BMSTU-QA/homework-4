import os
import unittest

from random_username.generate import generate_username
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from navbar.page import NavbarPage
from profile.page import ProfilePage
from signin.page import SignInPage
from signup.page import SignUpPage

url = "https://goodvibesazot.tk/signup"

LOGIN = generate_username(1)[0]
LOGIN_USER_EXISTS = os.environ.get('LOGIN_USER_EXISTS')
EMAIL = os.environ.get('EMAIL')
EMAIL_WRONG = os.environ.get('EMAIL_WRONG')
PASSWORD = os.environ.get('PASSWORD')
PASSWORD_CONFIRM = os.environ.get('PASSWORD_CONFIRM')
PASSWORD_CONFIRM_NOT_MATCH = os.environ.get('PASSWORD_CONFIRM_NOT_MATCH')


class Signup(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.signinPage = SignInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.signupPage = SignUpPage(self.driver)
        self.navbarPage = NavbarPage(self.driver)

        self.driver.get(url=url)

    def test_signup_positive(self):
        self.signupPage.fill_login(LOGIN)

        self.signupPage.fill_email(EMAIL)

        self.signupPage.fill_password(PASSWORD)

        self.signupPage.fill_password_confirm(PASSWORD_CONFIRM)

        self.signupPage.click_submit_button()

        # check authorization
        self.navbarPage.click_profile_icon()
        self.navbarPage.click_profile_link()

        self.assertEqual(LOGIN, self.profilePage.get_username())

    def test_signup_empty_field(self):
        self.signupPage.fill_login(LOGIN)

        self.signupPage.click_submit_button()

        self.assertEqual(self.signupPage.wait_error(), 'Заполните все поля')

    def test_signup_user_exists(self):
        self.signupPage.fill_login(LOGIN_USER_EXISTS)

        self.signupPage.fill_email(EMAIL)

        self.signupPage.fill_password(PASSWORD)

        self.signupPage.fill_password_confirm(PASSWORD_CONFIRM)

        self.signupPage.click_submit_button()

        self.assertEqual(self.signupPage.wait_error(), 'Пользователь уже существует')

    def test_signup_passwords_not_match(self):
        self.signupPage.fill_login(LOGIN)

        self.signupPage.fill_email(EMAIL)

        self.signupPage.fill_password(PASSWORD)

        self.signupPage.fill_password_confirm(PASSWORD_CONFIRM_NOT_MATCH)

        self.signupPage.click_submit_button()

        self.assertEqual(self.signupPage.wait_error(), 'Пароли не одинаковые')

    def test_signup_wrong_email(self):
        self.signupPage.fill_login(LOGIN)

        self.signupPage.fill_email(EMAIL_WRONG)

        self.signupPage.fill_password(PASSWORD)

        self.signupPage.fill_password_confirm(PASSWORD)

        self.signupPage.click_submit_button()

        self.assertEqual(self.signupPage.wait_error(), 'Неправильный формат данных')

    def test_signup_redirect_to_signin(self):
        self.signupPage.click_on_signin_link()

        self.assertEqual(self.signinPage.get_signin_title(), 'Вход')

    def tearDown(self):
        self.driver.quit()
