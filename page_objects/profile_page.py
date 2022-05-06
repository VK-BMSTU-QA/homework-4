import selenium.webdriver.common.devtools.v99.runtime

from components.profile_form import ProfileForm
from page_objects.base import Page


class ProfilePage(Page):
    BASE_URL = 'http://pyaterochka-team.site/'
    PATH = 'profile'
    BTN_CHANGE_PASSWORD = 'button[class="btn btn_primary "]'
    VALIDATION_ERR = 'div[class="validation_error"]'
    EMAIL_HEADER = '.profile-card__username'
    PASSWORD_FIELDS = 'input[type="password"]'


    def __init__(self, driver):
        super().__init__(driver)
        self.profile_form = ProfileForm(driver)

    def click_button_change_password(self):
        return self._click_button(self.BTN_CHANGE_PASSWORD)

    def fill_change_password_form(self):
        return self._click_button(self.BTN_CHANGE_PASSWORD)

    def get_validation_err(self):
        return self._check_drawable(self.VALIDATION_ERR)

    def get_password_fields(self):
        return self._get_elements(self.PASSWORD_FIELDS)

    def set_new_password(self, fields, old_password, new_password):
        if len(fields) != 3:
            return False
        fields[0].clear()
        fields[0].send_keys(old_password)
        fields[1].clear()
        fields[2].clear()
        fields[1].send_keys(new_password)
        fields[2].send_keys(new_password)

        return True

    def go_to_switch_password(self):
        _ = self._get_element(self.EMAIL_HEADER)
        return self.driver.get(self.BASE_URL + 'profile/edit/secure')
