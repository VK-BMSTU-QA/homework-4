# -*- coding: utf-8 -*-

import os
import unittest
from cProfile import label

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from sympy import O

from tests.common import Albums, CommonTest, Page, Player, Sidebar, Topbar, Tracks, has_element
from tests.login_test import Component, LoginPage

class ErrorMessage(Component):
    FILL_REMAINING_FIELDS = '//div[contains(text(), "Please, fill in the remaining fields")]'

    def requires_to_fill_remaining_fields(self):
        return len(self.driver.find_elements_by_xpath(self.FILL_REMAINING_FIELDS)) == 1

class ProfilePage(Page):
    path = 'profile'

    @property
    def profile_form(self):
        return ProfileForm(self.driver)

class ProfileForm(Component):
    NICKNAME = '//input[@name="nickname"]'
    EMAIL = '//input[@name="email"]'
    OLD_PASSWORD = '//input[@name="old_password"]'
    NEW_PASSWORD = '//input[@name="password"]'
    CONFIRM_PASSWORD = '//input[@name="confirm_password"]'
    SUBMIT = '//input[@class="profile-form__submit"]'

    def submit(self):
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

class ProfilePageTest(unittest.TestCase):
    EMAIL = os.environ['TESTUSERNAME']
    PASSWORD = os.environ['TESTPASSWORD']

    def setUp(self):
        browser = os.environ.get('TESTBROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        login_page = LoginPage(self.driver)
        login_page.open()

        login_form = login_page.form
        login_form.set_email(self.EMAIL)
        login_form.set_password(self.PASSWORD)
        login_form.login()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "avatar__img"))
        )

    def tearDown(self):
        self.driver.quit()

    def test_empty_nickname(self):
        form = ProfilePage(self.driver).profile_form

    # def test_nickname_lt_3(self):
    

    # def test_nickname_allowed_characters(self):

    # def test_wrong_email_error(self):

    # def test_password_requires_8chars_and_1_letter(self):

    # def test_confirm_password_error(self):

    # def test_wrong_current_password_error(self):