# -*- coding: utf-8 -*-
import os
import unittest
from selenium import webdriver
from dotenv import load_dotenv

from tests.config import config
from tests.pages.MainPage import MainPage
# from pyvirtualdisplay import Display


class BaseTest(unittest.TestCase):

    def setUp(self):
        load_dotenv()
        self.correct_login = os.getenv('LOGIN_EXIST')
        self.correct_password = os.getenv('PASSWORD_EXIST')

        self.reg_mail = os.getenv('REG_MAIL')
        self.reg_name = os.getenv('REG_NAME')
        self.reg_surname = os.getenv('REG_SURNAME')
        self.reg_password = os.getenv('REG_PASSWORD')
        # display = Display(visible=0, size=(1600, 900))  
        # display.start()

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'ru,ru_RU'})
        if (config.ON_DRIVER):
            self.driver = webdriver.Chrome(config.DRIVER, chrome_options=chrome_options)
            # self.driver = webdriver.Firefox(executable_path=config.MOZILA_DRIVER)
        else:
            nodeUrl = 'http://localhost:4444/wd/hub'
            self.driver = webdriver.Remote(
                command_executor=nodeUrl,
                desired_capabilities={
                    'browserName': config.BROWSER,
                },
                options=chrome_options
            )

    def login(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.click_login()
        login_email_input = main_page.wait_render(main_page.login_email_input)
        login_email_input.send_keys(self.correct_login)
        login_pass_input = main_page.wait_render(main_page.login_password_input)
        login_pass_input.send_keys(self.correct_password)

        login_btn = main_page.wait_render(main_page.login_btn)
        login_btn.click()
        main_page.is_exist(main_page.header_profile)
