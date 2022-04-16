from tests.BaseTest import BaseTest
from tests.pages.AdvertPage import AdvertPage


class AdvertTest(BaseTest):
    def setUp(self):
        super(AdvertTest, self).setUp()
        self.adv_page = AdvertPage(self.driver)
        self.adv_page.open(8)

    def test_nav_to_main(self):
        self.adv_page.wait_click(self.adv_page.nav_to_main)
        is_main = self.adv_page.wait_redirect('https://volchock.ru/')
        self.assertEqual(is_main, True, 'Редирект на главную не произошел')

    def test_nav_to_category(self):
        self.adv_page.wait_click(self.adv_page.nav_to_category)
        self.adv_page.wait_any_redirect('category')
        is_category = (len(list(filter(lambda x: x == 'category', self.driver.current_url.split('/')))) > 0)
        self.assertEqual(is_category, True, 'Редирект на категорию не произошел')

    def test_nav_to_elem(self):
        self.adv_page.wait_click(self.adv_page.nav_to_elem)
        self.adv_page.wait_any_redirect('ad')
        is_adv = (len(list(filter(lambda x: x == 'ad', self.driver.current_url.split('/')))) > 0)
        self.assertEqual(is_adv, True, 'Редирект на страницу товара не произошел')

    def test_image_slider(self):
        first_visible = self.adv_page.is_exist(self.adv_page.active_image)
        self.adv_page.wait_click(self.adv_page.next_btn)
        second_visible = self.adv_page.is_exist(self.adv_page.active_image)
        self.assertNotEqual(first_visible, second_visible, 'Изображения не меняются по клику на стрелки')

    def test_image_num_switch(self):
        first_visible = self.adv_page.is_exist(self.adv_page.active_image)
        self.adv_page.wait_click(self.adv_page.second_dot)
        second_visible = self.adv_page.is_exist(self.adv_page.active_image)
        self.assertNotEqual(first_visible, second_visible, 'Изображения не меняются по клику на точки внизу')

    def test_map_togle(self):
        self.adv_page.wait_click(self.adv_page.show_map)
        is_visible = self.adv_page.is_exist(self.adv_page.ymap)
        self.assertEqual(is_visible, True, 'Карта не показывается по клику')

    def test_not_auth_fav(self):
        self.adv_page.wait_click(self.adv_page.fav_btn)
        is_visible = self.adv_page.is_exist(self.adv_page.modal_window)
        self.assertEqual(is_visible, True, 'Модальное окно не открывается при попытке добавить в избранное')

    def test_not_auth_cart(self):
        self.adv_page.wait_click(self.adv_page.cart_btn)
        is_visible = self.adv_page.is_exist(self.adv_page.modal_window)
        self.assertEqual(is_visible, True, 'Модальное окно не открывается при попытке добавить в корзину')

    def test_not_auth_chat(self):
        self.adv_page.wait_click(self.adv_page.chat_btn)
        is_visible = self.adv_page.is_exist(self.adv_page.modal_window)
        self.assertEqual(is_visible, True, 'Модальное окно не открывается при попытке добавить в избранное')

    def test_nav_to_salesman_img(self):
        self.adv_page.wait_click(self.adv_page.salesman_avatar)
        self.adv_page.wait_any_redirect('salesman')
        is_adv = (len(list(filter(lambda x: x == 'salesman', self.driver.current_url.split('/')))) > 0)
        self.assertEqual(is_adv, True, 'Редирект на страницу продавца не произошел по клику на аватар')

    def test_nav_to_salesman_name(self):
        self.adv_page.wait_click(self.adv_page.salesman_name)
        self.adv_page.wait_any_redirect('salesman')
        is_adv = (len(list(filter(lambda x: x == 'salesman', self.driver.current_url.split('/')))) > 0)
        self.assertEqual(is_adv, True, 'Редирект на страницу товара не произошел по клику на имя')

    def test_adv_owner_cart(self):
        self.login()
        self.adv_page.open(13)
        is_visible = self.adv_page.is_exist(self.adv_page.cart_btn)
        self.assertEqual(is_visible, False, 'Есть кнопка добавить в корзину, когда объявление принадлежит пользователю')

    def test_adv_owner_chat(self):
        self.login()
        self.adv_page.open(13)
        is_visible = self.adv_page.is_exist(self.adv_page.chat_btn)
        self.assertEqual(is_visible, False, 'Есть кнопка чата, когда объявление принадлежит пользователю')

    def test_adv_owner_fav(self):
        self.login()
        self.adv_page.open(13)
        self.adv_page.wait_click(self.adv_page.fav_btn)
        is_redirected_correctly = self.adv_page.wait_redirect('https://volchock.ru/profile')
        self.assertEqual(is_redirected_correctly, True, 'Некорректный редирект при нажатии на избранное')

    def test_adv_owner_edit(self):
        self.login()
        self.adv_page.open(13)
        self.adv_page.wait_click(self.adv_page.edit_btn)
        self.adv_page.wait_any_redirect('edit')
        is_edit = (len(list(filter(lambda x: x == 'edit', self.driver.current_url.split('/')))) > 0)
        self.assertEqual(is_edit, True, 'Некорректный редирект при нажатии на редактировать')

    def test_one_fav_click(self):
        self.login()
        self.adv_page.open(8)
        first_text = self.adv_page.get_innerhtml(self.adv_page.fav_btn)
        self.adv_page.wait_until_innerhtml_changes_after_click(self.adv_page.fav_btn)
        second_text = self.adv_page.get_innerhtml(self.adv_page.fav_btn)
        self.assertNotEqual(first_text, second_text, 'Нажатие по кнопке добавить в избранное не изменяет текст')
        self.adv_page.clearFav()

    def test_two_fav_click(self):
        self.login()
        self.adv_page.open(8)
        self.adv_page.wait_until_innerhtml_changes_after_click(self.adv_page.fav_btn)
        self.adv_page.wait_click(self.adv_page.fav_btn)
        is_redirected_correctly = self.adv_page.wait_redirect('https://volchock.ru/profile/favorite')
        self.assertEqual(is_redirected_correctly, True,
                         'Нажатие по кнопке добавить в избранное повторно не редиректит')
        self.adv_page.clearFav()

    def test_one_cart_click(self):
        self.login()
        self.adv_page.open(8)
        first_text = self.adv_page.get_innerhtml(self.adv_page.cart_btn)
        self.adv_page.wait_until_innerhtml_changes_after_click(self.adv_page.cart_btn)
        second_text = self.adv_page.get_innerhtml(self.adv_page.cart_btn)
        self.assertNotEqual(first_text, second_text, 'Нажатие по кнопке добавить в корзину не изменяет текст')
        self.adv_page.clearCart()

    def test_two_cart_click(self):
        self.login()
        self.adv_page.open(8)
        self.adv_page.wait_until_innerhtml_changes_after_click(self.adv_page.cart_btn)
        self.adv_page.wait_click(self.adv_page.cart_btn)
        is_redirected_correctly = self.adv_page.wait_redirect('https://volchock.ru/profile/cart')
        self.assertEqual(is_redirected_correctly, True,
                         'Нажатие по кнопке добавить в корзину повторно не редиректит')
        self.adv_page.clearCart()

    def test_one_chat_click(self):
        self.login()
        self.adv_page.open(8)
        self.adv_page.wait_click(self.adv_page.chat_btn)
        is_redirected = self.adv_page.wait_redirect('https://volchock.ru/profile/chat/2/8')
        self.assertEqual(is_redirected, True, 'Нет редиректа в чат')
