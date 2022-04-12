from tests.BaseTest import BaseTest
from tests.pages.MainPage import MainPage
from urllib.parse import unquote


class MainTest(BaseTest):
    def setUp(self):
        super(MainTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()

    def test_categories(self):
        is_exist = self.main_page.is_exist(self.main_page.categories)
        self.assertEqual(is_exist, True, 
                        'На главной странице не отображается блок категорий'
                        )

    def test_category_routing(self):
        category_href = self.main_page.wait_render(self.main_page.category_href)
        href = category_href.get_attribute('href')
        category_href.click()
        self.main_page.wait_redirect(href)
        self.assertEqual(self.driver.current_url, 
                        self.main_page.category_url(href.split('/')[-1]),
                        'Название категории и страницы категорий не совпадают')

    def test_card_grid(self):
        is_visible_card = self.main_page.is_exist(self.main_page.card)
        self.assertEqual(is_visible_card, True,
                        'Грид карточек не отображается')

    def test_card_routing(self):
        self.main_page.wait_click(self.main_page.card)
        self.main_page.wait_any_redirect('ad')
        self.assertEqual(self.driver.current_url.split('/')[3], 
                        'ad',
                        'Названия страниц не совпадают')

    def test_card_empty_search(self):
        self.main_page.fill_input(self.main_page.search_input, 'paskdpasjdauewvbzxcjzlxkcweqoejqeov')
        self.main_page.wait_click(self.main_page.search_btn)
        self.main_page.wait_any_redirect('search')
        is_empty = self.main_page.is_exist(self.main_page.empty)
        self.assertEqual(is_empty, True, 'Элемент пустой сетки отсутствует')


    def test_change_lang_btn(self):
        btn = self.main_page.wait_render(self.main_page.open_modal_btn)
        pre_text = btn.get_attribute('innerHTML')
        self.main_page.wait_click(self.main_page.lang_btn)
        post_text = btn.get_attribute('innerHTML')
        self.assertNotEqual(pre_text, post_text, 'Текст не изменился')

    def test_open_modal_log(self):
        self.main_page.click_login()
        is_modal_active = self.main_page.is_exist(self.main_page.modal_window)
        self.assertEqual(is_modal_active, True, 'Модальное окно не открылось')

    def test_open_modal_new_adv(self):
        self.main_page.click_new_adv()
        is_modal_active = self.main_page.is_exist(self.main_page.modal_window)
        self.assertEqual(is_modal_active, True, 'Модальное окно не открылось')

    
    def test_card_search(self):
        self.main_page.fill_input(self.main_page.search_input, 'тест')
        self.main_page.wait_click(self.main_page.search_btn)
        self.main_page.wait_any_redirect('search')
        search_text = self.driver.current_url.split('/')[4]
        search_text = unquote(search_text)
        self.assertEqual(search_text, 'тест', 'Инпут в поиск и страница поиска отличаются')

    def test_username_visible(self):
        self.login()
        self.main_page.wait_click(self.main_page.header_profile)
        is_visible = self.main_page.is_exist(self.main_page.expand_menu)
        self.assertEqual(is_visible, True, 'Нажатие на имя пользователя не открывает меню')
        
    def test_profile_redirection(self):
        self.login()
        self.main_page.wait_click(self.main_page.header_profile)
        self.main_page.wait_click(self.main_page.profile_link)
        is_redirected = self.main_page.wait_redirect('https://volchock.ru/profile')
        self.assertEqual(is_redirected, True, 'Редирект на профиль не выполнен')

    def test_fav_redirection(self):
        self.login()
        self.main_page.wait_click(self.main_page.header_profile)
        self.main_page.wait_click(self.main_page.fav_link)
        is_redirected = self.main_page.wait_redirect('https://volchock.ru/profile/favorite')
        self.assertEqual(is_redirected, True, 'Редирект на избранное не выполнен')

    def test_set_redirection(self):
        self.login()
        self.main_page.wait_click(self.main_page.header_profile)
        self.main_page.wait_click(self.main_page.setting_link)
        is_redirected = self.main_page.wait_redirect('https://volchock.ru/profile/settings')
        self.assertEqual(is_redirected, True, 'Редирект на настройки не выполнен')

    def test_logout(self):
        self.login()
        self.main_page.wait_click(self.main_page.header_profile)
        self.main_page.wait_click(self.main_page.logout_btn)
        is_logout = self.main_page.is_exist(self.main_page.open_modal_btn)
        self.assertEqual(is_logout, True, 'Логаут по нажатию кнопки не выполнен')