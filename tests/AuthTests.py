from tests.BaseTest import BaseTest
from tests.helpers import string_generator, cyrillic
from tests.pages.MainPage import MainPage


class SignUpTest(BaseTest):
    def setUp(self):
        # подготавливаем окружение, открываем страницу
        # переходим на страницу логина
        super(SignUpTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.main_page.click_signup()

    # все поля пустые
    def test_empty_fields(self):
        btn = self.main_page.wait_render(self.main_page.reg_submit_btn)
        btn.click()
        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text != ''
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы с пустыми полями')

    # поле логина пустое
    def test_empty_login(self):
        password = string_generator(8)
        btn = self.main_page.wait_render(self.main_page.reg_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        btn.click()

        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text != ''
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы с пустым логином')

    # поле пароля пустое
    def test_empty_password(self):
        login = string_generator(8)
        btn = self.main_page.wait_render(self.main_page.reg_submit_btn)
        self.main_page.fill_input(self.main_page.auth_login_input, login)
        btn.click()

        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text != ''
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы с пустым паролем')

    # регистрация с уже занятым логином
    def test_existing_login(self):
        password = string_generator(8)
        login = self.login
        btn = self.main_page.wait_render(self.main_page.reg_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)

        btn.click()
        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text != ''
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы с уже занятым логином')

    # логин слишком короткий
    def test_short_login(self):
        password = string_generator(8)
        login = string_generator(2)
        btn = self.main_page.wait_render(self.main_page.reg_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)

        btn.click()
        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text is not None
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы со слишком коротким логином')

    # пароль слишком короткий
    def test_short_password(self):
        password = string_generator(5)
        login = string_generator(5)
        btn = self.main_page.wait_render(self.main_page.reg_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)

        btn.click()
        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text is not None
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы со слишком коротким паролем')

    # пароль слишком длинный
    def test_too_long_password(self):
        password = string_generator(50)
        login = string_generator(5)
        btn = self.main_page.wait_render(self.main_page.reg_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)

        btn.click()
        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text is not None

        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы со слишком длинным паролем')

    # корректный ввод
    def test_valid_latin(self):
        password = string_generator(10)
        login = string_generator(5)
        btn = self.main_page.wait_render(self.main_page.reg_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)
        btn.click()
        isCorrect = self.main_page.wait_redirect(self.main_page.BASE_URL)
        self.assertTrue(isCorrect, 'Не происходит редирект на главную '
                                   'после успешной регистрации')

    # корректный ввод (кириллица)
    def test_valid_cyrillic(self):
        password = string_generator(10, cyrillic)
        login = string_generator(5, cyrillic)
        btn = self.main_page.wait_render(self.main_page.reg_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)

        btn.click()
        isCorrect = self.main_page.wait_redirect(self.main_page.BASE_URL)
        self.assertTrue(isCorrect, 'Не происходит редирект на главную '
                                   'после успешной регистрации')


class LoginTest(BaseTest):
    def setUp(self):
        # подготавливаем окружение, открываем страницу
        # переходим на страницу логина
        super(LoginTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.main_page.click_login()


    # все поля пустые
    def test_empty_fields(self):
        btn = self.main_page.wait_render(self.main_page.auth_submit_btn)
        btn.click()
        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text is not None or error_block.text != ""
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы с пустыми полями')

    # поле логина пустое
    def test_empty_login(self):
        password = string_generator(8)
        btn = self.main_page.wait_render(self.main_page.auth_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)

        btn.click()
        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text is not None or error_block.text != ""
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы с пустым логином')

    # поле пароля пустое
    def test_empty_password(self):
        login = string_generator(8)
        btn = self.main_page.wait_render(self.main_page.auth_submit_btn)
        self.main_page.fill_input(self.main_page.auth_login_input, login)

        btn.click()
        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text is not None or error_block.text != ""
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы с пустым паролем')

    # некорректная пара логин-пароль
    def test_incorrect_pair(self):
        password = string_generator(8)
        login = string_generator(8)
        btn = self.main_page.wait_render(self.main_page.auth_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)

        btn.click()
        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text is not None or error_block.text != ""
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы с неправильной парой логин-пароль')

    # логин слишком короткий
    def test_short_login(self):
        password = string_generator(8)
        login = string_generator(2)
        btn = self.main_page.wait_render(self.main_page.auth_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)

        btn.click()
        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text is not None or error_block.text != ""
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы со слишком коротким логином')

    # пароль слишком короткий
    def test_short_password(self):
        password = string_generator(5)
        login = string_generator(5)
        btn = self.main_page.wait_render(self.main_page.auth_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)

        btn.click()
        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text is not None or error_block.text != ""
        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы со слишком коротким паролем')

    # пароль слишком длинный
    def test_too_long_password(self):
        password = string_generator(50)
        login = string_generator(5)
        btn = self.main_page.wait_render(self.main_page.auth_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)

        btn.click()
        error_block = self.main_page.wait_render(self.main_page.error_block)
        isCorrect = error_block.text is not None or error_block.text != ""

        self.assertTrue(isCorrect, 'Не отображается сообщение об ошибке '
                                   'при отправке формы со слишком длинным паролем')

    # корректный ввод
    def test_valid_latin(self):
        password = self.password
        login = self.login
        btn = self.main_page.wait_render(self.main_page.auth_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)

        btn.click()
        isCorrect = self.main_page.wait_redirect(self.main_page.BASE_URL)
        self.assertTrue(isCorrect, 'Не происходит редирект на главную '
                                   'после успешной авторизации')

    # корректный ввод (кириллица)
    def test_valid_cyrillic(self):
        password = self.password_cyr
        login = self.login_cyr
        btn = self.main_page.wait_render(self.main_page.auth_submit_btn)
        self.main_page.fill_input(self.main_page.auth_password_input, password)
        self.main_page.fill_input(self.main_page.auth_login_input, login)

        btn.click()
        isCorrect = self.main_page.wait_redirect(self.main_page.BASE_URL)

        self.assertTrue(isCorrect, 'Не происходит редирект на главную '
                                   'после успешной авторизации')
