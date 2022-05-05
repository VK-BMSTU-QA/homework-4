import unittest

from page_objects.search_page import SearchPage
from setup.default_setup import default_setup


class SearchCreatorTest(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def setUp(self):
        default_setup(self)

        self.search_page = SearchPage(self.driver)


        self.search_page.open()

    def tearDown(self):
        self.search_page.open()

        self.driver.quit()
