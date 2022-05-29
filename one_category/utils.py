import time

from selenium.webdriver import Keys

from navbar.page import NavbarPage
from profile.page import ProfilePage
from signin.page import SignInPage
from signup.page import SignUpPage
from all_products.page import AllProductsPage
from one_category.page import OneCategoryPage


class TestUtils:
    def __init__(self, driver):
        self.driver = driver
        self.signinPage = SignInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.signupPage = SignUpPage(self.driver)
        self.navbarPage = NavbarPage(self.driver)
        self.oneCategoryPage = OneCategoryPage(self.driver)
        self.allProductsPage = AllProductsPage(self.driver)

    def click_on_category_list_button(self):
        category_list_button = self.allProductsPage.get_category_list_button()
        category_list_button.click()

    def click_on_category(self, category_name):
        all_categories = self.allProductsPage.get_category_list()
        category_need = ''
        for category in all_categories:
            if category.text == category_name:
                category_need = category
                break

        category_need.click()

    def click_on_sort_by_price_button(self):
        sort_by_price_button = self.oneCategoryPage.get_sort_by_price_button()
        sort_by_price_button.click()

    def check_products_order(self, order):
        self.oneCategoryPage.wait_product_appear(862)

        if order == 'ASC':
            first_element_price = '250 ₽'
        else:
            first_element_price = '500000 ₽'

        product_price = ''
        while product_price != first_element_price:
            product_price = self.oneCategoryPage.get_first_product_price().text

        product_prices = self.oneCategoryPage.get_category_products_price()

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
        price_from_input = self.oneCategoryPage.get_price_from_input()
        price_from_input.send_keys(Keys.COMMAND + "a")
        price_from_input.send_keys(Keys.DELETE)
        price_from_input.send_keys(price)

    def fill_price_to_input(self, price):
        price_to_input = self.oneCategoryPage.get_price_to_input()
        price_to_input.clear()
        price_to_input.send_keys(price)

    def check_products_price_filter(self, min_price, max_price):
        self.oneCategoryPage.wait_product_disappear(881)
        self.oneCategoryPage.wait_product_appear(909)

        product_prices = self.oneCategoryPage.get_category_products_price()

        product_prices_num = list()
        for product_price in product_prices:
            product_prices_num.append(int(product_price.text[0:len(product_price.text) - 2]))

        for product_price in product_prices_num:
            if product_price > max_price or product_price < min_price:
                return False

        return True

    def click_anywhere(self):
        page_title = self.oneCategoryPage.get_page_title()
        page_title.click()

    def wait_no_products_notification(self):
        no_products_notification = self.oneCategoryPage.get_no_products_notification()
        no_products_notification.click()
