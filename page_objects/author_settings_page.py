from components.level_card import LevelCard
from page_objects.base import Page


class AuthorSettingsPage(Page):
    LEVEL_EDIT_BUTTON = 'div[class="level-card "] > button'

    def __init__(self, driver):
        super().__init__(driver)

        self.level_card = LevelCard(driver)

    def open_edit_level_page(self):
        self.level_card.click_card_button()

    def open_add_level_page(self):
        self._click_button(self.LEVEL_EDIT_BUTTON)

    def get_level_name(self):
        return self.level_card.get_level_name()

    def get_advantage_of_level(self, n):
        return self.level_card.get_advantage_of_level(n)

    def get_level_price(self):
        return self.level_card.get_level_price()
