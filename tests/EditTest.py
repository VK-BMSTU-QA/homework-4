from tests.BaseTest import BaseTest
from tests.pages.NewAdvertPage import NewAdvertPage
from tests.pages.AdvertPage import AdvertPage


class EditTest(BaseTest):
    edit_advert_id = 13
    is_image_uploaded = False
    def setUp(self):
        super(EditTest, self).setUp()
        self.login()
        self.new_adv_page = NewAdvertPage(self.driver)
        self.adv_page = AdvertPage(self.driver)
        self.adv_page.open(self.edit_advert_id)
    
    def tearDown(self):
        self.new_adv_page.set_title_to_default()
        if self.is_image_uploaded:
             self.new_adv_page.delete_images()
        super(EditTest, self).tearDown()

    def test_name_change(self):
        title = self.adv_page.get_advert_title()
        self.adv_page.click_edit_button()
        self.new_adv_page.change_advert_title('bbb')
        self.new_adv_page.submit_changes()
        page_title = self.adv_page.get_advert_title()
        self.assertNotEqual(title, page_title, 'Название не изменилось')

    def test_name_notchange(self):
        title = self.adv_page.get_advert_title()
        self.adv_page.click_edit_button()
        self.new_adv_page.change_advert_title('bbb')
        self.new_adv_page.cancel_changes()
        page_title = self.adv_page.get_advert_title()
        self.assertEqual(title, page_title, 'Название изменилось')

    def test_add_image(self):
        self.adv_page.click_edit_button()
        self.new_adv_page.input_images()
        self.is_image_uploaded = True
        is_paginatable = self.adv_page.is_paginatable()
        self.assertTrue(is_paginatable, 'Изображений не 2')
       
