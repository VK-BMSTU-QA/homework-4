from tests.BaseTest import BaseTest
from tests.pages.MainPage import MainPage


class LoginTest(BaseTest):
    def setUp(self):
        super(LoginTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.main_page.click_login()

    def test_log_correct(self):
        self.main_page.fill_login_email(self.correct_login)
        self.main_page.fill_login_password(self.correct_password)
        self.main_page.click_login_button()

        is_logged = self.main_page.is_logged()
        self.assertTrue(is_logged,
                        'Ошибка авторизации при корректных данных')

    def test_log_email(self):
        self.main_page.click_login_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Поле ввода email нет ошибки при пустой почте')

        self.main_page.fill_login_email('testtest')
        self.main_page.click_login_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Поле ввода email нет ошибки при ошибке в почте')
        self.main_page.clear_log_inputs()

        self.main_page.fill_login_email('somenonexistendstrongmail@mail.ru')
        self.main_page.fill_login_password('somepassword')
        self.main_page.click_login_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Поле ввода email логина не показывает ошибки при несуществующем пользователе'
                        )

    def test_log_password(self):
        self.main_page.fill_login_email(self.correct_login)
        self.main_page.click_login_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Поле ввода пароля логина не показывает ошибки при пустом инпуте')

        self.main_page.fill_login_password('pass')
        self.main_page.click_login_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Поле ввода пароля логина не показывает ошибки при вводе пароля менее 5 символов')
