from tests.pages.BasePage import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # открывает главную страницу сайта
    def open(self):
        self.driver.get(self.BASE_URL)

    # открывает окно логина
    def click_login(self):
        elem = self.wait_render(self.login_btn)
        elem.click()

    def click_signup(self):
        elem = self.wait_render(self.signup_btn)
        elem.click()
