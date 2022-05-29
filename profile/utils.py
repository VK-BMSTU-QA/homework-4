from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from navbar.page import NavbarPage
from profile.page import ProfilePage
from signin.page import SignInPage
from signup.page import SignUpPage
from all_products.page import AllProductsPage
from one_product.page import OneProductPage
from basket.page import BasketPage


class TestUtils:
    def __init__(self, driver):
        self.driver = driver
        self.signinPage = SignInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.signupPage = SignUpPage(self.driver)
        self.navbarPage = NavbarPage(self.driver)
        self.allProductsPage = AllProductsPage(self.driver)
        self.oneProductPage = OneProductPage(self.driver)
        self.basketPage = BasketPage(self.driver)

    def click_on_profile_icon(self):
        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

    def click_on_profile_link(self):
        profile_link = self.navbarPage.get_profile_link()
        profile_link.click()

    def click_on_change_profile_link(self):
        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

    def wait_for_update_button(self):
        return self.profilePage.get_update_profile_button()

    def click_on_update_button(self):
        update_button = self.profilePage.get_update_profile_button()
        update_button.click()

    def wait_for_update_notification(self):
        return self.profilePage.get_update_profile_notification().text

    def fill_name(self, name):
        name_input = self.profilePage.get_name_input()
        name_input.click()
        name_input.clear()
        name_input.send_keys(name)

    def refresh_page(self):
        self.driver.refresh()

    def wait_for_updated_name(self):
        return self.profilePage.get_name_input().get_attribute('value')

    def fill_surname(self, surname):
        surname_input = self.profilePage.get_surname_input()
        surname_input.click()
        surname_input.clear()
        surname_input.send_keys(surname)

    def wait_for_updated_surname(self):
        return self.profilePage.get_surname_input().get_attribute('value')

    def fill_email(self, email):
        email_input = self.profilePage.get_email_input()
        email_input.click()
        email_input.clear()
        email_input.send_keys(email)

    def wait_for_updated_email(self):
        return self.profilePage.get_email_input().get_attribute('value')

    def fill_birthday(self, birthday):
        birthday_input = self.profilePage.get_birthday_input()
        birthday_input.click()
        birthday_input.clear()
        birthday_input.send_keys(birthday)

    def wait_for_updated_birthday(self):
        return self.profilePage.get_birthday_input().get_attribute('value')

    def select_sex(self, option):
        sex = self.profilePage.get_sex_input()
        selector = Select(sex)
        selector.select_by_index(option)

    def wait_for_updated_sex(self):
        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

        sex = self.profilePage.get_sex_input()
        selector = Select(sex)
        return selector.first_selected_option.text

