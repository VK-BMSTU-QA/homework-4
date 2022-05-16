from page_objects.base import Page


class UserPage(Page):
    PATH = 'profile'
    SETTING_BUTTON = 'div[class="profile-card__body"] > button'
    SEARCH_BUTTON = 'div[class="profile-block__no-creators"] > img'

    def open_setting(self):
        self._click_button(self.SETTING_BUTTON)

    def open_search(self):
        self._click_button(self.SEARCH_BUTTON)
