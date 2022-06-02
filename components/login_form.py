from selenium_utils.utils_object import SeleniumBaseObject


class LoginForm(SeleniumBaseObject):
    BASE_URL = 'http://pyaterochka-team.site/'
    PATH = 'signin'

    USERNAME = 'input[type="email"]'
    PASSWORD = 'input[type="password"]'
    SUBMIT = 'button[class="btn btn_primary btn_rounded"]'
    EMAIL_HEADER = '.profile-card__username'
    INVALID_LOGIN_OR_PASSWORD = 'div[class="error"]'
    BTN_OPEN_NAVBAR = '.navbar__profile-name'
    BTN_LOGOUT_NAVBAR = '.navbar__popup > a[router-go="/logout"]'
    PAGE_NAME = '.auth-block > h1[key="null"]'
    BTN_SUBMIT_LOGOUT = "button.btn.btn_primary"

    def open_navbar(self):
        hover = self.actions.move_to_element(self._get_dom_element(self.BTN_OPEN_NAVBAR))
        hover.perform()

    def click_logout_navbar(self):
        return self._click_button(self.BTN_LOGOUT_NAVBAR)

    def click_logout_confirm(self):
        return self._click_button(self.BTN_SUBMIT_LOGOUT)

    def get_page_name(self):
        return self._get_element(self.PAGE_NAME)

    def get_email_header(self):
        return self._get_element(self.EMAIL_HEADER)

    def get_error(self):
        return self._check_drawable(self.INVALID_LOGIN_OR_PASSWORD)

    def fill_login(self, login):
        return self._set_text(self.USERNAME, login)

    def fill_password(self, password):
        return self._set_text(self.PASSWORD, password)

    def submit(self):
        return self._click_button(self.SUBMIT)
