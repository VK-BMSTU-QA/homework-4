from Base.BasePage import Page
from Login.LoginComponents import LoginForm


class LoginPage(Page):
    PATH = "signin"

    @property
    def form(self):
        return LoginForm(self.driver)

    def login(self, email, password):
        self.open()

        login_form = self.form
        login_form.set_email(email)
        login_form.set_password(password)
        login_form.login()
        login_form.check_login()
