from selenium.webdriver.common.by import By

from tests.BaseTest import BaseTest
from tests.helpers import string_generator, cyrillic
from tests.pages.MainPage import MainPage

from selenium import webdriver

class NavbarTest(BaseTest):
    def setUp(self):
        # подготавливаем окружение, открываем страницу
        # переходим на страницу логина
        super(NavbarTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()

    def tearDown(self):
        pass

# Навигационная панель. При нажатии на иконку сайта открывается главная страница.
    def test_main_icon_click(self):
        logo = self.main_page.wait_render(".logo")
        logo.click()
        main_block = self.main_page.wait_render(".film-first-title__text")
        isCorrect = main_block is not None
        self.assertTrue(isCorrect, '')

    # Навигационная панель. При нажатии на окно поиска открывается страница поиска.
    def test_search_btn_color(self):
        self.main_page.click_search()
        closebtn = self.main_page.wait_render(self.main_page.close_search_btn)
        isCorrect = closebtn is not None
        self.assertTrue(isCorrect, '')

    # Навигационная панель. При наведении на кнопку `войти`, кнопка меняет цвет.
    def test_login_btn_color(self):
        login_btn = self.main_page.wait_render(".login")
        prev_color = login_btn.value_of_css_property("color")
        webdriver.ActionChains(self.driver).move_to_element(login_btn).perform()
        self.assert_(login_btn.value_of_css_property("color"), prev_color)


    # Навигационная панель. При наведении на кнопку `регистрация`, кнопка меняет цвет.
    def test_signup_btn_color(self):
        login_btn = self.main_page.wait_render(".signup")
        prev_color = login_btn.value_of_css_property("color")
        webdriver.ActionChains(self.driver).move_to_element(login_btn).perform()
        self.assert_(login_btn.value_of_css_property("color"), prev_color)
