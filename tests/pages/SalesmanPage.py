from tests.pages.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class SalesmanPage(BasePage):
    card = '.card__content'
    star = '.stars__star'

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open(self, id):
        self.driver.get(self.salesman_url(id))

    def hover(self, selector):
        elem = self.wait_render(selector)
        hover = ActionChains(self.driver).move_to_element(elem)
        hover.perform()
