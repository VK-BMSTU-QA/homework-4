from page_objects.base import Page


class UserPage(Page):
    PATH = 'profile'
    SETTING_BUTTON = 'div[class="profile-card__body"] > button'

    def open_setting(self):
        self._click_button(self.SETTING_BUTTON)
