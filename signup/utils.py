from navbar.page import NavbarPage
from profile.page import ProfilePage
from signin.page import SignInPage
from signup.page import SignUpPage

url = "https://goodvibesazot.tk/signup"

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
        element_login = self.signupPage.get_login_element()
        element_login.send_keys(login)

    def fill_email(self, email):
        element_email = self.signupPage.get_email_element()
        element_email.send_keys(email)

    def fill_password(self, password):
        element_password = self.signupPage.get_password_element()
        element_password.send_keys(password)

    def fill_password_confirm(self, password):
        element_password_repeat = self.signupPage.get_password_confirm_element()
        element_password_repeat.send_keys(password)

    def click_button(self):
        element_button = self.signupPage.get_button_element()
        element_button.click()

    def check_authorization(self):
        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

        profile_link = self.navbarPage.get_profile_link()
        profile_link.click()

        user_name = self.profilePage.get_username_element()
        return user_name.text

    def wait_error(self):
        return self.signupPage.get_error_element().text

    def click_on_signin_link(self):
        element_signup_link = self.signupPage.get_signin_link()
        element_signup_link.click()

    def check_signup_redirect(self):
        return self.signinPage.get_signin_title().text