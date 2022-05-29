from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *



class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])

    def get_username_element(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.profile-image-block .b2n')))

    def get_profile_orders_title(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.orders-box .box-title')))

    def get_change_profile_link(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'change-btn')))

    def get_update_profile_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'update-btn')))

    def get_update_profile_notification(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile-update-alert-label')))

    def get_name_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__firstname')))

    def get_surname_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__secondname')))

    def get_email_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__email')))

    def get_birthday_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__birthday')))

    def get_sex_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'user-box__sex')))

    def get_favourite_product(self, product_id):
        css_locator = f'div[href="/product?id={product_id}"]'
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_locator)))

    def get_fav_product_by_id(self, product_id):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'div[href="/product?id={product_id}"]')))

    def get_product_by_id(self, product_id):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'a[href="/product?id={product_id}"]')))

