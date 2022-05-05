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

    # # Плеер. При движении мыши появляется панель управления видео.
    # def test_move_mouse(self):
    #     pass
    #     # player_panel = self.main_page.wait_render('.player-panel')

    # # Плеер. При нажатии на кнопку Play появляется кнопка Stop
    # def test_play_toggle(self):
    #     play_btn = self.main_page.wait_render(".player-start-stop__btn point")
    #     play_btn.click()
    #     stop_btn = webdriver.Chrome.find_element(By.XPATH, "//img[@src='https://a06367.ru/pause.png']")
    #     isCorrect = stop_btn.text is not None
    #     self.assertTrue(isCorrect, '')

    # Плеер. При нажатии на кнопку exit (крестик) переход на главную страницу.
    def test_exit(self):
        exit_btn = self.main_page.wait_render('.player-back__column')
        exit_btn.click()
        start_page = self.main_page.wait_render(".film-first-title__column")
        isCorrect = start_page.text is not None
        self.assertTrue(isCorrect, '')
    #
    # # Плеер. При запуске видео счетчик текущего времени устанавливается в 0.
    # def test_time_zero_value(self):
    #     player_panel = self.main_page.wait_render(".player-buttons__holder")
    #     webdriver.ActionChains(webdriver).move_to_element(player_panel).perform()
    #     time_cur_row = self.main_page.wait_render(".player-timeline-current__row")
    #     self.assert_(time_cur_row.value_of_css_property("width"), '0px')
