import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from navbar.page import NavbarPage
from profile.page import ProfilePage
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
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.utils = Utils(driver=self.driver)
        self.navbarPage = NavbarPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.utils.login()

    def test_profile_update_notification(self):
        self.navbarPage.click_profile_icon()

        self.navbarPage.click_profile_link()

        self.profilePage.click_on_change_profile_link()

        self.assertEqual(self.profilePage.wait_for_update_button().text, 'ОБНОВИТЬ')

        self.profilePage.click_on_update_button()

        self.assertEqual(self.profilePage.wait_for_update_notification(), 'Данные обновлены!')

    def test_update_all_positive(self):
        self.navbarPage.click_profile_icon()

        self.navbarPage.click_profile_link()

        self.profilePage.click_on_change_profile_link()

        # fill data

        self.profilePage.fill_name(NEW_NAME)

        self.profilePage.fill_surname(NEW_SURNAME)

        self.profilePage.fill_email(NEW_EMAIL)

        self.profilePage.select_sex(MALE_SEX)

        self.profilePage.fill_birthday(NEW_DATE)

        # click update

        self.profilePage.click_on_update_button()

        self.profilePage.refresh_page()

        # assert

        self.assertEqual(self.profilePage.get_updated_name(), NEW_NAME)

        self.assertEqual(self.profilePage.get_updated_surname(), NEW_SURNAME)

        self.assertEqual(self.profilePage.get_updated_email(), NEW_EMAIL)

        self.assertEqual(self.profilePage.get_updated_sex(), "Мужской")

        self.assertEqual(self.profilePage.get_updated_birthday(), NEW_DATE_COMPARE)

        def finalizer():
            self.profilePage.click_on_change_profile_link()
            self.profilePage.fill_name(OLD_NAME)

            self.profilePage.click_on_change_profile_link()
            self.profilePage.fill_surname(OLD_SURNAME)

            self.profilePage.click_on_change_profile_link()
            self.profilePage.fill_email(OLD_EMAIL)

            self.profilePage.select_sex(NO_SEX)

            self.profilePage.click_on_change_profile_link()
            self.profilePage.fill_birthday(OLD_DATE)

            self.profilePage.click_on_update_button()

        finalizer()

    def tearDown(self):
        self.driver.quit()
