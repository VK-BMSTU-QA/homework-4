import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class WaitForTheAttributeValue(object):
    def __init__(self, locator, attribute, value):
        self.locator = locator
        self.attribute = attribute
        self.value = value

    def __call__(self, driver):
        try:
            element_attribute = driver.find_element(By.CLASS_NAME, self.locator).get_attribute(self.attribute)
            return element_attribute == self.value
        except StaleElementReferenceException:
            return False


class BasketPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])

    def get_basket_product(self, product_id):
        css_product = 'table-product-' + product_id.__str__()
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, css_product)))

    def wait_basket_product_remove(self, product):
        return self.wait.until(EC.staleness_of(product))

    def get_product_to_remove(self, product_id):
        css_remove = f'a[href="/cart/remove/{product_id}"]'
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_remove)))

    def wait_product_remove_from_basket(self, product_id):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, f'table-product-{product_id}')))

    def get_product_sum(self, product_id):
        css_sum = 'raw-item-price-' + product_id.__str__()
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, css_sum)))

    def get_product_price(self, product_id):
        css_price = 'item-price-' + product_id.__str__()
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, css_price)))

    def get_empty_basket_text(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'basket-empty-text')))

    def get_product_count_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'spinner__count')))

    def get_any_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'coupon-row')))

    def get_order_sum(self):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'basket-order-total__number')))
        self.wait.until_not(WaitForTheAttributeValue('basket-order-total__number', "textContent", "0₽"))
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'basket-order-total__number')))

    def get_back_in_catalog_link(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'back-to-result__link')))

    def get_delivery_selector(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'orderform-delivery_method')))

    def get_confirm_order_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'confirm-btn')))

    def get_page_title(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'title-page')))

    def get_last_sum_order(self):
        item = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.order-item__info > .price-title ~ span')))
        return item.get_attribute("innerText")


