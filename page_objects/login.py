from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base import Component
from page_objects.base import Page
from components.login_form import AuthForm


class LoginPage(Page):
    BASE_URL = 'http://pyaterochka-team.site/'
    PATH = 'login'

    USERNAME = 'input[type="email"]'
    PASSWORD = 'input[type="password"]'
    SUBMIT = 'button[class="btn btn_primary btn_rounded"]'
    EMAIL_HEADER = '.profile-card__username'
    INVALID_LOGIN_OR_PASSWORD = '.error'
    BTN_OPEN_NAVBAR = '.navbar__profile-name'
    BTN_LOGOUT_NAVBAR = '.navbar__popup > a[router-go="/logout"]'
    PAGE_NAME = '.auth-block > h1[key="null"]'

    def fill_login(self, login):
        username = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.USERNAME))
        )
        username.send_keys(login)

    def fill_password(self, password):
        pswd_elem = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.PASSWORD))
        )
        pswd_elem.send_keys(password)

    def submit(self):
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.SUBMIT))
        )
        submit.click()

    def login(self, login, password):
        self.fill_login(login)
        self.fill_password(password)
        self.submit()







# public async fillLogin(username: string) {
# await this.inputUsername.waitForDisplayed();
# await this.inputUsername.setValue(username);
# }
#
# public async fillPassword(password: string) {
# await this.inputPassword.waitForDisplayed();
# await this.inputPassword.setValue(password);
# await this.btnSubmit.click();
# }
#
# public async login(username: string, password: string) {
# await this.fillLogin(username);
# await this.fillPassword(password);
# }
#
# public async logout()
# {
# await this.btnOpenNavBar.click();
# await this.btnNavBarLogout.click();
# }
#
# public async getEmail()
# {
# await this.userEmailHeader.waitForDisplayed();
# return this.userEmailHeader.getText();
# }
#
# public async getPageName()
# {
# await this.pageName.waitForDisplayed();
# return this.pageName.getText();
# }
#
# public async getError()
# {
# await this.invalidLoginOrPassword.waitForDisplayed();
# return this.invalidLoginOrPassword.getText();
# }
#
# public
# open()
# {
# return super.open('signin');
# }
