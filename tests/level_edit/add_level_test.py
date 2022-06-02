from page_objects.approve_delete_level_page import ApproveDeleteLevelPage
from page_objects.level_create_page import LevelAddPage
from page_objects.level_edit_page import LevelEditPage
from page_objects.login import LoginPage
from tests.level_edit.base import BaseLevelTest


class AddLevelTest(BaseLevelTest):

    def __init__(self, methodName: str = ...):
        super(AddLevelTest, self).__init__(methodName)

        self.level_data = {
            "name": "Первый уровень",
            "first_advantage": "Хорошее преимущество",
            "second_advantage": "Второе хорошее преимущество",
            "third_advantage": "Третье хорошее преимущество",
            "price": "20",
        }

    def setUp(self):
        super().setUp()
        self.base_page.open_add_level_page()
        self.add_page = LevelAddPage(self.driver)

    def tearDown(self):
        self.base_page.open()
        if self.base_page.check_exist_level():
            self.base_page.open_edit_level_page()

            level_edit_page = LevelEditPage(self.driver)
            level_edit_page.delete_level()

            approve_delete_level_page = ApproveDeleteLevelPage(self.driver)
            approve_delete_level_page.delete_level()
        loginPage = LoginPage(self.driver)
        loginPage.logout()
        super().tearDown()

    def fill_level_form(self):
        self.add_page.fill_form(self.level_data["name"], self.level_data["price"], self.level_data["first_advantage"])

    def fill_empty_form(self):
        self.add_page.fill_form("", "", "")

    def test_correct_preview_name(self):
        self.fill_level_form()

        self.assertEqual(self.add_page.get_preview_level_name(), self.level_data["name"])

    def test_correct_preview_price(self):
        self.fill_level_form()

        self.assertEqual(self.add_page.get_preview_level_price(), self.level_data["price"])

    def test_correct_preview_first_advantage(self):
        self.fill_level_form()

        self.assertEqual(self.add_page.get_advantage_of_preview_level(1), self.level_data["first_advantage"])

    def test_correct_preview_second_advantage(self):
        self.fill_level_form()

        self.add_page.add_advantage_to_level()
        self.assertTrue(self.add_page.check_advantage(2))
        self.add_page.set_level_advantage(self.level_data["second_advantage"], 2)

        self.assertEqual(self.add_page.get_advantage_of_preview_level(2), self.level_data["second_advantage"])

    def test_correct_add_level(self):
        self.fill_level_form()

        self.add_page.save_level()

        self.assertTrue(self.base_page.check_exist_level())

    def test_correct_display_level_name(self):
        self.fill_level_form()

        self.add_page.save_level()

        self.assertEqual(self.base_page.get_level_name(), self.level_data["name"])

    def test_correct_display_level_price(self):
        self.fill_level_form()

        self.add_page.save_level()

        self.assertEqual(self.base_page.get_level_price(), self.level_data["price"])

    def test_correct_display_level_first_advantage(self):
        self.fill_level_form()

        self.add_page.save_level()

        self.assertEqual(self.base_page.get_advantage_of_level(1), self.level_data["first_advantage"])

    def test_correct_display_level_second_advantage(self):
        self.fill_level_form()

        self.add_page.add_advantage_to_level()
        self.assertTrue(self.add_page.check_advantage(2))
        self.add_page.set_level_advantage(self.level_data["second_advantage"], 2)

        self.add_page.save_level()

        self.assertEqual(self.base_page.get_advantage_of_level(2), self.level_data["second_advantage"])

    def test_invalid_price(self):
        self.fill_level_form()
        for price in self.incorrect_price:
            self.add_page.set_level_price(price)
            self.assertTrue(self.add_page.check_price_error())

    def test_invalid_name(self):
        self.fill_level_form()

        self.add_page.set_level_name("")
        self.assertTrue(self.add_page.check_name_error())

    def test_invalid_first_advantage(self):
        self.fill_level_form()

        self.add_page.set_level_advantage("", 1)
        self.assertTrue(self.add_page.check_advantage_error(1))

    def test_invalid_second_advantage(self):
        self.fill_level_form()

        self.add_page.add_advantage_to_level()
        self.assertTrue(self.add_page.check_advantage(2))
        self.add_page.set_level_advantage("", 2)

        self.assertTrue(self.add_page.check_advantage_error(2))

    def test_empty_form(self):
        self.fill_empty_form()

        self.add_page.save_level()

        self.assertTrue(self.add_page.check_error())
