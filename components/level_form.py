from components.base import Component

class LevelForm(Component):
    LEVEL_ADD_ADVANTAGE_BUTTON = 'button[class="btn btn_warning "]'

    LEVEL_NAME_INPUT = 'input[type="text"]:nth-child(1)'
    LEVEL_PRICE_INPUT = 'input[type="number"]'
    LEVEL_ADVANTAGE_INPUT = 'input[type="text"]:nth-child({})'

    def add_advantage(self):
        self._click_button(self.LEVEL_ADD_ADVANTAGE_BUTTON)

    def set_name(self, value):
        self._set_text(self.LEVEL_NAME_INPUT, value)

    def set_price(self, value):
        self._set_text(self.LEVEL_PRICE_INPUT, value)

    def set_advantage(self, value, n):
        self._set_text(self.LEVEL_ADVANTAGE_INPUT.format(1 + n), value)
