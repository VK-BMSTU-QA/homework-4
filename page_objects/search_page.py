from components.search_field import SearchField
from page_objects.base import Page


class SearchPage(Page):
    PATH = 'search'

    CREATOR_NAME = 'div[class="creator-card__header"]'

    def fill_form(self, name):
        self.fill_form(name)

    def get_creators(self):
        return self._get_element(self.CREATOR_NAME).text.charAt(0)
