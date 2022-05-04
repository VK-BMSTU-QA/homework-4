from signin.page import SignInPage


LOGIN = '1234567'
PASSWORD = '1234567'

url = "https://goodvibesazot.tk/signin"


class Utils:
    def __init__(self, driver):
        self.driver = driver
        self.signInPage = SignInPage(self.driver)

    def login(self):
        self.driver.get(url=url)
        element_login = self.signInPage.get_login_element()
        element_login.send_keys(LOGIN)
        element_password = self.signInPage.get_password_element()
        element_password.send_keys(PASSWORD)
        element_button = self.signInPage.get_button_element()
        element_button.click()
