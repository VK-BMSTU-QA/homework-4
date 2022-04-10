# -*- coding: utf-8 -*-
import os
import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote
from dotenv import load_dotenv

from tests.config import config

class BaseTest(unittest.TestCase):

    def setUp(self):
        load_dotenv()
        self.correct_login = os.getenv('LOGIN_EXIST')
        self.correct_password = os.getenv('PASSWORD_EXIST')

        self.reg_mail = os.getenv('REG_EMAIL')
        self.reg_name = os.getenv('REG_NAME')
        self.reg_surname = os.getenv('REG_SURNAME')
        self.reg_password = os.getenv('REG_PASSWORD')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'ru,ru_RU'})
        if (config.ON_DRIVER):
            self.driver = webdriver.Chrome(config.DRIVER, chrome_options=chrome_options)
        else:
            nodeUrl = 'http://localhost:4444/wd/hub'
            self.driver = webdriver.Remote(
                command_executor=nodeUrl,
                desired_capabilities={
                    'browserName': config.BROWSER,
                },
                options=chrome_options
            )
    