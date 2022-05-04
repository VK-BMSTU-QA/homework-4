from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class AllProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])

    def get_product_card(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-card')))

    def get_product_trends_title(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#product-tabletrends > div > span')))

    def get_category_name(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-left')))
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-table__title')))
