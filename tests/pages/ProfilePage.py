import time
from telnetlib import EC

import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.BasePage import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(self.PROFILE_URL)

    def fill_image_input(self, path, image):
        upd = self.wait_render(self.image_field)
        upd.click()
        time.sleep(2)

        pyautogui.write(path)
        pyautogui.press('enter')
        pyautogui.write(image)
        pyautogui.press('enter')