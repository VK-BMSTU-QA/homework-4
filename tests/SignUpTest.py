from tests.BaseTest import BaseTest
from tests.pages.MainPage import MainPage


class SignUpTest(BaseTest):
    def setUp(self):
        super(SignUpTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.main_page.click_login()
        self.main_page.switch_to_reg()

    def test_reg_correct(self):
        self.main_page.fill_reg_email(self.reg_mail)
        self.main_page.fill_reg_name(self.reg_name)
        self.main_page.fill_reg_surname(self.reg_surname)
        self.main_page.fill_reg_password(self.reg_password)
        self.main_page.fill_reg_passwordRep(self.reg_password)
        self.main_page.click_reg_button()
        is_logged = self.main_page.is_logged()
        self.assertTrue(is_logged,
                        'Ошибка регистрации при корректных данных')

    def test_reg_email(self):
        self.main_page.click_reg_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Нет ошибки в регистрации при пустом email')

        self.main_page.fill_reg_email('testtest')
        self.main_page.click_reg_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Нет ошибки в регистрации при неверном формате email')
        self.main_page.clear_reg_email()

        self.main_page.fill_reg_email(self.reg_mail)
        self.main_page.click_reg_button()
        is_correct = self.main_page.check_reg_email_correct()
        self.assertTrue(is_correct,
                        'Ошибки в регистрации при верном формате email')

    def test_reg_name(self):
        self.main_page.fill_reg_email(self.reg_mail)
        self.main_page.click_reg_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Нет ошибки в регистрации при пустом имени')

        self.main_page.fill_reg_name('a')
        self.main_page.click_reg_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Нет ошибки в регистрации при коротком имени')
        self.main_page.clear_reg_name()

        self.main_page.fill_reg_name('a<>?')
        self.main_page.click_reg_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Нет ошибки в регистрации при недопустимах символах в имени')
        self.main_page.clear_reg_name()

        self.main_page.fill_reg_name(self.reg_name)
        self.main_page.click_reg_button()
        is_correct = self.main_page.check_reg_name_correct()
        self.assertTrue(is_correct,
                        'Ошибки в регистрации при верном формате имени')

    def test_reg_surname(self):
        self.main_page.fill_reg_email(self.reg_mail)
        self.main_page.fill_reg_name(self.reg_name)
        self.main_page.click_reg_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Нет ошибки в регистрации при пустой фамилии')

        self.main_page.fill_reg_surname('a')
        self.main_page.click_reg_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Нет ошибки в регистрации при короткой фамилии')
        self.main_page.clear_reg_surname()

        self.main_page.fill_reg_surname('a<>?')
        self.main_page.click_reg_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Нет ошибки в регистрации при недопустимах символах в фамилии')
        self.main_page.clear_reg_surname()

        self.main_page.fill_reg_surname(self.reg_surname)
        self.main_page.click_reg_button()
        is_correct = self.main_page.check_reg_surname_correct()
        self.assertTrue(is_correct,
                        'Ошибки в регистрации при верном формате фамилии')

    def test_reg_password(self):
        self.main_page.fill_reg_email(self.reg_mail)
        self.main_page.fill_reg_name(self.reg_name)
        self.main_page.fill_reg_password(self.reg_password)
        self.main_page.click_reg_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Нет ошибки в регистрации при пустом пароле')

        self.main_page.fill_reg_password('pas')
        self.main_page.click_reg_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Нет ошибки в регистрации при коротком пароле')
        self.main_page.clear_reg_password()

        self.main_page.fill_reg_password(self.correct_password)
        self.main_page.click_reg_button()
        is_correct = self.main_page.check_reg_password_correct()
        self.assertTrue(is_correct,
                        'Ошибки в регистрации при верном формате пароля')

    def test_reg_password_missmatch(self):
        self.main_page.fill_reg_email(self.reg_mail)
        self.main_page.fill_reg_name(self.reg_name)
        self.main_page.fill_reg_password(self.reg_password)
        self.main_page.fill_reg_passwordRep("missmatchedpassword")
        self.main_page.click_reg_button()
        is_error = self.main_page.check_error()
        self.assertTrue(is_error,
                        'Нет ошибки в регистрации при разных паролях')

    def test_reg_used_email(self):
        self.main_page.fill_reg_email(self.correct_login)
        self.main_page.fill_reg_name(self.reg_name)
        self.main_page.fill_reg_surname(self.reg_surname)
        self.main_page.fill_reg_password(self.reg_password)
        self.main_page.fill_reg_passwordRep(self.reg_password)
        self.main_page.click_reg_button()
        is_logged = self.main_page.is_logged()
        self.assertFalse(is_logged,
                         'Произошла регистрация при существующей почте')
