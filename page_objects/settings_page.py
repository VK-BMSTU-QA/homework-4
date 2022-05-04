from page_objects.base import Page


class SettingsPage(Page):
    PATH = 'profile/edit'
    AUTHOR_SETTING_BUTTON = 'div[class="tabs-panel"] > div[key="creator_settings"]'

    def open_author_setting(self):
        self._click_button(self.AUTHOR_SETTING_BUTTON)