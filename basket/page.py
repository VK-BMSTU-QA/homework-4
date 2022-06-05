from selenium.common.exceptions import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page import BasePage
from basket.static_locators import *


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


class BasketPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_cross_to_delete_product(self, product_id):
        remover = self.get_element_by_css_selector(f'a[href="/cart/remove/{product_id}"]')
        remover.click()
        self.wait_product_invisibility(f'table-product-{product_id}')

    def check_product_count(self, product_id):
        product_sum = self.get_element_by_class('raw-item-price-' + product_id.__str__())
        product_price = self.get_element_by_class('item-price-' + product_id.__str__())

        return int(int(product_sum.text) / int(product_price.text))

    def wait_product_in_basket(self, product_id):
        return self.get_element_by_class('table-product-' + product_id.__str__())

    def wait_for_empty_basket_notification(self):
        return self.get_element_by_class(empty_basket_notification_locator).text

    def choose_products_count(self, count):
        product_count_input = self.get_element_by_class(count_spinner_locator)
        product_count_input.send_keys(Keys.ARROW_RIGHT)
        product_count_input.send_keys(Keys.BACK_SPACE)
        product_count_input.send_keys(count.__str__())

    def click_anywhere(self):
        anywhere = self.get_element_by_class(coupon_locator)
        anywhere.click()

    def get_product_price(self, product_id):
        return int(self.get_element_by_class('item-price-' + product_id.__str__()).text)

    def get_order_sum(self):
        order_sum = self.get_element_by_class(order_total_sum_locator)
        return int(order_sum.text[:len(order_sum.text)-1])

    def get_expected_sum(self, first, second):
        product_sum_first = self.get_element_by_class('raw-item-price-' + first.__str__())
        product_sum_second = self.get_element_by_class('raw-item-price-' + second.__str__())

        return int(product_sum_first.text) + int(product_sum_second.text)

    def select_delivery_way(self, option):
        select_elem = self.get_element_by_id(delivery_method_locator)
        selector = Select(select_elem)
        selector.select_by_index(option)

        return selector.first_selected_option.text

    def click_on_confirm_order_button(self):
        confirm_order_button = self.get_element_by_class(confirm_button_locator)
        confirm_order_button.click()
