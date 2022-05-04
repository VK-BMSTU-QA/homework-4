from Base.BaseComponent import Component
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProfileForm(Component):
    NICKNAME = '//input[@name="nickname"]'
    EMAIL = '//input[@name="email"]'
    OLD_PASSWORD = '//input[@name="old_password"]'
    NEW_PASSWORD = '//input[@name="password"]'
    CONFIRM_PASSWORD = '//input[@name="confirm_password"]'
    SUBMIT = '//input[@class="profile-form__submit"]'
    ERROR_FILL_REMAINING_FIELDS = '//div[contains(text(), "Please, fill in the remaining fields")]'
    ERROR_NAME_LT3 = '//div[contains(text(), "Name needs to be at least 3 characters")]'
    INVALID_NICKNAME_CHARS = "//div[contains(text(), \"Name allows only letters and numbers and '_'\")]"
    INVALID_EMAIL = '//div[contains(text(), "Invalid email address")]'
    WEAK_PASSWORD_LENGTH = '//div[contains(text(), "Password needs to be 8 or more characters")]'
    WEAK_PASSWORD_NUMBERS = '//div[contains(text(), "Password requires at least 1 number")]'
    PASSWORD_MISMATCH = '//div[contains(text(), "Password confirmation needs to match the password")]'
    WRONG_OLD_PASSWORD = '//div[contains(text(), "Old password is wrong")]'

    def submit(self):
        WebDriverWait(self.driver, 10, 0.1).until(EC.element_to_be_clickable((By.XPATH, self.SUBMIT)))
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def set_nickname(self, nickname):
        input = self.driver.find_element_by_xpath(self.NICKNAME)
        input.clear()
        input.send_keys(nickname)

    def set_email(self, email):
        input = self.driver.find_element_by_xpath(self.EMAIL)
        input.clear()
        input.send_keys(email)

    def set_old_password(self, old_password):
        input = self.driver.find_element_by_xpath(self.OLD_PASSWORD)
        input.clear()
        input.send_keys(old_password)

    def set_new_password(self, new_password):
        input = self.driver.find_element_by_xpath(self.NEW_PASSWORD)
        input.clear()
        input.send_keys(new_password)

    def set_confirm_password(self, confirm_password):
        input = self.driver.find_element_by_xpath(self.CONFIRM_PASSWORD)
        input.clear()
        input.send_keys(confirm_password)

    def requires_to_fill_remaining_fields(self):
        return len(self.driver.find_elements_by_xpath(self.ERROR_FILL_REMAINING_FIELDS)) == 1

    def requires_name_at_least_3_characters(self):
        return len(self.driver.find_elements_by_xpath(self.ERROR_NAME_LT3)) == 1

    def invalid_chars_in_nickname(self):
        return len(self.driver.find_elements_by_xpath(self.INVALID_NICKNAME_CHARS)) == 1

    def invalid_email(self):
        return len(self.driver.find_elements_by_xpath(self.INVALID_EMAIL)) == 1

    def weak_password(self):
        return (
            len(self.driver.find_elements_by_xpath(self.WEAK_PASSWORD_LENGTH)) == 1
            and len(self.driver.find_elements_by_xpath(self.WEAK_PASSWORD_NUMBERS)) == 1
        )

    def password_mismatch(self):
        return len(self.driver.find_elements_by_xpath(self.PASSWORD_MISMATCH)) == 1

    def wrong_old_password(self):
        WebDriverWait(self.driver, 10, 0.1).until(lambda d: d.find_element_by_xpath(self.WRONG_OLD_PASSWORD))
        return True
