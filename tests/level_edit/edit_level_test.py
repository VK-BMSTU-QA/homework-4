from page_objects.approve_delete_level_page import ApproveDeleteLevelPage
from page_objects.level_create_page import LevelAddPage
from page_objects.level_edit_page import LevelEditPage
from page_objects.login import LoginPage
from tests.level_edit.base import BaseLevelTest


class EditLevelTest(BaseLevelTest):

    def __init__(self, methodName: str = ...):
        super(EditLevelTest, self).__init__(methodName)

        self.edit_level_data = {
            "name": "Первый уровень",
            "first_advantage": "Хорошее преимущество",
            "second_advantage": "Второе хорошее преимущество",
            "price": "20",
        }

        self.level_data = {
            "name": "Редактированный уровень",
            "first_advantage": "Редактированное преимущество",
            "third_advantage": "Третье Редактированное преимущество",
            "price": "30",
        }

    def setUp(self):
        super().setUp()
        self.base_page.open_add_level_page()

        add_page = LevelAddPage(self.driver)
        add_page.fill_form(self.edit_level_data["name"], self.edit_level_data["price"], self.edit_level_data["first_advantage"])
        add_page.add_advantage_to_level()
        add_page.set_level_advantage(self.edit_level_data["second_advantage"], 2)
        add_page.save_level()

        self.edit_page = LevelEditPage(self.driver)
        self.base_page.check_exist_level()
        self.base_page.open_edit_level_page()
        self.approve_delete_level_page = ApproveDeleteLevelPage(self.driver)

    def tearDown(self):
        self.base_page.open()
        if self.base_page.check_exist_level():
            self.base_page.open_edit_level_page()

            self.edit_page.delete_level()
            self.approve_delete_level_page.delete_level()

        loginPage = LoginPage(self.driver)
        loginPage.logout()
        super().tearDown()

    def fill_level_form(self):
        self.edit_page.fill_form(self.level_data["name"], self.level_data["price"], self.level_data["first_advantage"])

    def fill_empty_form(self):
        self.edit_page.fill_form("", "", "")

    def test_correct_preview_name(self):
        self.fill_level_form()

        self.assertEqual(self.edit_page.get_preview_level_name(), self.level_data["name"])

    def test_correct_preview_price(self):
        self.fill_level_form()

        self.assertEqual(self.edit_page.get_preview_level_price(), self.level_data["price"])

    def test_correct_preview_first_advantage(self):
        self.fill_level_form()

        self.assertEqual(self.edit_page.get_advantage_of_preview_level(1), self.level_data["first_advantage"])

    def test_correct_delete_second_advantage(self):
        self.fill_level_form()

        self.edit_page.delete_advantage(2)
        self.assertFalse(self.edit_page.check_advantage(2))

    def test_correct_preview_third_advantage(self):
        self.fill_level_form()

        self.edit_page.delete_advantage(2)
        self.assertTrue(self.edit_page.check_disappear_advantage(2))
        self.edit_page.add_advantage_to_level()
        self.edit_page.set_level_advantage(self.level_data["third_advantage"], 2)

        self.assertEqual(self.edit_page.get_advantage_of_preview_level(2), self.level_data["third_advantage"])

    def test_exists_edit_level(self):
        self.fill_level_form()

        self.edit_page.save_level()

        self.assertTrue(self.base_page.check_exist_level())

    def test_correct_display_level_name(self):
        self.fill_level_form()

        self.edit_page.save_level()

        self.assertEqual(self.base_page.get_level_name(), self.level_data["name"])

    def test_correct_display_level_price(self):
        self.fill_level_form()

        self.edit_page.save_level()

        self.assertEqual(self.base_page.get_level_price(), self.level_data["price"])

    def test_correct_display_level_first_advantage(self):
        self.fill_level_form()

        self.edit_page.save_level()

        self.assertEqual(self.base_page.get_advantage_of_level(1), self.level_data["first_advantage"])

    def test_correct_display_level_second_advantage(self):
        self.fill_level_form()

        self.edit_page.delete_advantage(2)
        self.assertTrue(self.edit_page.check_disappear_advantage(2))
        self.edit_page.add_advantage_to_level()
        self.edit_page.set_level_advantage(self.level_data["third_advantage"], 2)

        self.edit_page.save_level()

        self.assertEqual(self.base_page.get_advantage_of_level(2), self.level_data["third_advantage"])

    def test_invalid_price(self):
        self.fill_level_form()
        for price in self.incorrect_price:
            self.edit_page.set_level_price(price)
            self.assertTrue(self.edit_page.check_price_error())

    def test_invalid_name(self):
        self.fill_level_form()

        self.edit_page.set_level_name("")
        self.assertTrue(self.edit_page.check_name_error())

    def test_invalid_first_advantage(self):
        self.fill_level_form()

        self.edit_page.set_level_advantage("", 1)
        self.assertTrue(self.edit_page.check_advantage_error(1))

    def test_invalid_second_advantage(self):
        self.fill_level_form()

        self.edit_page.delete_advantage(2)
        self.assertTrue(self.edit_page.check_disappear_advantage(2))
        self.edit_page.add_advantage_to_level()
        self.edit_page.set_level_advantage(self.level_data["third_advantage"], 2)

        self.assertTrue(self.edit_page.check_advantage_error(2))

    def test_cancel_delete(self):
        self.fill_level_form()

        self.edit_page.delete_level()
        self.approve_delete_level_page.cancel_delete_level()

        self.base_page.open()

        self.assertTrue(self.base_page.check_exist_level())

    def test_correct_delete(self):
        self.fill_level_form()

        self.edit_page.delete_level()
        self.approve_delete_level_page.delete_level()

        self.assertFalse(self.base_page.check_exist_level())
