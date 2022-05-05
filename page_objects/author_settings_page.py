from components.level_card import LevelCard
from page_objects.base import Page


class AuthorSettingsPage(Page):
    PATH = 'profile/edit/creator_settings'
    LEVEL_ADD_BUTTON = 'div[class="profile-edit__levels-container"] img'

    LEVEL_EXIST = 'div[class~="level-card"]'

    def __init__(self, driver):
        super().__init__(driver)

        self.level_card = LevelCard(driver)

    def open_edit_level_page(self):
        self.level_card.click_card_button()

    def check_exist_level(self):
        return self._check_drawable(self.LEVEL_EXIST)

    def open_add_level_page(self):
        self._click_button(self.LEVEL_ADD_BUTTON)

    def get_level_name(self):
        return self.level_card.get_level_name()

    def get_advantage_of_level(self, n):
        return self.level_card.get_advantage_of_level(n)

    def get_level_price(self):
        return self.level_card.get_level_price()
