from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class OneProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])

    def get_product_card(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'slider-preview__picture')))

    def get_product_card_by_id(self, product_id):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'div[href="/product?id={product_id}"]')))

    def get_add_to_basket_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__cart')))

    def get_go_to_basket_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card-btn__wrap')))

    def get_product_count_input(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-page-spinner__count')))

    def get_any_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card__name')))

    def get_add_favourite_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-favorite-btn__favorite')))

    def get_favourite_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-favorite-btn__favorite')))

    def get_delete_from_favourite_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'flagIsFavorite_true')))

    def get_review_text_field(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-comment-text')))

    def get_add_review_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-comment-btn')))

    def get_rating_item(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.rating__items')))

    def get_review(self):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.comments-container:last-child > li > div > p')))

    def get_review_error(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'new-comment-alert-label')))

    def get_back_to_catalog_link(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'back-to-result__link')))

    def get_product_name(self):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-card__name')))
