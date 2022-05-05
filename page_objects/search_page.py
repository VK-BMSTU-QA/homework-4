from page_objects.base import Page


class SearchPage(Page):
    PATH = 'search'
    SEARCH_BUTTON = 'div[class="profile-block__no-creators"] > img'

    def open_search(self):
        self._click_button(self.SEARCH_BUTTON)