import os
from tests.BaseTest import BaseTest
from tests.pages.ProfilePage import ProfilePage


class ProfileTest(BaseTest):
    is_password_changed = False
    is_info_changed = False

    def setUp(self):
        super(ProfileTest, self).setUp()
        self.login()
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.open()
    
    def tearDown(self):
        if self.is_password_changed:
            self.profile_page.reset_pass(self.correct_password)
        if self.is_info_changed:
            self.profile_page.reset_info()
        super(ProfileTest, self).tearDown()

    def test_delete_btn(self):
        is_delete_cross_exist = self.profile_page.press_delete()
        self.assertTrue(is_delete_cross_exist, 'Элемент удаления карт не появился')
        self.profile_page.press_delete_cross()
        is_modal_exist = self.profile_page.is_profile_modal_exist()
        self.assertTrue(is_modal_exist, 'Элемент модального окна не появился')

    def test_delete_from_fav(self):
        self.profile_page.add_to_fav()
        self.profile_page.press_delete_not_main()
        self.profile_page.press_delete_cross()

        is_exist = self.profile_page.is_advert_exist()
        self.assertFalse(is_exist, 'Объявление не удалилось из избранного')

    def test_delete_from_cart(self):
        self.profile_page.add_to_cart()
        self.profile_page.press_delete_not_main()
        self.profile_page.press_delete_cross()

        is_exist = self.profile_page.is_advert_exist()
        self.assertFalse(is_exist, 'Объявление не удалилось из корзины')

    def test_buy_from_cart(self):
        self.profile_page.add_to_cart()
        self.profile_page.click_buy_button()
        is_exist = self.profile_page.is_profile_modal_exist()
        self.assertTrue(is_exist, 'Покупка не совершилась')

    def test_chat(self):
        self.profile_page.driver.get('https://volchock.ru/profile/chat')
        is_redirected = self.profile_page.click_chat()
        self.assertTrue(is_redirected, 'Редирект на страницу чата не выполнен')
        self.profile_page.send_chat_message('тест')
        is_exist = self.profile_page.is_message_send()
        self.assertTrue(is_exist, 'Сообщение не отправилось')


    def test_image_upload(self):
        self.profile_page.driver.get('https://volchock.ru/profile/settings')
        first_src = self.profile_page.get_avatar_in_profile()
        self.profile_page.fill_image_input(os.getcwd()+'/tests/images/test0.jpeg')
        second_src = self.profile_page.get_avatar_in_profile()
        self.assertNotEqual(first_src, second_src, 'Аватар в профиле не изменился')
        navbar_src = self.profile_page.get_avatar_in_navbar()
        self.assertNotEqual(first_src, navbar_src, 'Аватар в навбаре не изменился')


    def test_password_change_validations(self):
        first_value = 'a'
        second_value = 'somepassword'
        self.profile_page.driver.get('https://volchock.ru/profile/settings')

        self.profile_page.click_change_password()
        is_error = self.profile_page.is_error_in_new_password()
        self.assertTrue(is_error, 'Нет ошибки при пустом новом пароле')

        
        self.profile_page.fill_new_password(first_value)
        self.profile_page.click_change_password()
        is_error = self.profile_page.is_error_in_new_password()
        self.assertTrue(is_error, 'Нет ошибки при коротком новом пароле')
        
        self.profile_page.fill_new_password(second_value)
        self.profile_page.click_change_password()
        is_error = self.profile_page.is_error_in_old_password()
        self.assertTrue(is_error, 'Нет ошибки при пустом старом пароле')

        self.profile_page.fill_old_password(first_value + second_value)
        self.profile_page.click_change_password()
        is_error = self.profile_page.is_error_in_new_password()
        self.assertTrue(is_error, 'Нет ошибки при одинаковых паролях')


    def test_password_change_correct(self):
        self.profile_page.driver.get('https://volchock.ru/profile/settings')
        
        self.profile_page.fill_old_password(self.correct_password)
        self.profile_page.fill_new_password('password1')
        self.profile_page.click_change_password()
        is_correct = self.profile_page.is_password_changed()
        self.is_password_changed = True
        self.assertTrue(is_correct, 'Ошибка при корретных данных')

    def test_short_info(self):
        self.profile_page.driver.get('https://volchock.ru/profile/settings')
        self.profile_page.fill_name('a')
        self.profile_page.click_change_info()
        is_error = self.profile_page.is_error_in_name()
        self.assertTrue(is_error, 'Нет ошибки при коротком имени')

        self.profile_page.fill_name('aa')
        self.profile_page.fill_surnname('a')
        self.profile_page.click_change_info()
        is_error = self.profile_page.is_error_in_surname()
        self.assertTrue(is_error, 'Нет ошибки при короткой фамилии')

    def test_name_change(self):
        self.profile_page.driver.get('https://volchock.ru/profile/settings')
        username = 'aa'
        self.profile_page.fill_name(username)
        self.profile_page.fill_surnname(username)
        self.profile_page.click_change_info()
        
        self.profile_page.is_name_changed()
        new_username_in_profile = self.profile_page.get_name_from_profile()
        self.is_info_changed = True
        self.assertEqual(new_username_in_profile, username, 'Имя в профиле не изменилось')

        new_user_name_in_navbar = self.profile_page.get_name_from_navbar()
        self.assertEqual(new_user_name_in_navbar, username, 'Имя в навбаре не изменилось')


    def test_change_phone(self):
        self.profile_page.driver.get('https://volchock.ru/profile/settings')
        self.profile_page.fill_phone('322)111-11-11')
        self.profile_page.click_change_info()
        is_correct = self.profile_page.is_phone_changed()
        self.assertTrue(is_correct, 'Ошибка в телефоне')
