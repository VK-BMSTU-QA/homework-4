import time

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from navbar.page import NavbarPage
from profile.page import ProfilePage
from signin.page import SignInPage
from signup.page import SignUpPage
from all_products.page import AllProductsPage
from one_product.page import OneProductPage
from basket.page import BasketPage


class TestUtils:
    def __init__(self, driver):
        self.driver = driver
        self.signinPage = SignInPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.signupPage = SignUpPage(self.driver)
        self.navbarPage = NavbarPage(self.driver)
        self.allProductsPage = AllProductsPage(self.driver)
        self.oneProductPage = OneProductPage(self.driver)
        self.basketPage = BasketPage(self.driver)

    def click_on_product(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()
        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        return int(current_url[current_url.rfind('=')+1:len(current_url)])

    def click_on_product_by_id(self, product_id):
        product_card = self.oneProductPage.get_product_card_by_id(product_id=product_id)
        product_card.click()

    def click_add_to_basket_button(self):
        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

    def click_go_to_basket_button(self):
        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()
        go_to_basket_button.click()

    def remove_product_from_basket(self, product_id):
        remover = self.basketPage.get_product_to_remove(product_id=product_id)
        remover.click()
        self.basketPage.wait_product_remove_from_basket(product_id=product_id)

    def wait_product_in_basket(self, product_id):
        return self.basketPage.get_basket_product(product_id)

    def choose_products_count(self, count):
        product_count_input = self.oneProductPage.get_product_count_input()
        product_count_input.send_keys(Keys.ARROW_RIGHT)
        product_count_input.send_keys(Keys.BACK_SPACE)
        product_count_input.send_keys(count)

    def check_product_count_in_basket(self, product_id):
        product_sum = self.basketPage.get_product_sum(product_id)
        product_price = self.basketPage.get_product_price(product_id)
        count = int(int(product_sum.text) / int(product_price.text))
        return count

    def wait_for_empty_basket_notification(self):
        return self.basketPage.get_empty_basket_text().text

    def choose_products_count_in_basket(self, count):
        product_count_input = self.basketPage.get_product_count_input()
        product_count_input.send_keys(Keys.ARROW_RIGHT)
        product_count_input.send_keys(Keys.BACK_SPACE)
        product_count_input.send_keys(count.__str__())

    def click_anywhere(self):
        anywhere = self.basketPage.get_any_field()
        anywhere.click()

    def wait_product_price(self, product_id):
        return int(self.basketPage.get_product_price(product_id).text)

    def wait_order_sum(self):
        order_sum = self.basketPage.get_order_sum()
        return int(order_sum.text[:len(order_sum.text)-1])

    def click_back_to_catalog_link(self):
        back_in_catalog = self.basketPage.get_back_in_catalog_link()
        back_in_catalog.click()

    def get_expected_sum(self, first, second):
        product_sum_first = self.basketPage.get_product_sum(product_id=first)
        product_sum_second = self.basketPage.get_product_sum(product_id=second)

        return int(product_sum_first.text) + int(product_sum_second.text)

    def select_delivery_way(self, option):
        select_elem = self.basketPage.get_delivery_selector()
        selector = Select(select_elem)
        selector.select_by_index(option)

        return selector.first_selected_option.text

    def click_on_confirm_order_button(self):
        confirm_order_button = self.basketPage.get_confirm_order_button()
        confirm_order_button.click()

    def wait_redirect_to_profile_orders(self):
        return self.profilePage.get_profile_orders_title().text
