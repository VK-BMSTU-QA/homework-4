from components.login_form import LoginForm
from page_objects.base import Page


class LoginPage(Page):
    BASE_URL = 'http://pyaterochka-team.site/'
    PATH = 'signin'

    def __init__(self, driver):
        super().__init__(driver)
        self.login_form = LoginForm(driver)

    def login(self, login, password):
        self.login_form.fill_login(login)
        self.login_form.fill_password(password)
        self.login_form.submit()

    def logout(self):
        self.login_form.open_navbar()
        self.login_form.click_logout_navbar()
        self.login_form.click_logout_confirm()

    def get_email(self):
        return self.login_form.get_email_header()

    def get_error(self):
        return self.login_form.get_error()
