import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from navbar.page import NavbarPage
from profile.page import ProfilePage
import unittest

from profile.utils import TestUtils
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
        # EXE_PATH = r'C:\chromedriver.exe'
        # self.driver = webdriver.Chrome(executable_path=EXE_PATH)
        self.driver = webdriver.Chrome()
        self.utils = Utils(driver=self.driver)
        self.navbarPage = NavbarPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.utils.login()
        self.testUtils = TestUtils(driver=self.driver)

    def test_profile_update_notification(self):
        self.testUtils.click_on_profile_icon()

        self.testUtils.click_on_profile_link()

        self.testUtils.click_on_change_profile_link()

        update_button = self.testUtils.wait_for_update_button()
        self.assertEqual(update_button.text, 'ОБНОВИТЬ')

        self.testUtils.click_on_update_button()

        update_notification = self.testUtils.wait_for_update_notification()
        self.assertEqual(update_notification, 'Данные обновлены!')

    def test_update_all(self):
        self.testUtils.click_on_profile_icon()

        self.testUtils.click_on_profile_link()

        self.testUtils.click_on_change_profile_link()

        # fill data

        self.testUtils.fill_name(NEW_NAME)

        self.testUtils.fill_surname(NEW_SURNAME)

        self.testUtils.fill_email(NEW_EMAIL)

        self.testUtils.select_sex(MALE_SEX)

        self.testUtils.fill_birthday(NEW_DATE)

        # click update

        self.testUtils.click_on_update_button()

        self.testUtils.refresh_page()

        # assert

        updated_name = self.testUtils.wait_for_updated_name()
        self.assertEqual(updated_name, NEW_NAME)

        updated_surname = self.testUtils.wait_for_updated_surname()
        self.assertEqual(updated_surname, NEW_SURNAME)

        updated_email = self.testUtils.wait_for_updated_email()
        self.assertEqual(updated_email, NEW_EMAIL)

        updated_sex = self.testUtils.wait_for_updated_sex()
        self.assertEqual(updated_sex, "Мужской")

        updated_birthday = self.testUtils.wait_for_updated_birthday()
        self.assertEqual(updated_birthday, NEW_DATE_COMPARE)

        def finalizer():
            self.testUtils.click_on_change_profile_link()
            self.testUtils.fill_name(OLD_NAME)

            self.testUtils.click_on_change_profile_link()
            self.testUtils.fill_surname(OLD_SURNAME)

            self.testUtils.click_on_change_profile_link()
            self.testUtils.fill_email(OLD_EMAIL)

            self.testUtils.select_sex(NO_SEX)

            self.testUtils.click_on_change_profile_link()
            self.testUtils.fill_birthday(OLD_DATE)

            self.testUtils.click_on_update_button()

        finalizer()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
