from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class NavbarPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])

    def get_profile_icon(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icons__link-avatar')))

    def get_profile_link(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'profile')))

    def get_favourites_link(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'favorite')))

    def get_reviews_link(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'reviews')))

    def get_search_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-input')))

    def get_search_result_first_element(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.search-suggests .search-suggest:first-child')))

    def get_search_result_elements(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.search-suggests .search-suggest')))
        return self.driver.find_elements_by_css_selector(".search-suggests .search-suggest")

    def get_search_result_products_elements(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.search-suggests .search-suggest')))
        return self.driver.find_elements_by_css_selector(".search-suggests > .search-suggest a[href^='/product']")

    def get_search_result_categories_elements(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.search-suggests .search-suggest')))
        return self.driver.find_elements_by_css_selector(".search-suggests > .search-suggest a[href^='/category']")
