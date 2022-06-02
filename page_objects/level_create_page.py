from components.level_card import LevelCard
from components.level_form import LevelForm
from page_objects.base import Page


class LevelAddPage(Page):
    LEVEL_SAVE_BUTTON = 'button[class="btn btn_success "]'
    LEVEL_ERROR = 'div[class="edit-level__fields"] > div[class="validation_error"]'

    def __init__(self, driver):
        super().__init__(driver)

        self.preview_card = LevelCard(driver)
        self.level_form = LevelForm(driver)

    def save_level(self):
        self._click_button(self.LEVEL_SAVE_BUTTON)

    def add_advantage_to_level(self):
        self.level_form.add_advantage()

    def check_disappear_advantage(self, n):
        return self.level_form.check_disappear_advantage(n)

    def check_advantage(self, n):
        return self.level_form.check_advantage(n)

    def fill_form(self, name, price, first_advantage):
        self.level_form.fill_form(name, price, first_advantage)

    def set_level_name(self, value):
        self.level_form.set_name(value)

    def set_level_price(self, value):
        self.level_form.set_price(value)

    def set_level_advantage(self, value, n):
        self.level_form.set_advantage(value, n)

    def get_preview_level_name(self):
        return self.preview_card.get_level_name()

    def get_advantage_of_preview_level(self, n):
        return self.preview_card.get_advantage_of_level(n)

    def get_preview_level_price(self):
        return self.preview_card.get_level_price()

    def check_name_error(self):
        return self.level_form.check_name_error()

    def check_advantage_error(self, n):
        return self.level_form.check_advantage_error(n)

    def check_price_error(self):
        return self.level_form.check_price_error()

    def delete_advantage(self, n):
        self.level_form.delete_advantage(n)

    def check_error(self):
        return self._check_drawable(self.LEVEL_ERROR)
