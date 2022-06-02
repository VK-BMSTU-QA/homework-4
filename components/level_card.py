from components.base import Component


class LevelCard(Component):
    LEVEL_NAME = 'div[class="level-card__header-name"]'
    LEVEL_PRICE = 'div[class="level-card__action-price"] > div[class="price"]'
    LEVEL_ADVANTAGE = 'div[class="level-card__body"] > div[key="{}"]'

    LEVEL_BUTTON = 'div[class~="level-card"] > button'

    def get_level_name(self):
        return self._get_element(self.LEVEL_NAME).text

    def get_advantage_of_level(self, n):
        return self._get_element(self.LEVEL_ADVANTAGE.format(n - 1)).text

    def get_level_price(self):
        return self._get_element(self.LEVEL_PRICE).text.split(" ")[0]

    def click_card_button(self):
        self._click_button(self.LEVEL_BUTTON)
