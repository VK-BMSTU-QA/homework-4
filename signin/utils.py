from navbar.page import NavbarPage
from profile.page import ProfilePage
from signin.page import SignInPage
from signup.page import SignUpPage

url = "https://goodvibesazot.tk/signin"

LOGIN = '12345'
PASSWORD = '12345'
LOGIN_NO_USER = 'adasdasdasd'
PASSWORD_INCORRECT = 'sdfsdfsdfsf'
PASSWORD_SHORT = '123'

class TestUtils:
    def __init__(self, driver):
        self.driver = driver
        self.signinPage = SignInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.signupPage = SignUpPage(self.driver)
        self.navbarPage = NavbarPage(self.driver)

    def fill_login(self, login):
        element_login = self.signinPage.get_login_element()
        element_login.send_keys(login)

    def fill_password(self, password):
        element_password = self.signinPage.get_password_element()
        element_password.send_keys(password)

    def click_button(self):
        element_button = self.signinPage.get_button_element()
        element_button.click()

    def check_authorization(self):
        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

        profile_link = self.navbarPage.get_profile_link()
        profile_link.click()

        user_name = self.profilePage.get_username_element()
        return user_name.text

    def wait_error(self):
        return self.signinPage.get_error_element().text

    def click_on_signup_link(self):
        element_signup_link = self.signinPage.get_signup_link()
        element_signup_link.click()

    def check_signup_redirect(self):
        return self.signupPage.get_signup_title().text

