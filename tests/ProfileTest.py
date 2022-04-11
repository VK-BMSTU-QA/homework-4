import profile
from tests.BaseTest import BaseTest
from tests.pages.ProfilePage import ProfilePage


class ProfileTest(BaseTest):
    def setUp(self):
        super(ProfileTest, self).setUp()
        self.login()
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.open()


    # def test_nav_adv(self):
    #     self.profile_page.wait_click(self.profile_page.adv_btn)
    #     is_adv = self.profile_page.wait_redirect('https://volchock.ru/profile')
    #     self.assertEqual(is_adv, True, 'Редирект на страницу объявлений не выполнен')

    # def test_nav_fav(self):
    #     self.profile_page.wait_click(self.profile_page.fav_btn)
    #     is_fav = self.profile_page.wait_redirect('https://volchock.ru/profile/favorite')
    #     self.assertEqual(is_fav, True, 'Редирект на страницу избранного не выполнен')

    # def test_nav_cart(self):
    #     self.profile_page.wait_click(self.profile_page.cart_btn)
    #     is_cart = self.profile_page.wait_redirect('https://volchock.ru/profile/cart')
    #     self.assertEqual(is_cart, True, 'Редирект на страницу корзины не выполнен')

    # def test_nav_chat(self):
    #     self.profile_page.wait_click(self.profile_page.chat_btn)
    #     is_chat = self.profile_page.wait_redirect('https://volchock.ru/profile/chat')
    #     self.assertEqual(is_chat, True, 'Редирект на страницу чата не выполнен')

    # def test_nav_promo(self):
    #     self.profile_page.wait_click(self.profile_page.promo_btn)
    #     is_promo = self.profile_page.wait_redirect('https://volchock.ru/profile/promotion')
    #     self.assertEqual(is_promo, True, 'Редирект на страницу промо не выполнен')

    # def test_nav_set(self):
    #     self.profile_page.wait_click(self.profile_page.set_btn)
    #     is_set = self.profile_page.wait_redirect('https://volchock.ru/profile/settings')
    #     self.assertEqual(is_set, True, 'Редирект на страницу настроек не выполнен')

    # def test_nav_archive(self):
    #     self.profile_page.wait_click(self.profile_page.archive_btn)
    #     is_arc = self.profile_page.wait_redirect('https://volchock.ru/profile/archive')
    #     self.assertEqual(is_arc, True, 'Редирект на страницу архива не выполнен')

    # def test_nav_grid(self):
    #     self.profile_page.wait_click(self.profile_page.advert)
    #     is_ad = self.profile_page.wait_any_redirect('ad')
    #     self.assertEqual(is_ad, True, 'Редирект на страницу объявления не выполнен')


    # def test_delete_btn(self):
    #     self.profile_page.wait_click(self.profile_page.delete_btn_main)
    #     is_exist = self.profile_page.is_exist(self.profile_page.card_delete_cross)
    #     self.assertEqual(is_exist, True, 'Элемент удаления карт не появился')

    # def test_modal_popup(self):
    #     self.profile_page.wait_click(self.profile_page.delete_btn_main)
    #     self.profile_page.wait_click(self.profile_page.card_delete_cross)
    #     is_exist = self.profile_page.is_exist(self.profile_page.modal)
    #     self.assertEqual(is_exist, True, 'Элемент модального окна не появился')


    # def test_delete_from_fav(self):
    #     self.profile_page.add_to_fav()
    #     self.profile_page.wait_click(self.profile_page.delete_btn)
    #     self.profile_page.wait_click(self.profile_page.card_delete_cross)
    #     self.profile_page.is_exist(self.profile_page.delete_btn_main)
    #     is_exist = self.profile_page.is_exist(self.profile_page.advert)
    #     self.assertNotEqual(is_exist, True, 'Объявление не удалилось из избранного')

    # def test_delete_from_cart(self):
    #     self.profile_page.add_to_cart()
    #     self.profile_page.wait_click(self.profile_page.delete_btn)
    #     self.profile_page.wait_click(self.profile_page.card_delete_cross)
    #     self.profile_page.is_exist(self.profile_page.delete_btn_main)
    #     is_exist = self.profile_page.is_exist(self.profile_page.advert)
    #     self.assertNotEqual(is_exist, True, 'Объявление не удалилось из корзины')

    # def test_buy_from_cart(self):
    #     self.profile_page.add_to_cart()
    #     self.profile_page.wait_render(self.profile_page.advert)
    #     self.profile_page.wait_click(self.profile_page.buy_btn)
    #     is_exist = self.profile_page.is_exist(self.profile_page.modal)
    #     self.assertEqual(is_exist, True, 'Покупка не совершилась')

    # def test_promo_nav(self):
    #     self.profile_page.wait_click(self.profile_page.promo_btn)
    #     self.profile_page.wait_click(self.profile_page.advert)
    #     is_ad = self.profile_page.wait_any_redirect('upgrade')
    #     self.assertEqual(is_ad, True, 'Редирект на страницу промо не выполнен')


    def test_chat_nav(self):
        self.profile_page.driver.get('https://volchock.ru/profile/chat')
        self.profile_page.wait_click(self.profile_page.dialog_btn)
        is_redir = self.profile_page.wait_redirect('https://volchock.ru/profile/chat/2/8')
        self.assertEqual(is_redir, True, 'Редирект на страницу чата не выполнен')

    
    def test_chat_send(self):
        self.profile_page.driver.get('https://volchock.ru/profile/chat/2/8')
        self.profile_page.fill_input(self.profile_page.chat_input, 'тест')
        self.profile_page.wait_click(self.profile_page.chat_send_btn)
        is_exist = self.profile_page.is_exist(self.profile_page.chat_message)
        self.assertEqual(is_exist, True, 'Сообщение не отправилось')

