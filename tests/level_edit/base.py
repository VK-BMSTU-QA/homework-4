import unittest

from page_objects.author_settings_page import AuthorSettingsPage
from page_objects.settings_page import SettingsPage
from page_objects.user_page import UserPage
from setup.default_setup import default_setup


class BaseLevelTest(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def setUp(self):
        default_setup(self)

        self.start_page = UserPage(self.driver)

        self.settings_page = SettingsPage(self.driver)

        self.base_page = AuthorSettingsPage(self.driver)

        self.start_page.open_setting()
        self.settings_page.open_author_setting()

        self.incorrect_price = [
            "Привет мир",
            "-20",
            "0",
            "5001",
            "",
        ]

    def tearDown(self):
        self.start_page.open()

        self.driver.quit()
