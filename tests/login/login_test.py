import os

from setup.default_setup import default_setup
from tests.login.base import BaseLoginTest


class LoginTest(BaseLoginTest):
    def __init__(self, methodName: str = ...):
        super(LoginTest, self).__init__(methodName)

    def setUp(self):
        super().setUp()
        default_setup(self)

    def tearDown(self):
        super().tearDown()

    def test_success_login(self):
        self.loginPage.open()
        self.loginPage.login(self.EMAIL, self.PASSWORD)

        receive = self.loginPage.get_email().text
        expected = self.EMAIL.split("@")[0]
        self.assertEqual(receive, expected)

    def test_empty_login_form(self):
        exp_err = 'Введите логин и пароль';
        self.loginPage.open()
        self.loginPage.login("", "")

        self.assertEqual(self.loginPage.get_error().text, exp_err)
