from tests.BaseTest import BaseTest
from tests.pages.NewAdvertPage import NewAdvertPage
from tests.pages.AdvertPage import AdvertPage


class EditTest(BaseTest):
    def setUp(self):
        super(EditTest, self).setUp()
        self.login()
        self.new_adv_page = NewAdvertPage(self.driver)
        self.adv_page = AdvertPage(self.driver)
        self.adv_page.open(13)
        self.adv_page.wait_click(self.adv_page.edit_btn)

    # def test_title_input(self):
    #     title = self.new_adv_page.get_input_value(self.new_adv_page.name_input)
    #     self.assertGreater(len(title), 0, 'Название пустое')

    # def test_price_input(self):
    #     price = self.new_adv_page.get_input_value(self.new_adv_page.price_input)
    #     self.assertGreater(len(price), 0, 'Цена пустая')

    def test_name_change(self):
        self.adv_page.open(13)
        self.adv_page.wait_render(self.adv_page.title)
        title = self.adv_page.get_innerhtml(self.adv_page.title).strip()
        self.adv_page.wait_click(self.adv_page.edit_btn)
        self.new_adv_page.fill_input(self.new_adv_page.name_input, 'aaa')
        self.new_adv_page.wait_click(self.new_adv_page.submit_btn)
        self.new_adv_page.wait_redirect('https://volchock.ru/ad/13')
        self.adv_page.wait_render(self.adv_page.title)
        page_title = self.adv_page.get_innerhtml(self.adv_page.title).strip()
        self.assertNotEqual(title, page_title, 'Название не изменилось')

    def test_name_notchange(self):
        self.adv_page.open(13)
        self.adv_page.wait_render(self.adv_page.title)
        title = self.adv_page.get_innerhtml(self.adv_page.title).strip()
        self.adv_page.wait_click(self.adv_page.edit_btn)
        self.new_adv_page.fill_input(self.new_adv_page.name_input, title+'bbb')
        self.new_adv_page.wait_click(self.new_adv_page.cancel_btn)
        self.new_adv_page.wait_redirect('https://volchock.ru/ad/13')
        self.adv_page.wait_render(self.adv_page.title)
        page_title = self.adv_page.get_innerhtml(self.adv_page.title).strip()
        self.assertEqual(title, page_title, 'Название изменилось')

    # def test_add_image(self):
    #     self.new_adv_page.input_images()
    #     is_paginatable = self.adv_page.is_exist(self.adv_page.next_btn)
    #     self.assertTrue(is_paginatable, 'Изображений не 2')
    #     self.new_adv_page.delete_images()
