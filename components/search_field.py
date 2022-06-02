from components.base import Component


class SearchField(Component):
    SEARCH_FIELD = 'div[class="search__fields-container"] > div > label > input'

    def fill_form(self, value):
        self._set_text(self.SEARCH_FIELD, value)
