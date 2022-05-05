import os
import unittest

from Login.LoginPage import LoginPage
from Profile.ProfilePage import ProfilePage
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options

class ProfilePageTest(unittest.TestCase):
    EMAIL = os.environ["TESTUSERNAME"]
    PASSWORD = os.environ["TESTPASSWORD"]

    def setUp(self):
        browser = os.environ.get("TESTBROWSER", "CHROME")
        options = Options()
        options.headless = bool(os.environ.get("HEADLESS", False))
        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            options=options
        )

        login_page = LoginPage(self.driver)
        login_page.login(self.EMAIL, self.PASSWORD)

        self.profile_page = ProfilePage(self.driver)
        self.profile_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_empty_nickname(self):
        form = self.profile_page.profile_form
        form.set_nickname("")
        form.submit()
        self.assertTrue(form.requires_to_fill_remaining_fields())

    def test_nickname_lt_3(self):
        form = self.profile_page.profile_form
        form.set_nickname("ta")
        form.submit()
        self.assertTrue(form.requires_name_at_least_3_characters())

    def test_nickname_allowed_characters(self):
        form = self.profile_page.profile_form
        form.set_nickname("Привет =)")
        form.submit()
        self.assertTrue(form.invalid_chars_in_nickname())

    def test_wrong_email_error(self):
        form = self.profile_page.profile_form
        form.set_email("testing.com")
        form.submit()
        self.assertTrue(form.invalid_email())

    def test_password_requires_8chars_and_1_letter(self):
        form = self.profile_page.profile_form
        form.set_new_password("baNaNa")
        form.submit()
        self.assertTrue(form.weak_password())

    def test_confirm_password_error(self):
        form = self.profile_page.profile_form
        new_password = "ndbybUYDBy6rdG"
        form.set_new_password(new_password)
        form.set_confirm_password(new_password + "a")
        form.submit()
        self.assertTrue(form.password_mismatch())

    def test_wrong_current_password_error(self):
        form = self.profile_page.profile_form
        new_password = "ndbybUYDBy6rdG"
        form.set_new_password(new_password)
        form.set_confirm_password(new_password)
        form.set_old_password("mysecretpassword")
        form.submit()
        self.assertTrue(form.wrong_old_password())
