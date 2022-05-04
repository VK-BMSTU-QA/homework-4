from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *



class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

    def get_signup_title(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.auth-box h2')))

    def get_login_element(self):
        return self.driver.find_element(by=By.CLASS_NAME, value='user-box__login')

    def get_email_element(self):
        return self.driver.find_element(by=By.CLASS_NAME, value='user-box__email')

    def get_password_element(self):
        return self.driver.find_element(by=By.CLASS_NAME, value='user-box__password')

    def get_password_confirm_element(self):
        return self.driver.find_element(by=By.CLASS_NAME, value='user-box__confirm-password')

    def get_button_element(self):
        return self.driver.find_element(by=By.CLASS_NAME, value='auth-btn')

    def get_error_element(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'auth-content-inner__error')))

    def get_signin_link(self):
        return self.driver.find_element(by=By.CLASS_NAME, value='auth-content-form-signin__link')
