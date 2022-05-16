from tests.creator.base import BaseCreatorTest
from page_objects.creator_page import CreatorPage


class CreatorTest(BaseCreatorTest):

    def __init__(self, methodName: str = ...):
        super(CreatorTest, self).__init__(methodName)

        self.creator_data = {
            "shared": "Ссылка скопирована в буфер обмена",
        }

    def setUp(self):
        super().setUp()

        self.search_page.open_creator_page()
        self.creator_page = CreatorPage(self.driver)

    def tearDown(self):
        self.creator_page.open()
        super().tearDown()

    def test_share_account(self):
        self.creator_page.share_account()

        self.assertEqual(self.creator_page.is_account_shared(), self.creator_data["shared"])

    def test_subscribe(self):
        self.creator_page.pick_level()
        self.creator_page.subscribe()

        self.assertTrue(self.creator_page._check_current_url('https://yoomoney.ru/'))

    def test_open_post(self):
        self.assertTrue(self.creator_page.open_post())
