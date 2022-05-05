from selenium.webdriver.common.by import By

from tests.BaseTest import BaseTest
from tests.helpers import string_generator, cyrillic
from tests.pages.MainPage import MainPage

from selenium import webdriver

class ActorPageTest(BaseTest):
    def setUp(self):
        # подготавливаем окружение, открываем страницу
        # переходим на страницу логина
        super(ActorPageTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        actor_name = "Пол"
        self.main_page.fill_input(self.main_page.search_input, actor_name)
        item = self.main_page.wait_render(self.main_page.carousel_item_text)
        item.click()

    def tearDown(self):
        pass

    # Страница актера. При нажатии на жанр открывается страница выбранного жанра.
    def test_genre_click(self):
        genre_link = self.main_page.wait_render(".actor-name__text")
        genre_link.click()
        film_block = self.main_page.wait_render('.films-genres-title__text')
        isCorrect = film_block.text is not None
        self.assertTrue(isCorrect, '')

    # Страница актера. При наведении на жанр фильма подчеркивающая жанр линия меняет цвет.
    def test_genre_link_color(self):
        genre_link = self.main_page.wait_render(".actor-name__text")
        prev_color = genre_link.value_of_css_property("color")
        webdriver.ActionChains(self.driver).move_to_element(genre_link).perform()
        self.assert_(genre_link.value_of_css_property("color"), prev_color)

    # Страница актера. При нажатии на иконку фильма открывается страница выбранного фильма.
    def test_film_icon_click(self):
        film_item = self.main_page.wait_render('.films-content__img')
        film_item.click()
        film_block = self.main_page.wait_render('.film-about-title__text')
        isCorrect = film_block.text is not None
        self.assertTrue(isCorrect, '')
