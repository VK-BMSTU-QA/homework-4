import os
import unittest
from selenium import webdriver
from dotenv import load_dotenv
from .Config import *
from .pages.MainPage import MainPage

is_chrome = True

class BaseTest(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        # логин и пароль для существующего пользователя
        self.login = os.getenv('LIME_LOGIN')
        self.password = os.getenv('LIME_PASSWORD')
        self.login_cyr = os.getenv('LIME_LOGIN_CYRILLIC')
        self.password_cyr = os.getenv('LIME_PASSWORD_CYRILLIC')

        # логин и пароль для нового пользователя

        # селениум
        if is_chrome:
            self.options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(CHROME_DRIVER)
        else:
            self.driver = webdriver.Firefox(executable_path=MOZILA_DRIVER)

    def tearDown(self):
        self.driver.quit()

    def login(self):
        a = MainPage(self.driver)
        a.open()
        a.click_login()
        pass
