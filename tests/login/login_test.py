import os

from page_objects.login import LoginPage
from setup.default_setup import default_setup
from tests.login.base import BaseLoginTest


class LoginTest(BaseLoginTest):
    def __init__(self, methodName: str = ...):
        super(LoginTest, self).__init__(methodName)

    def setUp(self):
        super().setUp()
        self.loginPage = LoginPage(self.driver)

    def tearDown(self):
        super().tearDown()

    def test_success_login(self):
        self.loginPage.open()
        self.loginPage.login(self.EMAIL, self.PASSWORD)

        receive = self.loginPage.get_email().text
        expected = self.EMAIL.split("@")[0]
        self.assertEqual(receive, expected)
        self.loginPage.logout()

    def test_empty_login_form(self):
        self.loginPage.open()
        self.loginPage.login("", "")

        self.assertTrue(self.loginPage.get_error())
