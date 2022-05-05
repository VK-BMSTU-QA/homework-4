import unittest

from page_objects.login import LoginPage


class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def login_simple_ok(self, test):
        auth_page = LoginPage(test.driver)
        auth_page.open()
        auth_page.fill_login(test.EMAIL)
        auth_page.fill_password(test.PASSWORD)
        auth_page.submit()
