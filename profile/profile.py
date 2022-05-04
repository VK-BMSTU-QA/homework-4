import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from navbar.page import NavbarPage
from profile.page import ProfilePage
import unittest
from utils.utils import Utils

OLD_NAME = 'OldName'
NEW_NAME = 'NewName'
OLD_SURNAME = 'OldSurname'
NEW_SURNAME = 'NewSurname'
OLD_EMAIL = 'OldEmail@mail.ru'
NEW_EMAIL = 'NewEmail@mail.ru'
OLD_DATE = '01.01.2000'
NEW_DATE = '31.12.2000'
NEW_DATE_COMPARE = '2000-12-31'
MALE_SEX = 2
NO_SEX = 0


class Profile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.utils = Utils(driver=self.driver)
        self.navbarPage = NavbarPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.utils.login()

    def test_profile_update_button(self):
        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

        profile_link = self.navbarPage.get_profile_link()
        profile_link.click()

        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

        update_button = self.profilePage.get_update_profile_button()
        self.assertEqual(update_button.text, 'ОБНОВИТЬ')

    def test_profile_update_notification(self):
        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

        profile_link = self.navbarPage.get_profile_link()
        profile_link.click()

        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

        update_button = self.profilePage.get_update_profile_button()
        update_button.click()

        update_notification = self.profilePage.get_update_profile_notification()
        self.assertEqual(update_notification.text, 'Данные обновлены!')

    def test_update_name(self):
        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

        profile_link = self.navbarPage.get_profile_link()
        profile_link.click()

        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

        name_input = self.profilePage.get_name_input()
        name_input.click()
        name_input.clear()
        name_input.send_keys(NEW_NAME)

        update_button = self.profilePage.get_update_profile_button()
        update_button.click()

        self.driver.refresh()

        updated_name = self.profilePage.get_name_input()
        self.assertEqual(updated_name.get_attribute('value'), NEW_NAME)

        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

        updated_name.click()
        updated_name.clear()
        updated_name.send_keys(OLD_NAME)

        update_button = self.profilePage.get_update_profile_button()
        update_button.click()

    def test_update_surname(self):
        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

        profile_link = self.navbarPage.get_profile_link()
        profile_link.click()

        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

        surname_input = self.profilePage.get_surname_input()
        surname_input.click()
        surname_input.clear()
        surname_input.send_keys(NEW_SURNAME)

        update_button = self.profilePage.get_update_profile_button()
        update_button.click()

        self.driver.refresh()

        updated_surname = self.profilePage.get_surname_input()
        self.assertEqual(updated_surname.get_attribute('value'), NEW_SURNAME)

        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

        updated_surname.click()
        updated_surname.clear()
        updated_surname.send_keys(OLD_SURNAME)

        update_button = self.profilePage.get_update_profile_button()
        update_button.click()

    def test_update_email(self):
        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

        profile_link = self.navbarPage.get_profile_link()
        profile_link.click()

        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

        email_input = self.profilePage.get_email_input()
        email_input.click()
        email_input.clear()
        email_input.send_keys(NEW_EMAIL)

        update_button = self.profilePage.get_update_profile_button()
        update_button.click()

        self.driver.refresh()

        updated_email = self.profilePage.get_email_input()
        self.assertEqual(updated_email.get_attribute('value'), NEW_EMAIL)

        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

        updated_email.click()
        updated_email.clear()
        updated_email.send_keys(OLD_EMAIL)

        update_button = self.profilePage.get_update_profile_button()
        update_button.click()

    def test_update_sex(self):
        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

        profile_link = self.navbarPage.get_profile_link()
        profile_link.click()

        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

        sex = self.profilePage.get_sex_input()
        selector = Select(sex)
        selector.select_by_index(MALE_SEX)

        update_button = self.profilePage.get_update_profile_button()
        update_button.click()

        self.driver.refresh()

        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

        sex = self.profilePage.get_sex_input()
        selector = Select(sex)
        option = selector.first_selected_option
        self.assertEqual(option.text, "Мужской")

        selector.select_by_index(NO_SEX)

        update_button = self.profilePage.get_update_profile_button()
        update_button.click()

    def test_update_birthday(self):
        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

        profile_link = self.navbarPage.get_profile_link()
        profile_link.click()

        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

        birthday = self.profilePage.get_birthday_input()
        birthday.send_keys(NEW_DATE)

        update_button = self.profilePage.get_update_profile_button()
        update_button.click()

        self.driver.refresh()

        updated_birthday = self.profilePage.get_birthday_input()
        self.assertEqual(updated_birthday.get_attribute('value'), NEW_DATE_COMPARE)

        change_profile_link = self.profilePage.get_change_profile_link()
        change_profile_link.click()

        updated_birthday.click()
        updated_birthday.send_keys(OLD_DATE)

        update_button = self.profilePage.get_update_profile_button()
        update_button.click()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
