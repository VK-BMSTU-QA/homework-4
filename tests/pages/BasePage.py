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

    # кнопки формы регистрации
    auth_submit_btn = ".auth-signup__btn"
    reg_submit_btn = ".auth-registration__btn"

    # инпуты формы регистрации и авторизации
    auth_login_input = '#auth-login'
    auth_password_input = '#auth-password'

    # блок сообщения об ошибке
    error_block = '#error'
    error_msg = '.error'
    success_block = '#success'
    success_msg = '.success'

    # блок оплаты
    payment_btn = '.subscription__button'
    settings_btn = '.profile-settings__ico'

    # кнопка аватарки
    update_userpic = '.profile-info-avatar'
    update_password = '.profile-info-save__btn'
    update_password_input = '.profile-info-pass__input'
    update_description = '.about_save_btn'
    update_description_input = '.profile-info-bio__textarea'

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
            EC.url_contains(url))

    def fill_input(self, selector, text):
        text_input = self.wait_render(selector)
        text_input.send_keys(text)

    def fill_image_input(self, image):
        img_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.update_userpic)))
        img_input.send_keys(image)