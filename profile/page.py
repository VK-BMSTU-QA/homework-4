from selenium.webdriver.support.select import Select

from base_page import BasePage
from profile.static_locators import *


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_favourite_product(self, product_id):
        return self.get_element_by_css_selector(f'div[href="/product?id={product_id}"]')

    def click_on_change_profile_link(self):
        change_profile_link = self.get_element_by_class(change_profile_button_locator)
        change_profile_link.click()

    def wait_for_update_button(self):
        return self.get_element_by_class(update_profile_button_locator)

    def click_on_update_button(self):
        update_button = self.get_element_by_class(update_profile_button_locator)
        update_button.click()

    def wait_for_update_notification(self):
        return self.get_element_by_class(update_notification_locator).text

    def fill_name(self, name):
        name_input = self.get_element_by_class(username_locator)
        name_input.click()
        name_input.clear()
        name_input.send_keys(name)

    def refresh_page(self):
        self.driver.refresh()

    def get_updated_name(self):
        return self.get_element_by_class(username_locator).get_attribute('value')

    def fill_surname(self, surname):
        surname_input = self.get_element_by_class(surname_locator)
        surname_input.click()
        surname_input.clear()
        surname_input.send_keys(surname)

    def get_updated_surname(self):
        return self.get_element_by_class(surname_locator).get_attribute('value')

    def fill_email(self, email):
        email_input = self.get_element_by_class(email_locator)
        email_input.click()
        email_input.clear()
        email_input.send_keys(email)

    def get_updated_email(self):
        return self.get_element_by_class(email_locator).get_attribute('value')

    def fill_birthday(self, birthday):
        birthday_input = self.get_element_by_class(birthday_locator)
        birthday_input.click()
        birthday_input.clear()
        birthday_input.send_keys(birthday)

    def get_updated_birthday(self):
        return self.get_element_by_class(birthday_locator).get_attribute('value')

    def select_sex(self, option):
        sex = self.get_element_by_class(sex_locator)
        selector = Select(sex)
        selector.select_by_index(option)

    def get_updated_sex(self):
        sex = self.get_element_seen_by_selector(sex_selector_locator)
        selector = Select(sex)
        return selector.first_selected_option.text

    def get_username(self):
        return self.get_element_by_css_selector(profile_name_locator).text

    def click_on_certain_fav_product(self, product_id):
        product = self.get_element_by_css_selector(f'div[href="/product?id={product_id}"]')
        product.click()

    def wait_product_review(self, product_id):
        self.get_element_by_css_selector(f'a[href="/product?id={product_id}"]')

    def get_last_sum_order(self):
        self.get_element_by_css_selector(last_order_sum_locator)
        return self.get_element_by_css_selector(last_order_sum_locator).get_attribute("innerText")
