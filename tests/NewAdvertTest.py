from tests.BaseTest import BaseTest
from tests.pages.NewAdvertPage import NewAdvertPage
import os


class NewAdvertTest(BaseTest):
    def setUp(self):
        super(NewAdvertTest, self).setUp()
        self.login()
        self.new_adv_page = NewAdvertPage(self.driver)
        self.new_adv_page.open()

    def test_error_validation(self):
        self.new_adv_page.change_advert_title('т')
        self.new_adv_page.press_sumbit_button()
        is_error = self.new_adv_page.is_error_in_title_input()
        self.assertTrue(is_error,
                         'Нет ошибки при создании объявления при названии <2')

        self.new_adv_page.change_advert_title('тест')
        self.new_adv_page.change_price_value(-100)
        self.new_adv_page.press_sumbit_button()
        is_error = self.new_adv_page.is_error_in_price_input()
        self.assertTrue(is_error,
                         'Нет ошибки при отрицательной цене')

        self.new_adv_page.clear_price_input()
        self.new_adv_page.change_price_value(100)
        self.new_adv_page.press_sumbit_button()
        is_error = self.new_adv_page.is_error_in_addres_input()
        self.assertTrue(is_error,
                         'Нет ошибки при создании объявления без адреса')


    def test_image_uploader(self):
        self.new_adv_page.fill_image_input(os.getcwd()+"/tests/images/test0.jpeg")
        is_added = self.new_adv_page.is_image_exist()
        self.assertTrue(is_added,
                         'изображение не добавилось')
        self.new_adv_page.delete_added_image()
        is_exist = self.new_adv_page.is_image_exist()
        self.assertNotEqual(is_added, is_exist,
                            'изображение не удалилось')


    def test_valid_adv_simple(self):
        self.new_adv_page.change_advert_title('тест')
        self.new_adv_page.change_price_value(100)
        self.new_adv_page.click_map()

        self.new_adv_page.press_sumbit_button()
        is_created = self.new_adv_page.is_redirected_to_updrage_page()
        self.assertTrue(is_created, 'Объявление не создалось')

    def test_valid_adv_with_image(self):
        self.new_adv_page.change_advert_title('тест')
        self.new_adv_page.change_price_value(100)
        self.new_adv_page.fill_image_input(os.getcwd()+"/tests/images/test0.jpeg")
        self.new_adv_page.fill_description('Это описание')
        self.new_adv_page.click_map()
        self.new_adv_page.press_sumbit_button()
        is_created = self.new_adv_page.is_redirected_to_updrage_page()
        self.assertTrue(is_created, 'Объявление с фотографией не создалось')
