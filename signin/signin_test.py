import os
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from navbar.page import NavbarPage
from profile.page import ProfilePage
from signup.page import SignUpPage
from .page import SignInPage

url = "https://goodvibesazot.tk/signin"

LOGIN = os.environ.get('LOGIN')
PASSWORD = os.environ.get('PASSWORD')
LOGIN_NO_USER = os.environ.get('LOGIN_NO_USER')
PASSWORD_INCORRECT = os.environ.get('PASSWORD_INCORRECT')
PASSWORD_SHORT = os.environ.get('PASSWORD_SHORT')


class SignIn(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.signinPage = SignInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.signupPage = SignUpPage(self.driver)
        self.navbarPage = NavbarPage(self.driver)

        self.driver.get(url=url)

    def test_signin_positive(self):
        self.signinPage.fill_login(LOGIN)

        self.signinPage.fill_password(PASSWORD)

        self.signinPage.click_button()

        # check authorization
        self.navbarPage.click_profile_icon()
        self.navbarPage.click_profile_link()

        self.assertEqual(LOGIN, self.profilePage.get_username())

    def test_signin_empty_field(self):
        self.signinPage.fill_login(env.LOGIN)

        self.signinPage.click_button()

        self.assertEqual(self.signinPage.wait_error(), 'Заполните все поля')

    def test_signin_no_user(self):
        self.signinPage.fill_login(LOGIN_NO_USER)

        self.signinPage.fill_password(PASSWORD)

        self.signinPage.click_button()

        self.assertEqual(self.signinPage.wait_error(), 'Пользователя не существует')

    def test_signin_incorrect_password(self):
        self.signinPage.fill_login(LOGIN)

        self.signinPage.fill_password(PASSWORD_INCORRECT)

        self.signinPage.click_button()

        self.assertEqual(self.signinPage.wait_error(), 'Неверный пароль')

    def test_signin_short_password(self):
        self.signinPage.fill_login(LOGIN)

        self.signinPage.fill_password(PASSWORD_SHORT)

        self.signinPage.click_button()

        self.assertEqual(self.signinPage.wait_error(), 'Неверный формат пароля')

    def test_signin_redirect_to_signup(self):
        self.signinPage.click_on_signup_link()

        self.assertEqual(self.signupPage.get_signup_title(), 'Создать аккаунт')

    def tearDown(self):
        self.driver.quit()
