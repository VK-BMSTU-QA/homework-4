from tests.BaseTest import BaseTest
from tests.pages.MainPage import MainPage

class LoginTest(BaseTest):
    def setUp(self):
        super(LoginTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.main_page.click_login()

    def test_log_empty_email(self):
        login_btn = self.main_page.wait_render(self.main_page.login_btn)
        login_btn.click()
        login_email_div = self.main_page.wait_render(self.main_page.login_email_div)
        is_error = "text-input_wrong" in login_email_div.get_attribute("class")
        self.assertEqual(is_error, True, 
                        'Поле ввода email логина не показывает ошибки при пустой почте'
                        )

    def test_log_broken_email(self):
        login_email_input = self.main_page.wait_render(self.main_page.login_email_input)
        login_email_input.send_keys('testtest')
        login_btn = self.main_page.wait_render(self.main_page.login_btn)
        login_btn.click()
        login_email_div = self.main_page.wait_render(self.main_page.login_email_div)
        is_error = "text-input_wrong" in login_email_div.get_attribute("class")
        self.assertEqual(is_error, True, 
                        'Поле ввода email логина не показывает ошибки при некорректной почте'
                        )

    def test_log_empty_password(self):
        login_email_input = self.main_page.wait_render(self.main_page.login_email_input)
        login_email_input.send_keys(self.correct_login)
        login_btn = self.main_page.wait_render(self.main_page.login_btn)
        login_btn.click()
        login_password_div = self.main_page.wait_render(self.main_page.login_password_div)
        is_error = "text-input_wrong" in login_password_div.get_attribute("class")
        self.assertEqual(is_error, True, 
                        'Поле ввода пароля логина не показывает ошибки при пустом инпуте'
                        )

    def test_log_no_user(self):
        login_email_input = self.main_page.wait_render(self.main_page.login_email_input)
        login_email_input.send_keys('somenonexistendstrongmail@mail.ru')
        login_pass_input = self.main_page.wait_render(self.main_page.login_password_input)
        login_pass_input.send_keys('somepassword')
        login_btn = self.main_page.wait_render(self.main_page.login_btn)
        login_btn.click()
        is_error = self.main_page.is_exist(self.main_page.input_err)
        self.assertEqual(is_error, True, 
                        'Поле ввода email логина не показывает ошибки при несуществующем пользователе'
                        )

    
    def test_log_correct(self):
        login_email_input = self.main_page.wait_render(self.main_page.login_email_input)
        login_email_input.send_keys(self.correct_login)
        login_pass_input = self.main_page.wait_render(self.main_page.login_password_input)
        login_pass_input.send_keys(self.correct_password)

        login_btn = self.main_page.wait_render(self.main_page.login_btn)
        login_btn.click()
        is_logged = self.main_page.is_exist(self.main_page.header_profile)
        self.assertEqual(is_logged, True, 
                        'Ошибка авторизации при корректных данных'
                        )

    def test_reg_empty(self):
        to_reg_btn = self.main_page.wait_render(self.main_page.swith_to_reg_btn)
        to_reg_btn.click()

        reg_btn = self.main_page.wait_render(self.main_page.reg_btn)
        reg_btn.click()

        email_div = self.main_page.wait_render(self.main_page.reg_email_div)
        is_error = "text-input_wrong" in email_div.get_attribute("class")
        self.assertEqual(is_error, True, 
                        'Нет ошибки в регистрации при пустом email'
                        )

    def test_reg_broken_email(self):
        to_reg_btn = self.main_page.wait_render(self.main_page.swith_to_reg_btn)
        to_reg_btn.click()

        email_input = self.main_page.wait_render(self.main_page.reg_email_input)
        email_input.send_keys('testtest')

        reg_btn = self.main_page.wait_render(self.main_page.reg_btn)
        reg_btn.click()

        email_div = self.main_page.wait_render(self.main_page.reg_email_div)
        is_error = "text-input_wrong" in email_div.get_attribute("class")
        self.assertEqual(is_error, True, 
                        'Нет ошибки в регистрации при неверном формате email'
                        )

    def test_reg_correct_email(self):
        to_reg_btn = self.main_page.wait_render(self.main_page.swith_to_reg_btn)
        to_reg_btn.click()

        email_input = self.main_page.wait_render(self.main_page.reg_email_input)
        email_input.send_keys('zxc@mail.ru')

        reg_btn = self.main_page.wait_render(self.main_page.reg_btn)
        reg_btn.click()

        email_div = self.main_page.wait_render(self.main_page.reg_email_div)
        is_correct = "text-input_correct" in email_div.get_attribute("class")
        self.assertEqual(is_correct, True, 
                        'Ошибки в регистрации при верном формате email'
                        )

    def test_reg_short_name(self):
        to_reg_btn = self.main_page.wait_render(self.main_page.swith_to_reg_btn)
        to_reg_btn.click()

        name_input = self.main_page.wait_render(self.main_page.reg_name_input)
        name_input.send_keys('a')

        reg_btn = self.main_page.wait_render(self.main_page.reg_btn)
        reg_btn.click()

        name_div = self.main_page.wait_render(self.main_page.reg_name_div)
        is_error = "text-input_wrong" in name_div.get_attribute("class")
        self.assertEqual(is_error, True, 
                        'Нет ошибки в регистрации при слишком коротком имени <2'
                        )


    def test_reg_spec_sign_name(self):
        to_reg_btn = self.main_page.wait_render(self.main_page.swith_to_reg_btn)
        to_reg_btn.click()

        name_input = self.main_page.wait_render(self.main_page.reg_name_input)
        name_input.send_keys('aа<>')

        reg_btn = self.main_page.wait_render(self.main_page.reg_btn)
        reg_btn.click()

        name_div = self.main_page.wait_render(self.main_page.reg_name_div)
        is_error = "text-input_wrong" in name_div.get_attribute("class")
        self.assertEqual(is_error, True, 
                        'Нет ошибки в регистрации при спец символах в имени'
                        )

    def test_reg_short_surname(self):
        to_reg_btn = self.main_page.wait_render(self.main_page.swith_to_reg_btn)
        to_reg_btn.click()

        surname_input = self.main_page.wait_render(self.main_page.reg_surname_input)
        surname_input.send_keys('a')

        reg_btn = self.main_page.wait_render(self.main_page.reg_btn)
        reg_btn.click()

        surnname_div = self.main_page.wait_render(self.main_page.reg_surname_div)
        is_error = "text-input_wrong" in surnname_div.get_attribute("class")
        self.assertEqual(is_error, True, 
                        'Нет ошибки в регистрации при слишком короткой фамилии <2'
                        )


    def test_reg_spec_sign_surname(self):
        to_reg_btn = self.main_page.wait_render(self.main_page.swith_to_reg_btn)
        to_reg_btn.click()

        surname_input = self.main_page.wait_render(self.main_page.reg_surname_input)
        surname_input.send_keys('aа<>')

        reg_btn = self.main_page.wait_render(self.main_page.reg_btn)
        reg_btn.click()

        surnname_div = self.main_page.wait_render(self.main_page.reg_surname_div)
        is_error = "text-input_wrong" in surnname_div.get_attribute("class")
        self.assertEqual(is_error, True, 
                        'Нет ошибки в регистрации при спец символах в фамилии'
                        )


    def test_reg_short_password(self):
        to_reg_btn = self.main_page.wait_render(self.main_page.swith_to_reg_btn)
        to_reg_btn.click()

        password_input = self.main_page.wait_render(self.main_page.reg_password_input)
        password_input.send_keys('pass')

        reg_btn = self.main_page.wait_render(self.main_page.reg_btn)
        reg_btn.click()

        password_div = self.main_page.wait_render(self.main_page.reg_password_div)
        is_error = "text-input_wrong" in password_div.get_attribute("class")
        self.assertEqual(is_error, True, 
                        'Нет ошибки в регистрации при слишком коротком пароле'
                        )

    def test_reg_passwords_missmatch(self):
        to_reg_btn = self.main_page.wait_render(self.main_page.swith_to_reg_btn)
        to_reg_btn.click()

        password_input = self.main_page.wait_render(self.main_page.reg_password_input)
        password_input.send_keys('password')

        repassword_input = self.main_page.wait_render(self.main_page.reg_reppassword_input)
        repassword_input.send_keys('password1')

        reg_btn = self.main_page.wait_render(self.main_page.reg_btn)
        reg_btn.click()

        repassword_div = self.main_page.wait_render(self.main_page.reg_reppassword_div)
        is_error = "text-input_wrong" in repassword_div.get_attribute("class")
        self.assertEqual(is_error, True, 
                        'Нет ошибки в регистрации при разных паролях'
                        )

    def test_reg_correct(self):
        to_reg_btn = self.main_page.wait_render(self.main_page.swith_to_reg_btn)
        to_reg_btn.click()

        email_input = self.main_page.wait_render(self.main_page.reg_email_input)
        email_input.send_keys(self.reg_mail)

        name_input = self.main_page.wait_render(self.main_page.reg_name_input)
        name_input.send_keys(self.reg_name)

        surname_input = self.main_page.wait_render(self.main_page.reg_surname_input)
        surname_input.send_keys(self.reg_surname)

        password_input = self.main_page.wait_render(self.main_page.reg_password_input)
        password_input.send_keys(self.reg_password)

        repassword_input = self.main_page.wait_render(self.main_page.reg_reppassword_input)
        repassword_input.send_keys(self.reg_password)

        reg_btn = self.main_page.wait_render(self.main_page.reg_btn)
        reg_btn.click()

        is_logged = self.main_page.is_exist(self.main_page.header_profile)
        self.assertEqual(is_logged, True, 
                        'Ошибка регистрации при корректных данных'
                        )


    def test_reg_passwords_missmatch(self):
        to_reg_btn = self.main_page.wait_render(self.main_page.swith_to_reg_btn)
        to_reg_btn.click()

        password_input = self.main_page.wait_render(self.main_page.reg_password_input)
        password_input.send_keys('password')

        repassword_input = self.main_page.wait_render(self.main_page.reg_reppassword_input)
        repassword_input.send_keys('password1')

        reg_btn = self.main_page.wait_render(self.main_page.reg_btn)
        reg_btn.click()

        repassword_div = self.main_page.wait_render(self.main_page.reg_reppassword_div)
        is_error = "text-input_wrong" in repassword_div.get_attribute("class")
        self.assertEqual(is_error, True, 
                        'Ошибка в регистрации при коррентных данных'
                        )

    def test_reg_correct(self):
        to_reg_btn = self.main_page.wait_render(self.main_page.swith_to_reg_btn)
        to_reg_btn.click()

        email_input = self.main_page.wait_render(self.main_page.reg_email_input)
        email_input.send_keys(self.correct_login)

        name_input = self.main_page.wait_render(self.main_page.reg_name_input)
        name_input.send_keys(self.reg_name)

        surname_input = self.main_page.wait_render(self.main_page.reg_surname_input)
        surname_input.send_keys(self.reg_surname)

        password_input = self.main_page.wait_render(self.main_page.reg_password_input)
        password_input.send_keys(self.reg_password)

        repassword_input = self.main_page.wait_render(self.main_page.reg_reppassword_input)
        repassword_input.send_keys(self.reg_password)

        reg_btn = self.main_page.wait_render(self.main_page.reg_btn)
        reg_btn.click()

        email_div = self.main_page.wait_render(self.main_page.reg_email_div)
        is_error = "text-input_wrong" in email_div.get_attribute("class")
        self.assertEqual(is_error, True, 
                        'Нет ошибки в регистрации при использовании существующего email'
                        )