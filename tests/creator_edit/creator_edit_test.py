from page_objects.login import LoginPage
from page_objects.author_settings_page import AuthorSettingsPage
from tests.creator_edit.base import BaseCreatorEditTest



class CreatorEditTest(BaseCreatorEditTest):
    def __init__(self, methodName: str = ...):
        super(CreatorEditTest, self).__init__(methodName)

    def setUp(self):
        super().setUp()
        self.loginPage = LoginPage(self.driver)
        self.authorPage = AuthorSettingsPage(self.driver)

    def tearDown(self):
        super().tearDown()

    def recover_change_avatar(self):
        self.authorPage.redirect_to_profile_settings()
        field = self.authorPage.get_avatar_input()
        self.authorPage.set_new_avatar(field, self.ROOT + self.authorPage.DEFAULT_AVATAR)

    def test_change_avatar(self):
        new_img_path = self.ROOT+"/files/author-avatar.png"

        self.loginPage.open()
        self.loginPage.login(self.EMAIL, self.PASSWORD)
        self.authorPage.go_to_profile_settings()
        old_name = self.authorPage.get_avatar_filename().get_attribute("style")
        avatar_input = self.authorPage.get_avatar_input()
        self.authorPage.set_new_avatar(avatar_input, new_img_path)
        self.authorPage.wait_update_avatar()
        new_name = self.authorPage.get_avatar_filename().get_attribute("style")
        self.recover_change_avatar()
        self.assertNotEqual(old_name, new_name)

    def test_change_avatar_invalid_file(self):
        new_img_path = self.ROOT+"/files/not_image"

        self.loginPage.open()
        self.loginPage.login(self.EMAIL, self.PASSWORD)
        self.authorPage.go_to_profile_settings()
        avatar_input = self.authorPage.get_avatar_input()
        old_name = self.authorPage.get_avatar_filename().get_attribute("style")
        self.authorPage.set_new_avatar(avatar_input, new_img_path)

        new_name = self.authorPage.get_avatar_filename().get_attribute("style")
        self.assertEqual(old_name, new_name)

