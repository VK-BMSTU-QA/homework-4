from base_page import BasePage
from signin.static_locators import *


class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_login(self, login):
        element_login = self.get_element_by_class(login_input_locator)
        element_login.send_keys(login)

    def fill_password(self, password):
        self.wait_item_disappear(login_input_locator)
        element_password = self.get_element_by_class(password_input_locator)
        element_password.send_keys(password)

    def click_button(self):
        element_button = self.get_element_by_class(auth_button_locator)
        element_button.click()

    # def wait_error(self):
    #     return self.get_element_by_class(auth_error_locator).text
