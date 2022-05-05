from selenium.webdriver.common.by import By

from tests.BaseTest import BaseTest
from tests.helpers import string_generator, cyrillic
from tests.pages.MainPage import MainPage

from selenium import webdriver

class FilmPageTest(BaseTest):
    def setUp(self):
        # подготавливаем окружение, открываем страницу
        # переходим на страницу логина
        super(FilmPageTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.main_page.click_first_film_info()

    def setUpAuth(self):
        self.main_page.click_login()
        password = 'dddddd'
        login = 'dddddd'
        btn = self.main_page.wait_render(self.main_page.auth_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)
        btn.click()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.main_page.click_first_film_info()

    def setUpSignUp(self):
        self.main_page.click_signup()
        password = string_generator(10, cyrillic)
        login = string_generator(5, cyrillic)
        btn = self.main_page.wait_render(self.main_page.reg_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)
        btn.click()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.main_page.click_first_film_info()

    def tearDown(self):
        pass

    # Страница фильма. При нажатии на кнопку смотреть открывается страница плеера.
    def test_watch_click(self):
        watch_btn = self.main_page.wait_render('.btn-watch')
        watch_btn.click()
        player_block = self.main_page.wait_render('.player')
        isCorrect = player_block is not None
        self.assertTrue(isCorrect, '')

    # Страница фильма. При нажатии на жанр фильма открывается страница жанра.
    def test_genre_click(self):
        genre_btn = self.main_page.wait_render('.genres')
        genre_btn.click()
        film_block = self.main_page.wait_render('.films-genres-title__text')
        isCorrect = film_block.text is not None
        self.assertTrue(isCorrect, '')

    # Страница фильма. При наведении на жанр фильма в разделе Информация, подчеркивающая жанр линия меняет цвет.
    def test_genre_info_move(self):
        genre_btn = self.main_page.wait_render('.genres')
        prev_color = genre_btn.value_of_css_property("text-decoration-color")
        webdriver.ActionChains(self.driver).move_to_element(genre_btn).perform()
        self.assertNotEqual(genre_btn.value_of_css_property("text-decoration-color"), prev_color)

    # # Страница фильма. При наведении на ссылку на актера, подчеркивающая ссылку линия меняет цвет.
    def test_actor_link(self):
        actor_link = self.main_page.wait_render('.actor_link_root-actors')
        prev_color = actor_link.value_of_css_property("text-decoration-color")
        webdriver.ActionChains(self.driver).move_to_element(actor_link).perform()
        self.assertFalse(actor_link.value_of_css_property("text-decoration-color") == prev_color)

    # Страница фильма. При наведении на кнопку `смотреть позже` у неавторизованного пользователя появляется окно с подсказкой, что нужно авторизоваться.
    def test_watch_later_unauth(self):
        watch_btn = self.main_page.wait_render('.info-b')
        webdriver.ActionChains(self.driver).move_to_element(watch_btn).perform()
        script = "return window.getComputedStyle(document.querySelector('.info-b'),':after').getPropertyValue('content')"
        content = self.driver.execute_script(script, None)
        self.assertTrue(content == '"Только для авторизованных пользователей."')

    # # Страница фильма. При наведении на кнопку `Like` у неавторизованного пользователя появляется окно с подсказкой, что нужно авторизоваться.
    def test_like_btn_unauth(self):
        like_btn = self.main_page.wait_render('.re-like')
        webdriver.ActionChains(self.driver).move_to_element(like_btn).perform()
        script = "return window.getComputedStyle(document.querySelector('.re-like'),':after').getPropertyValue('content')"
        content = self.driver.execute_script(script, None)
        self.assertTrue(content == '"Только для авторизованных пользователей."')

    # # Страница фильма. При наведении на окно рейтинга фильма у неавторизованного пользователя, появляется окно с подсказкой, что нужно авторизоваться.
    def test_rating_move(self):
        star_btn = self.main_page.wait_render('.rating-star__text')
        star_btn.click()
        script = "return window.getComputedStyle(document.querySelector('.re-like'),':after').getPropertyValue('content')"
        content = self.driver.execute_script(script, None)
        self.assertTrue(content == '"Только для авторизованных пользователей."')

    # # # Страница фильма. При нажатии на кнопку `Like` авторизованного пользователя кнопка меняет цвет.
    def test_like_auth(self):
        self.setUpAuth()
        wl_btn = self.main_page.wait_render(".re-like")
        prev_color = wl_btn.value_of_css_property("background")
        wl_btn.click()
        self.assertNotEqual(wl_btn.value_of_css_property("background"), prev_color)

    # Страница фильма. При нажатии на кнопку `смотреть позже` у авторизованного пользователя кнопка меняет цвет.
    def test_watch_later_auth(self):
        self.setUpAuth()
        wl_btn = self.main_page.wait_render(".wl")
        prev_color = wl_btn.value_of_css_property("background")
        wl_btn.click()
        wl_btn_after = self.main_page.wait_render(".wl", 5)
        self.assertNotEqual(wl_btn_after.value_of_css_property("background"), prev_color)
    # Страница фильма. При нажатие на звездочку рейтинга фильма у авторизованного пользователя, все звездочки до выбранной меняют цвет.
    def test_star_click(self):
        self.setUpSignUp()
        star_btn = self.main_page.wait_render(".rating-star__text")
        prev_color = star_btn.value_of_css_property("color")
        star_btn.click()
        wl_btn_after = self.main_page.wait_render(".star-select-user", 5)
        self.assertNotEqual(wl_btn_after.value_of_css_property("color"), prev_color)
