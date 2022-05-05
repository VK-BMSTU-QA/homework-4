from selenium.webdriver.common.by import By

from tests.BaseTest import BaseTest
from tests.helpers import string_generator, cyrillic
from tests.pages.MainPage import MainPage

from selenium import webdriver

class PlayerTest(BaseTest):
    def setUp(self):
        # подготавливаем окружение, открываем страницу
        # переходим на страницу логина
        super(PlayerTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.main_page.click_player()

    def tearDown(self):
        pass

    # # Плеер. При нажатии на кнопку Play появляется кнопка Stop
    def test_play_toggle(self):
        play_btn = self.main_page.wait_render(".player-start-stop__btn")
        play_btn.click()
        stop_btn = self.main_page.wait_render('.play_stop__pic')
        src = stop_btn.get_attribute("src")
        self.assertTrue(src == 'https://a06367.ru/pause.png')

    # Плеер. При нажатии на кнопку exit (крестик) переход на главную страницу.
    def test_exit(self):
        exit_btn = self.main_page.wait_render('.player-back__icon')
        exit_btn.click()
        start_page = self.main_page.wait_render(".film-first-title__column")
        isCorrect = start_page.text is not None
        self.assertTrue(isCorrect, '')

    # # Плеер. При запуске видео счетчик текущего времени устанавливается в 0.
    def test_time_zero_value(self):
        time_cur_row = self.main_page.wait_render(".player-timeline-current__row")
        self.assert_(time_cur_row.value_of_css_property("width"), '0px')
