import os

from tests.BaseTest import BaseTest
from tests.helpers import generate_pic, delete_pic, string_generator
from tests.pages.MainPage import MainPage
from tests.pages.ProfilePage import ProfilePage


class ProfileTest(BaseTest):
    # сетап: логин, переход на страницу профиля
    def setUp(self):
        super(ProfileTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()

        # пререквизит
        elem = self.main_page.wait_render(self.main_page.login_btn)
        elem.click()

        # no offence
        password = self.password_cyr
        login = self.login_cyr

        btn = self.main_page.wait_render(self.main_page.auth_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)
        btn.click()

        # переход на страницу профиля
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.open()

    # проверка редиректа на страницу настройки
    def test_settings_redirect(self):
        btn = self.profile_page.wait_render(self.main_page.settings_btn)
        btn.click()
        isCorrect = self.main_page.wait_redirect(self.main_page.SETTINGS_URL)
        self.assertTrue(isCorrect, 'Не происходит редирект на страницу настроек')

    # проверка редиректа на страницу оплаты
    def test_payments_redirect(self):
        btn = self.profile_page.wait_render(self.main_page.payment_btn)
        btn.click()
        # fuzzy match inside
        isCorrect = self.main_page.wait_redirect(self.main_page.PAYMENT_URL)
        self.assertTrue(isCorrect, 'Не происходит редирект на страницу оплаты')

    # проверка обновления аватара
    def test_settings_userpic(self):
        generate_pic()
        btn = self.profile_page.wait_render(self.main_page.settings_btn)
        btn.click()

        isCorrect = self.main_page.wait_redirect(self.main_page.SETTINGS_URL)
        self.assertTrue(isCorrect, '')
        self.profile_page.fill_image_input(os.getcwd(), 'test.png')
        message_block = self.profile_page.wait_render(self.profile_page.success_block)
        isCorrect = message_block.text != ''
        self.assertTrue(isCorrect, 'Не происходит обновление аватара пользователя')
        delete_pic()

    # проверка обновления аватара со слишком большим файлом
    def test_settings_userpic_too_big(self):
        generate_pic('test.png', 1000, 1000)
        btn = self.profile_page.wait_render(self.main_page.settings_btn)
        btn.click()

        isCorrect = self.main_page.wait_redirect(self.main_page.SETTINGS_URL)
        self.assertTrue(isCorrect, '')
        self.profile_page.fill_image_input(os.getcwd(), 'test.png')
        message_block = self.profile_page.wait_render(self.profile_page.error_block)
        isCorrect = message_block.text != ''
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке слишком большого файла')
        delete_pic()

    # обновление пароля, пароль слишком короткий
    def test_settings_password_short(self):
        btn = self.profile_page.wait_render(self.main_page.settings_btn)
        btn.click()
        upd = self.profile_page.wait_render(self.main_page.update_password)
        password = string_generator(5)
        self.profile_page.fill_input(self.main_page.update_password_input, password)
        upd.click()

        message_block = self.profile_page.wait_render(self.profile_page.error_block)
        isCorrect = message_block.text != self.message_ok_pass

        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке слишком короткого пароля')

    # обновление пароля, пароль слишком длинный
    def test_settings_password_long(self):
        generate_pic()
        btn = self.profile_page.wait_render(self.main_page.settings_btn)
        btn.click()
        upd = self.profile_page.wait_render(self.main_page.update_password)
        password = string_generator(50)
        self.profile_page.fill_input(self.main_page.update_password_input, password)
        upd.click()

        message_block = self.profile_page.wait_render(self.profile_page.error_block)
        isCorrect = message_block.text != self.message_ok_pass
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке слишком длинного пароля')

    # обновление пароля
    def test_settings_password(self):
        generate_pic()
        btn = self.profile_page.wait_render(self.main_page.settings_btn)
        btn.click()

        upd = self.profile_page.wait_render(self.main_page.update_password)
        self.profile_page.fill_input(self.main_page.update_password_input, self.password_cyr)
        upd.click()

        message_block = self.profile_page.wait_render(self.profile_page.success_block)
        isCorrect = message_block.text == self.message_ok_pass
        self.assertTrue(isCorrect, 'Не отображается сообщение '
                                   'об успешном обновлении пароля')

    # обновление описания
    def test_settings_description(self):
        generate_pic()
        btn = self.profile_page.wait_render(self.main_page.settings_btn)
        btn.click()

        upd = self.profile_page.wait_render(self.main_page.update_description)
        description = string_generator(50)
        self.profile_page.fill_input(self.main_page.update_description_input, description)
        upd.click()

        message_block = self.profile_page.wait_render(self.profile_page.success_block)
        isCorrect = message_block.text == self.message_ok_desc

        self.assertTrue(isCorrect, 'Не отображается сообщение '
                                   'об успешном обновлении описания')
