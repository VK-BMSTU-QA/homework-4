from tests.search_creator.base import BaseSearchTest
from page_objects.search_page import SearchPage


class AddLevelTest(BaseSearchTest):

    def __init__(self, methodName: str = ...):
        super(AddLevelTest, self).__init__(methodName)

        self.search_data = {
            "name": "v",
        }

    def setUp(self):
        super().setUp()
        self.start_page.open_search()
        self.search_page = SearchPage(self.driver)

    def tearDown(self):
        self.search_page.open()
        super().tearDown()

    def fill_search_form(self):
        self.search_page.fill_form(self.search_data["name"])

    def test_correct_creator(self):
        self.fill_search_form()

        self.assertEqual(self.search_page.get_creators(), self.search_data["name"])
