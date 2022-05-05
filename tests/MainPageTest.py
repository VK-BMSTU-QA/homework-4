import os

from tests.BaseTest import BaseTest
from tests.helpers import string_generator, cyrillic
from tests.pages.MainPage import MainPage

class MainPageTest(BaseTest):
    def setUp(self):
        # подготавливаем окружение, открываем страницу
        super(MainPageTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()

    def tearDown(self):
        pass

    # Главная страница. Нажатие на кнопку play открывает страницу плеера.
    def test_player_open(self):
        self.main_page.click_player()
        player_block = self.main_page.wait_render('.player')
        isCorrect = player_block is not None
        self.assertTrue(isCorrect, '')

    # Главная страница. Нажатие на кнопку info открывает страницу фильма.
    def test_info_click(self):
        self.main_page.click_first_film_info()
        film_block = self.main_page.wait_render('.film-about')
        isCorrect = film_block.text is not None
        self.assertTrue(isCorrect, '')


    # Главная страница. Нажатие на икноку жанра открывает страницу жанра.
    def test_genres_open(self):
        self.main_page.click_genre_comedy()
        film_block = self.main_page.wait_render('.films-genres-title__text')
        isCorrect = film_block.text is not None
        self.assertTrue(isCorrect, '')

    # Главная страница. Нажатие на иконку фильма из раздела Новое на Lime TV открывает страницу фильма. TODO
    def test_new_open(self):
        self.main_page.click_new_film()
        film_block = self.main_page.wait_render('.film-about-title__text')
        isCorrect = film_block.text is not None
        self.assertTrue(isCorrect, '')

    # # Главная страница. Нажатие на иконку фильма из раздела Популярное на Lime TV открывает страницу фильма. TODO
    def test_popular_open(self):
        self.main_page.click_popular_film()
        film_block = self.main_page.wait_render('.film-about-title__text')
        isCorrect = film_block.text is not None
        self.assertTrue(isCorrect, '')
