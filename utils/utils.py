import os

from signin.page import SignInPage


LOGIN = os.environ.get('LOGIN')
PASSWORD = os.environ.get('PASSWORD')

url = "https://account.mail.ru/login"


class Utils:
    def __init__(self, driver):
        self.driver = driver
        self.signInPage = SignInPage(self.driver)
        self.driver.get(url=url)

    def login(self):
        self.signInPage.fill_login(LOGIN)
        self.signInPage.click_button()
        self.signInPage.fill_password(PASSWORD)
        self.signInPage.click_button()
