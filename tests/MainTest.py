from unicodedata import category
from tests.BaseTest import BaseTest
from tests.pages.MainPage import MainPage

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
        card = self.main_page.wait_render(self.main_page.card)
        card.click()
        self.main_page.wait_any_redirect()
        self.assertEqual(self.driver.current_url.split('/')[3], 
                        'ad',
                        'Названия страниц не совпадают')

    def test_card_empty_search(self):
        self.main_page.fill_input(self.main_page.search_input, 'paskdpasjdauewvbzxcjzlxkcweqoejqeov')
        search_btn = self.main_page.wait_render(self.main_page.search_btn)
        search_btn.click()
        is_empty = self.main_page.is_exist(self.main_page.empty)
        self.assertEqual(is_empty, True, 'Элемент пустой сетки отсутствует')