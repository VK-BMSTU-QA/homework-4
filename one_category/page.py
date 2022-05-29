from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class OneCategoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])

    def get_sort_by_price_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'sort-price-toggle')))

    def get_category_products_price(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.sc-fweGeb')))
        return self.driver.find_elements_by_css_selector(".sc-fweGeb")

    def get_first_product_price(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.sc-fweGeb')))

    def get_price_from_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-filter-amount__from')))

    def get_price_to_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-filter-amount__to')))

    def get_page_title(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-table__title')))

    def get_no_products_notification(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-table-body')))

    def wait_product_disappear(self, product_id):
        return self.wait.until_not(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, f'div[href="/product?id=862"]')))

    def wait_product_appear(self, product_id):
        return self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, f'div[href="/product?id={product_id}"]')))

