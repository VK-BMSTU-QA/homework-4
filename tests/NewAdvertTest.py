from tests.BaseTest import BaseTest
from tests.pages.NewAdvertPage import NewAdvertPage
import os


class NewAdvertTest(BaseTest):
    def setUp(self):
        super(NewAdvertTest, self).setUp()
        self.login()
        self.new_adv_page = NewAdvertPage(self.driver)
        self.new_adv_page.open()

    def test_name_error_validation(self):
        self.new_adv_page.fill_input(self.new_adv_page.name_input, 'a')
        self.new_adv_page.wait_click(self.new_adv_page.submit_btn)
        name_div = self.new_adv_page.wait_render(self.new_adv_page.name_div)
        is_error = "text-input_wrong" in name_div.get_attribute("class")
        self.assertEqual(is_error, True,
                         'Нет ошибки при создании объявления при названии <2')

    def test_price_error_validation(self):
        self.new_adv_page.fill_input(self.new_adv_page.name_input, 'тест')
        self.new_adv_page.fill_input(self.new_adv_page.price_input, -100)
        self.new_adv_page.wait_click(self.new_adv_page.submit_btn)
        price_div = self.new_adv_page.wait_render(self.new_adv_page.price_div)
        is_error = "text-input_wrong" in price_div.get_attribute("class")
        self.assertEqual(is_error, True,
                         'Нет ошибки при отрицательной цене')

    def test_address_error_validation(self):
        self.new_adv_page.fill_input(self.new_adv_page.name_input, 'тест')
        self.new_adv_page.fill_input(self.new_adv_page.price_input, 100)
        self.new_adv_page.wait_click(self.new_adv_page.submit_btn)
        adr_div = self.new_adv_page.wait_visible(self.new_adv_page.addres_div)
        is_error = "text-input_wrong" in adr_div.get_attribute("class")
        self.assertEqual(is_error, True,
                         'Нет ошибки при создании объявления без адреса')

    def test_price_valid_validation(self):
        self.new_adv_page.fill_input(self.new_adv_page.name_input, 'тест')
        self.new_adv_page.fill_input(self.new_adv_page.price_input, 100)
        self.new_adv_page.wait_click(self.new_adv_page.submit_btn)
        price_div = self.new_adv_page.wait_visible(self.new_adv_page.price_div)
        is_error = "text-input_correct" in price_div.get_attribute("class")
        self.assertEqual(is_error, True,
                         'Нет корректной валидации цены')

    def test_image_uploader(self):
        self.new_adv_page.fill_image_input(os.getcwd()+"/tests/images/test.jpeg")
        is_added = self.new_adv_page.is_exist(self.new_adv_page.inputed_image)
        self.assertEqual(is_added, True,
                         'изображение не добавилось')

    def test_image_delete(self):
        self.new_adv_page.fill_image_input(os.getcwd()+"/tests/images/test.jpeg")
        is_added = self.new_adv_page.is_exist(self.new_adv_page.inputed_image)
        self.new_adv_page.wait_click(self.new_adv_page.delete_image)
        is_exist = self.new_adv_page.is_exist(self.new_adv_page.inputed_image)
        self.assertNotEqual(is_added, is_exist,
                            'изображение не удалилось')

    def test_valid_adv_simple(self):
        self.new_adv_page.fill_input(self.new_adv_page.name_input, 'тест')
        self.new_adv_page.fill_input(self.new_adv_page.price_input, 100)
        self.new_adv_page.wait_click(self.new_adv_page.clickable_map)

        self.new_adv_page.wait_click(self.new_adv_page.submit_btn)
        self.new_adv_page.wait_any_redirect('upgrade')
        self.assertEqual(self.driver.current_url.split('/')[5],
                         'upgrade',
                         'Объявление не создалось')

    def test_valid_adv_with_image(self):
        self.new_adv_page.fill_input(self.new_adv_page.name_input, 'тест')
        self.new_adv_page.fill_input(self.new_adv_page.price_input, 100)
        self.new_adv_page.fill_image_input(os.getcwd()+"/tests/images/test.jpeg")
        self.new_adv_page.fill_input(self.new_adv_page.text_area, 'Это описание')
        self.new_adv_page.wait_click(self.new_adv_page.clickable_map)

        self.new_adv_page.wait_click(self.new_adv_page.submit_btn)
        self.new_adv_page.wait_any_redirect('upgrade')
        self.assertEqual(self.driver.current_url.split('/')[5],
                         'upgrade',
                         'Объявление с фотографией не создалось')
