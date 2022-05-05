from selenium.webdriver import ActionChains

from components.base import Component


class LevelForm(Component):
    LEVEL_ADD_ADVANTAGE_BUTTON = 'button[class="btn btn_warning "]'

    LEVEL_NAME_INPUT = 'div[class="edit-level__fields"] > div:nth-child(2) > label > input'
    LEVEL_PRICE_INPUT = 'div[class="edit-level__fields"] > div[class="add-benefit"] + div > label > input'
    LEVEL_ADVANTAGE_INPUT = 'div[class="edit-level__fields"] > div:nth-child({}) > div:nth-child(1) > label > input'

    LEVEL_NAME_ERROR = 'div[class="edit-level__fields"] > div:nth-child(2) > div[class="input-validation"]'
    LEVEL_ADVANTAGE_ERROR = 'div[class="edit-level__fields"] > div:nth-child({}) > div:nth-child(1) > div[' \
                            'class="input-validation"] '
    LEVEL_PRICE_ERROR = 'div[class="edit-level__fields"] > div[class="add-benefit"] + div > div[' \
                        'class="input-validation"] '

    LEVEL_DELETE_ADVANTAGE = 'div[class="edit-level__fields"] > div:nth-child({}) > div:nth-child(2)'

    START_NUMBER_ADVANTAGE = 4

    def add_advantage(self):
        self._click_button(self.LEVEL_ADD_ADVANTAGE_BUTTON)

    def set_name(self, value):
        self._set_text(self.LEVEL_NAME_INPUT, value)

    def set_price(self, value):
        self._set_text(self.LEVEL_PRICE_INPUT, value)

    def set_advantage(self, value, n):
        self._set_text(self.LEVEL_ADVANTAGE_INPUT.format(self.START_NUMBER_ADVANTAGE + n), value)

    def check_advantage(self, n):
        return self._check_drawable(self.LEVEL_ADVANTAGE_INPUT.format(self.START_NUMBER_ADVANTAGE + n))

    def check_name_error(self):
        return self._check_drawable(self.LEVEL_NAME_ERROR)

    def check_advantage_error(self, n):
        return self._check_drawable(self.LEVEL_ADVANTAGE_ERROR.format(self.START_NUMBER_ADVANTAGE + n))

    def check_price_error(self):
        return self._check_drawable(self.LEVEL_PRICE_ERROR)

    def check_disappear_advantage(self, n):
        return self._check_disappear(self.LEVEL_ADVANTAGE_INPUT.format(self.START_NUMBER_ADVANTAGE + n))

    def delete_advantage(self, n):
        hover = self.actions.move_to_element(self._get_dom_element(self.LEVEL_ADVANTAGE_INPUT.
                                                                   format(self.START_NUMBER_ADVANTAGE + n)))
        hover.perform()
        self._click_button(self.LEVEL_DELETE_ADVANTAGE.format(self.START_NUMBER_ADVANTAGE + n))

    def fill_form(self, name, price, first_advantage):
        self.set_name(name)
        self.set_price(price)
        self.set_advantage(first_advantage, 1)
