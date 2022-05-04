from Base.BasePage import Page
from Register.RegisterComponents import RegisterForm


class RegisterPage(Page):
    PATH = "signup"

    @property
    def form(self):
        return RegisterForm(self.driver)
