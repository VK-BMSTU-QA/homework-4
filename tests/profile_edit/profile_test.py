import os

from page_objects.login import LoginPage
from page_objects.profile_page import ProfilePage
from tests.profile_edit.base import BaseProfileTest


class ProfileTest(BaseProfileTest):
    def __init__(self, methodName: str = ...):
        super(ProfileTest, self).__init__(methodName)

    def setUp(self):
        super().setUp()
        self.loginPage = LoginPage(self.driver)
        self.profilePage = ProfilePage(self.driver)

    def tearDown(self):
        super().tearDown()

    def test_change_password_fail(self):
        exp_err = 'Проверьте правильность заполнения полей'
        self.loginPage.open()
        self.loginPage.login(self.EMAIL, self.PASSWORD)
        self.profilePage.go_to_switch_password()
        self.profilePage.click_button_change_password()

        res = self.profilePage.get_validation_err()
        self.assertNotEqual(res, exp_err)

