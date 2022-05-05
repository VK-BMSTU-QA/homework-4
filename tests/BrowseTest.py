from tests.BaseTest import BaseTest
from tests.helpers import string_generator, cyrillic
from tests.pages.MainPage import MainPage


class BrowseTest(BaseTest):
    def setUp(self):
        # подготавливаем окружение, открываем страницу
        super(BrowseTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.main_page.click_search()

    def tearDown(self):
        pass

    # Поиск. Нажатие на кнопку exit возвращает на страницу из которой открывается поиск.
    def test_exit(self):
        btn = self.main_page.wait_render(self.main_page.close_search_btn)
        btn.click()
        main_block = self.main_page.wait_render(".film-first-title__text")
        isCorrect = main_block is not None
        self.assertTrue(isCorrect, '')

    # Поиск. При вводе текста в поле поиска на странице появляются иконки фильмов с названием.
    def test_text_input_films(self):
        film_name = "Острые козырьки"
        self.main_page.fill_input(self.main_page.search_input, film_name)

        film_item = self.main_page.wait_render(self.main_page.carousel_item_text)
        isCorrect = film_item.text is not None
        self.assertTrue(isCorrect, '')

    # Поиск. При вводе текста в поле поиска на странице появляются иконки актеров с их именем.
    def test_text_input_actors(self):
        actor_name = "Пол"
        self.main_page.fill_input(self.main_page.search_input, actor_name)

        actor_item = self.main_page.wait_render(self.main_page.carousel_item_text)
        isCorrect = actor_item.text is not None
        self.assertTrue(isCorrect, '')

    # Поиск. При нажатии на иконку фильма открывается страница фильма.
    def test_click_film(self):
        film_name = "Острые козырьки"
        self.main_page.fill_input(self.main_page.search_input, film_name)

        film_item = self.main_page.wait_render(self.main_page.carousel_item_text)
        isCorrect = film_item.text is not None
        self.assertTrue(isCorrect, '')
        film_item.click()

        film_item = self.main_page.wait_render(self.main_page.film_about_item)
        isCorrect = film_item.text is not None
        self.assertTrue(isCorrect, '')

    # Поиск. При нажатии на иконку актера открывается страница актера.
    def test_click_actor(self):
        actor_name = "Пол"
        self.main_page.fill_input(self.main_page.search_input, actor_name)

        actor_item = self.main_page.wait_render(self.main_page.carousel_item_text)
        isCorrect = actor_item.text is not None
        self.assertTrue(isCorrect, '')
        actor_item.click()

        actor_item = self.main_page.wait_render(".page-title__text")
        isCorrect = actor_item.text is not None
        self.assertTrue(isCorrect, '')
