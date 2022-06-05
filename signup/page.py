from base_page import BasePage
from signup.static_locators import *


class SignUpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_login(self, login):
        element_login = self.get_element_by_class(login_input_locator)
        element_login.send_keys(login)

    def fill_email(self, email):
        element_email = self.get_element_by_class(email_input_locator)
        element_email.send_keys(email)

    def fill_password(self, password):
        element_password = self.get_element_by_class(password_input_locator)
        element_password.send_keys(password)

    def fill_password_confirm(self, password):
        element_password_repeat = self.get_element_by_class(password_confirm_input_locator)
        element_password_repeat.send_keys(password)

    def click_submit_button(self):
        element_button = self.get_element_by_class(auth_button_locator)
        element_button.click()

    def wait_error(self):
        return self.get_element_by_class(auth_error_locator).text

    def click_on_signin_link(self):
        element_signup_link = self.get_element_by_class(signup_link_locator)
        element_signup_link.click()

    def get_signup_title(self):
        return self.get_element_by_css_selector(signup_title_locator).text
