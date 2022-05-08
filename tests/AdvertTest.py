from tests.BaseTest import BaseTest
from tests.pages.AdvertPage import AdvertPage


class AdvertTest(BaseTest):
    advert_test_id = 8
    advert_owner_test_id = 13
    def setUp(self):
        super(AdvertTest, self).setUp()
        self.adv_page = AdvertPage(self.driver)
        self.adv_page.open(self.advert_test_id)

    def tearDown(self):
        is_not_logged = self.adv_page.check_log()
        if not is_not_logged:
            self.adv_page.clearCart()
            self.adv_page.clearFav()
        super(AdvertTest, self).tearDown()

    def test_map_togle(self):
        self.adv_page.toggle_map()
        is_visible = self.adv_page.is_map_visible()
        self.assertTrue(is_visible, 'Карта не показывается по клику')

    def test_image_slider(self):
        first_visible = self.adv_page.is_first_image_visible()
        self.adv_page.change_image_by_clicking_pointer()
        second_visible = self.adv_page.is_first_image_visible()
        self.assertNotEqual(first_visible, second_visible, 'Изображения не меняются по клику на стрелки')

    def test_image_num_switch(self):
        first_visible = self.adv_page.is_first_image_visible()
        self.adv_page.change_image_by_clicking_dot()
        second_visible = self.adv_page.is_first_image_visible()
        self.assertNotEqual(first_visible, second_visible, 'Изображения не меняются по клику на точки внизу')

    def test_not_auth_actions(self):
        self.adv_page.click_fav()
        is_visible = self.adv_page.is_modal_active()
        self.assertTrue(is_visible, 'Модальное окно не открывается при попытке добавить в избранное')
        self.adv_page.close_modal()

        self.adv_page.click_cart()
        is_visible = self.adv_page.is_modal_active()
        self.assertTrue(is_visible, 'Модальное окно не открывается при попытке добавить в корзину')
        self.adv_page.close_modal()

        self.adv_page.click_chat()
        is_visible = self.adv_page.is_modal_active()
        self.assertTrue(is_visible, 'Модальное окно не открывается при попытке добавить в корзину')
        self.adv_page.close_modal()

    def test_owner_actions(self):
        self.login()
        self.adv_page.open(self.advert_owner_test_id)

        is_cart = self.adv_page.is_cart_btn_exist()
        self.assertFalse(is_cart, 'Есть кнопка добавить в корзину, когда объявление принадлежит пользователю')

        is_chat = self.adv_page.is_chat_btn_exist()
        self.assertFalse(is_chat, 'Есть кнопка чата, когда объявление принадлежит пользователю')

        is_profile_after_fav = self.adv_page.is_fav_redirect_to_profile()
        self.assertTrue(is_profile_after_fav, 'Некорректный редирект при нажатии на избранное')
        self.adv_page.open(self.advert_owner_test_id)

        is_edit_after_click = self.adv_page.is_edit_after_click()
        self.assertTrue(is_edit_after_click, 'Некорректный редирект при нажатии на редактировать')

    
    def test_login_chat_click(self):
        self.login()
        self.adv_page.open(self.advert_test_id)

        self.adv_page.click_chat()
        is_redirected = self.adv_page.is_redirected_to_chat()
        self.assertTrue(is_redirected, 'Нет редиректа в чат')


    def test_login_fav_click(self):
        self.login()
        self.adv_page.open(self.advert_test_id)

        first_text = self.adv_page.fav_btn_text()
        self.adv_page.change_fav_text()
        second_text = self.adv_page.fav_btn_text()
        self.assertNotEqual(first_text, second_text, 'Нажатие по кнопке добавить в избранное не изменяет текст')
        
        self.adv_page.click_fav()
        is_redirected = self.adv_page.is_redirected_to_fav()
        self.assertTrue(is_redirected,
                         'Нажатие по кнопке добавить в избранное повторно не редиректит')

    def test_login_cart_click(self):
        self.login()
        self.adv_page.open(self.advert_test_id)

        first_text = self.adv_page.cart_btn_text()
        self.adv_page.change_cart_text()
        second_text = self.adv_page.cart_btn_text()
        self.assertNotEqual(first_text, second_text, 'Нажатие по кнопке добавить в корзину не изменяет текст')
        
        self.adv_page.click_cart()
        is_redirected = self.adv_page.is_redirected_to_cart()
        self.assertTrue(is_redirected,
                         'Нажатие по кнопке добавить в корзину повторно не редиректит')
