from tests.BaseTest import BaseTest
from tests.pages.MainPage import MainPage
from urllib.parse import unquote


class MainTest(BaseTest):
    def setUp(self):
        super(MainTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()

    def test_main_objects_visibility(self):
        is_exist = self.main_page.is_categories_exist()
        self.assertTrue(is_exist,
                        'На главной странице не отображается блок категорий')

        is_visible_card = self.main_page.is_card_grid_exist()
        self.assertTrue(is_visible_card,
                        'Грид карточек не отображается')

    def test_change_lang_btn(self):
        pre_text = self.main_page.get_login_btn_text()
        self.main_page.change_language()
        post_text = self.main_page.get_login_btn_text()
        self.assertNotEqual(pre_text, post_text, 'Текст не изменился')

    def test_open_modal(self):
        self.main_page.click_login()
        is_modal_active = self.main_page.is_modal_active()
        self.assertTrue(is_modal_active,
                        'Модальное окно не открылось при попытке авторизации')
        self.main_page.close_modal()

        self.main_page.click_new_adv()
        is_modal_active = self.main_page.is_modal_active()
        self.assertTrue(
            is_modal_active, 'Модальное окно не открылось при попытке добавить новое объявление')

    def test_username_visible(self):
        self.login()
        self.main_page.open_profile_menu()
        is_visible = self.main_page.is_profile_menu_active()
        self.assertTrue(
            is_visible, 'Нажатие на имя пользователя не открывает меню')

    def test_logout(self):
        self.login()
        self.main_page.open_profile_menu()
        self.main_page.click_logout_btn()
        is_logout = self.main_page.is_login_btn_exist()
        self.assertTrue(is_logout, 'Логаут по нажатию кнопки не выполнен')

    def test_search(self):
        search_string = 'тест'
        self.main_page.search_by_value_in_input(search_string)
        search_text = self.driver.current_url.split('/')[4]
        search_text = unquote(search_text)
        self.assertEqual(search_text, search_string,
                         'Инпут в поиск и страница поиска отличаются')
        self.main_page.clear_search_input()

        some_value_for_empty_search = 'sometextthatsupposedtobeneverfoundbyanyone'
        self.main_page.search_by_value_in_input(some_value_for_empty_search)
        is_empty = self.main_page.is_search_empty()
        self.assertTrue(is_empty, 'Элемент пустой сетки отсутствует')

