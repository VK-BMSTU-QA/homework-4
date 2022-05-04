import os
import unittest

from Login.LoginPage import LoginPage
from Profile.ProfilePage import ProfilePage
from selenium.webdriver import DesiredCapabilities, Remote


class ProfilePageTest(unittest.TestCase):
    EMAIL = os.environ["TESTUSERNAME"]
    PASSWORD = os.environ["TESTPASSWORD"]

    def setUp(self):
        browser = os.environ.get("TESTBROWSER", "CHROME")

        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
        )

        login_page = LoginPage(self.driver)
        login_page.login(self.EMAIL, self.PASSWORD)

        ProfilePage(self.driver).open()

    def tearDown(self):
        self.driver.quit()

    def test_empty_nickname(self):
        form = ProfilePage(self.driver).profile_form
        form.set_nickname("")
        form.submit()
        self.assertTrue(form.requires_to_fill_remaining_fields())

    def test_nickname_lt_3(self):
        form = ProfilePage(self.driver).profile_form
        form.set_nickname("ta")
        form.submit()
        self.assertTrue(form.requires_name_at_least_3_characters())

    def test_nickname_allowed_characters(self):
        form = ProfilePage(self.driver).profile_form
        form.set_nickname("Привет =)")
        form.submit()
        self.assertTrue(form.invalid_chars_in_nickname())

    def test_wrong_email_error(self):
        form = ProfilePage(self.driver).profile_form
        form.set_email("testing.com")
        form.submit()
        self.assertTrue(form.invalid_email())

    def test_password_requires_8chars_and_1_letter(self):
        form = ProfilePage(self.driver).profile_form
        form.set_new_password("baNaNa")
        form.submit()
        self.assertTrue(form.weak_password())

    def test_confirm_password_error(self):
        form = ProfilePage(self.driver).profile_form
        new_password = "ndbybUYDBy6rdG"
        form.set_new_password(new_password)
        form.set_confirm_password(new_password + "a")
        form.submit()
        self.assertTrue(form.password_mismatch())

    def test_wrong_current_password_error(self):
        form = ProfilePage(self.driver).profile_form
        new_password = "ndbybUYDBy6rdG"
        form.set_new_password(new_password)
        form.set_confirm_password(new_password)
        form.set_old_password("mysecretpassword")
        form.submit()
        self.assertTrue(form.wrong_old_password())
