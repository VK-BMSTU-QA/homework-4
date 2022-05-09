from components.search_field import SearchField
from page_objects.base import Page


class SearchPage(Page):
    PATH = 'search'

    CREATOR_NAME = 'div[class="creator-card__header"]'
    CREATOR_PAGE = 'div[class="creators-container"]'

    def __init__(self, driver):
        super().__init__(driver)

        self.search_field = SearchField(driver)

    def fill_form(self, name):
        self.search_field.fill_form(name)

    def get_creators(self):
        return self._get_elements(self.CREATOR_NAME)

    def open_creator_page(self):
        self._click_button(self.CREATOR_PAGE)
