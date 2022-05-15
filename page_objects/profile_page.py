import selenium.webdriver.common.devtools.v99.runtime

from components.profile_form import ProfileForm
from page_objects.base import Page


class ProfilePage(Page):
    BASE_URL = 'http://pyaterochka-team.site/'
    PATH = 'profile'
    DEFAULT_AVATAR = "/files/default_avatar.png"
    BTN_CHANGE_PASSWORD = 'button[class="btn btn_primary "]'
    VALIDATION_ERR = 'div[class="validation_error"]'
    EMAIL_HEADER = '.profile-card__username'
    PASSWORD_FIELDS = 'input[type="password"]'
    PROFILE_IMAGE_FORM = 'input[class="image-uploader__file-upload"]'
    PROFILE_AVATAR_NAME = '//*[@id="root"]/div/div[1]/div[2]/div/div/div[2]/div/div[1]'
    CONFIRM_CHANGE_PASSWORD = '#root > div > div:nth-child(1) > div:nth-child(2) > div > div > div.tabs-container__wrapper > div > div'


    def __init__(self, driver):
        super().__init__(driver)
        self.profile_form = ProfileForm(driver)

    def click_button_change_password(self):
        return self._click_button(self.BTN_CHANGE_PASSWORD)

    def wait_confirm_change_password(self):
        self._check_drawable(self.CONFIRM_CHANGE_PASSWORD)
        return not self._check_elem_not_exists(self.CONFIRM_CHANGE_PASSWORD)

    def fill_change_password_form(self):
        return self._click_button(self.BTN_CHANGE_PASSWORD)

    def get_validation_err(self):
        return self._check_drawable(self.VALIDATION_ERR)

    def get_password_fields(self):
        return self._get_elements(self.PASSWORD_FIELDS)

    def get_avatar_input(self):
        return self._get_input(self.PROFILE_IMAGE_FORM)

    def get_avatar_filename(self):
        return self._get_element_by_xpath(self.PROFILE_AVATAR_NAME)

    def wait_update_avatar(self):
        return self._check_disappear_by_xpath(self.PROFILE_AVATAR_NAME)

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

    def set_new_avatar(self, input_form, img_path):
        return input_form.send_keys(img_path)

    def redirect_to_profile_settings(self):
        return self.driver.get(self.BASE_URL + 'profile/edit/common')

    def go_to_switch_password(self):
        _ = self._get_element(self.EMAIL_HEADER)
        return self.driver.get(self.BASE_URL + 'profile/edit/secure')

    def go_to_profile_settings(self):
        _ = self._get_element(self.EMAIL_HEADER)
        return self.redirect_to_profile_settings()
