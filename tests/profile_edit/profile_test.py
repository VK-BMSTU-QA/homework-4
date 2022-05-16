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

    def recover_change_password(self, cur_password):
        self.profilePage.go_to_switch_password()
        fields = self.profilePage.get_password_fields()
        self.profilePage.set_new_password(fields, cur_password, self.PASSWORD)
        self.profilePage.click_button_change_password()
        self.loginPage.logout()


    def recover_change_avatar(self):
        self.profilePage.redirect_to_profile_settings()
        field = self.profilePage.get_avatar_input()
        self.profilePage.set_new_avatar(field, self.ROOT + self.profilePage.DEFAULT_AVATAR)


    def test_change_password_on_empty_fail(self):
        self.loginPage.open()
        self.loginPage.login(self.EMAIL, self.PASSWORD)
        self.profilePage.go_to_switch_password()
        self.profilePage.click_button_change_password()

        res = self.profilePage.get_validation_err()
        self.assertTrue(res)

    def test_change_password_on_valid(self):
        new_password = "qwerty"
        self.loginPage.open()
        self.loginPage.login(self.EMAIL, self.PASSWORD)
        self.profilePage.go_to_switch_password()
        fields = self.profilePage.get_password_fields()
        self.profilePage.set_new_password(fields, self.PASSWORD, new_password)
        self.profilePage.click_button_change_password()
        self.loginPage.logout()

        self.loginPage.login(self.EMAIL, new_password)
        self.recover_change_password(new_password)

    def test_change_avatar(self):
        new_img_path = self.ROOT+"/files/profile_avatar.png"

        self.loginPage.open()
        self.loginPage.login(self.EMAIL, self.PASSWORD)
        self.profilePage.go_to_profile_settings()
        old_name = self.profilePage.get_avatar_filename().get_attribute("style")
        avatar_input = self.profilePage.get_avatar_input()
        self.profilePage.set_new_avatar(avatar_input, new_img_path)
        self.profilePage.wait_update_avatar()
        new_name = self.profilePage.get_avatar_filename().get_attribute("style")
        self.recover_change_avatar()
        self.assertNotEqual(old_name, new_name)

    def test_change_avatar_invalid_file(self):
        new_img_path = self.ROOT+"/files/not_image"

        self.loginPage.open()
        self.loginPage.login(self.EMAIL, self.PASSWORD)
        self.profilePage.go_to_profile_settings()
        avatar_input = self.profilePage.get_avatar_input()
        old_name = self.profilePage.get_avatar_filename().get_attribute("style")
        self.profilePage.set_new_avatar(avatar_input, new_img_path)

        new_name = self.profilePage.get_avatar_filename().get_attribute("style")
        self.assertEqual(old_name, new_name)

