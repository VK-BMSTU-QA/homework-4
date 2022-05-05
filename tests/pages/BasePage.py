from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from ..urls import *


class BasePage(Urls):
    # блок ключевых элементов
    # кнопки навбара
    login_btn = ".login"
    signup_btn = ".signup"

    #
    search_btn = ".container-new-search__input"
    player_btn = ".film-first-play__btn"
    close_search_btn = ".search-icon__ico"
    root_search = ".root__search"

    new_film = ".films-content__img"
    popular_film = ".films-content__img"

    film_info_btn = ".film-first-info__btn"

    genre_comedy = ".genres-content__column"

    carousel_item = ".carousel-content__item"
    carousel_item_text = ".carousel-item__text"

    film_about_item = ".film-about-title__text"
    actor_about_item = ".actor-title__text"

    search_input = ".container-new-search__input"

    player_panel = ".player-panel"

    # кнопки формы регистрации
    auth_submit_btn = ".auth-signup__btn"
    reg_submit_btn = ".auth-registration__btn"

    # инпуты формы регистрации и авторизации
    auth_login_input = '#auth-login'
    auth_password_input = '#auth-password'

    # блок сообщения об ошибке
    error_block = '#error'


    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    def wait_visible(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout, ignored_exceptions=self.ignored_exceptions).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_render(self, selector, timeout=10):
        elem = self.wait_visible(selector)
        return WebDriverWait(self.driver, timeout, ignored_exceptions=self.ignored_exceptions).until(
            EC.element_to_be_clickable(elem))

    def wait_redirect(self, url, timeout=60):
        return WebDriverWait(self.driver, timeout, ignored_exceptions=self.ignored_exceptions).until(
            EC.url_matches(url))

    def fill_input(self, selector, text):
        text_input = self.wait_render(selector)
        text_input.send_keys(text)