from components.level_card import LevelCard
from page_objects.base import Page


class AuthorSettingsPage(Page):
    BASE_URL = 'http://pyaterochka-team.site/'
    PATH = 'profile/edit/creator_settings'
    LEVEL_ADD_BUTTON = 'div[class="profile-edit__levels-container"] img'
    DEFAULT_AVATAR = "/files/author-avatar-default.png"

    LEVEL_EXIST = 'div[class~="level-card"]'
    CHANGE_AVATAR = 'input[class="image-uploader__file-upload"]'
    PROFILE_AVATAR_NAME = '//*[@id="root"]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div[1]'
    EMAIL_HEADER = '.profile-card__username'

    def __init__(self, driver):
        super().__init__(driver)

        self.level_card = LevelCard(driver)

    def open_edit_level_page(self):
        self.level_card.click_card_button()

    def check_exist_level(self):
        return self._check_drawable(self.LEVEL_EXIST)

    def open_add_level_page(self):
        self._click_button(self.LEVEL_ADD_BUTTON)

    def go_to_profile_settings(self):
        _ = self._get_element(self.EMAIL_HEADER)
        return self.redirect_to_profile_settings()

    def get_level_name(self):
        return self.level_card.get_level_name()

    def get_advantage_of_level(self, n):
        return self.level_card.get_advantage_of_level(n)

    def get_level_price(self):
        return self.level_card.get_level_price()

    def get_avatar_input(self):
        return self._get_input(self.CHANGE_AVATAR)

    def get_avatar_filename(self):
        return self._get_element_by_xpath(self.PROFILE_AVATAR_NAME)

    def wait_update_avatar(self):
        return self._check_disappear_by_xpath(self.PROFILE_AVATAR_NAME)

    def set_new_avatar(self, input_form, img_path):
        return input_form.send_keys(img_path)

    def redirect_to_profile_settings(self):
        return self.driver.get(self.BASE_URL + 'profile/edit/creator_settings')

