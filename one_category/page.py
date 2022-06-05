from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import Keys

from base_page import BasePage
from one_category.static_locators import *


class OneCategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_category_name(self):
        self.get_element_by_class(filters_field_locator)
        return self.get_element_by_class(category_title_locator)

    def click_on_sort_by_price_button(self):
        sort_by_price_button = self.get_element_by_id(sort_by_price_button_locator)
        sort_by_price_button.click()

    def check_products_order(self, order):
        if order == 'ASC':
            first_product_price = '250 ₽'
        else:
            first_product_price = '500000 ₽'

        price = ''
        while price != first_product_price:
            try:
                price = self.get_element_seen_by_selector(product_price_locator).text
            except StaleElementReferenceException:
                continue

        product_prices = self.get_elements_by_css_selector(product_price_locator)

        product_prices_num = list()
        for product_price in product_prices:
            product_prices_num.append(int(product_price.text[0:len(product_price.text)-2]))

        current_price = product_prices_num[0]
        for product_price in product_prices_num:
            if order == 'DESC' and product_price > current_price or order == 'ASC' and product_price < current_price:
                return False

            current_price = product_price

        return True

    def fill_price_from_input(self, price):
        price_from_input = self.get_element_by_class(filter_price_from_locator)
        price_from_input.send_keys(Keys.COMMAND + "a")
        price_from_input.send_keys(Keys.DELETE)
        price_from_input.send_keys(price)

    def fill_price_to_input(self, price):
        price_to_input = self.get_element_by_class(filter_price_to_locator)
        price_to_input.clear()
        price_to_input.send_keys(price)

    def check_products_price_filter(self, min_price, max_price):
        price = ''
        while price != min_price + ' ₽':
            try:
                price = self.get_element_seen_by_selector(product_price_locator).text
            except StaleElementReferenceException:
                continue

        product_prices = self.get_elements_by_css_selector(product_price_locator)

        product_prices_num = list()
        for product_price in product_prices:
            product_prices_num.append(int(product_price.text[0:len(product_price.text) - 2]))

        for product_price in product_prices_num:
            if product_price > int(max_price) or product_price < int(min_price):
                return False

        return True

    def click_anywhere(self):
        page_title = self.get_element_by_class(category_title_locator)
        page_title.click()

    def wait_no_products_notification(self):
        no_products_notification = self.get_element_by_class(no_products_notification_locator)
        no_products_notification.click()
