import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from utils.utils import Utils
from selenium.webdriver.support.ui import Select
from all_products.page import AllProductsPage
from one_product.page import OneProductPage
from basket.page import BasketPage
from profile.page import ProfilePage


PRODUCT_COUNT = 2
POST_OPTION = 2


class Basket(unittest.TestCase):
    def setUp(self):
        EXE_PATH = r'C:\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=EXE_PATH)

        self.product_id = 0
        self.utils = Utils(driver=self.driver)
        self.allProductsPage = AllProductsPage(self.driver)
        self.oneProductPage = OneProductPage(self.driver)
        self.basketPage = BasketPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.utils.login()

    def test_basket(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()
        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()
        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()
        go_to_basket_button.click()

        product_in_basket = self.basketPage.get_basket_product(self.product_id)

        remover = self.basketPage.get_product_to_remove(product_id=self.product_id)
        remover.click()

    def test_basket_count(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()
        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

        product_count_input = self.oneProductPage.get_product_count_input()
        product_count_input.send_keys(Keys.ARROW_RIGHT)
        product_count_input.send_keys(Keys.BACK_SPACE)
        product_count_input.send_keys(PRODUCT_COUNT.__str__())

        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()
        go_to_basket_button.click()

        product_sum = self.basketPage.get_product_sum(self.product_id)
        product_price = self.basketPage.get_product_price(self.product_id)

        count = int(int(product_sum.text) / int(product_price.text))
        self.assertEqual(count, PRODUCT_COUNT)

        remover = self.basketPage.get_product_to_remove(product_id=self.product_id)
        remover.click()

    def test_basket_refresh(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()
        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])

        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()
        go_to_basket_button.click()

        self.driver.refresh()

        product_in_basket = self.basketPage.get_basket_product(self.product_id)

        remover = self.basketPage.get_product_to_remove(product_id=self.product_id)
        remover.click()

    def test_basket_delete_product(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()
        go_to_basket_button.click()

        product_in_basket = self.basketPage.get_basket_product(self.product_id)

        remover = self.basketPage.get_product_to_remove(product_id=self.product_id)
        remover.click()

        self.basketPage.wait_basket_product_remove(product_in_basket)

    def test_basket_empty(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()
        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])

        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()
        go_to_basket_button.click()

        remover = self.basketPage.get_product_to_remove(product_id=self.product_id)
        remover.click()

        empty_basket_text = self.basketPage.get_empty_basket_text()

        self.assertEqual(empty_basket_text.text, "Ваша корзина пуста. Вернуться к покупкам")

    def test_basket_increase_in_basket(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()
        go_to_basket_button.click()

        product_count_input = self.basketPage.get_product_count_input()
        product_count_input.send_keys(Keys.ARROW_RIGHT)
        product_count_input.send_keys(Keys.BACK_SPACE)
        product_count_input.send_keys(PRODUCT_COUNT.__str__())

        anywhere = self.basketPage.get_any_field()
        anywhere.click()

        product_sum = self.basketPage.get_product_sum(self.product_id)
        product_price = self.basketPage.get_product_price(self.product_id)

        count = int(int(product_sum.text) / int(product_price.text))
        self.assertEqual(count, PRODUCT_COUNT)

        remover = self.basketPage.get_product_to_remove(product_id=self.product_id)
        remover.click()

    def test_basket_change_sum_of_one_product(self):
        product_card = product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()
        go_to_basket_button.click()

        product_count_input = self.basketPage.get_product_count_input()
        product_count_input.send_keys(Keys.ARROW_RIGHT)
        product_count_input.send_keys(Keys.BACK_SPACE)
        product_count_input.send_keys(PRODUCT_COUNT.__str__())

        anywhere = self.basketPage.get_any_field()
        anywhere.click()

        order_sum = self.basketPage.get_order_sum()
        product_price = self.basketPage.get_product_price(self.product_id)

        expected_sum = int(product_price.text) * PRODUCT_COUNT

        self.assertEqual(int(order_sum.text[:len(order_sum.text)-1]), expected_sum)

        remover = self.basketPage.get_product_to_remove(product_id=self.product_id)
        remover.click()

    def test_basket_change_sum_many_products(self):
        product_card = product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])

        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

        back_in_catalog = self.basketPage.get_back_in_catalog_link()
        back_in_catalog.click()

        product_card = self.oneProductPage.get_product_card_by_id(product_id=self.product_id+1)
        product_card.click()

        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()
        go_to_basket_button.click()

        product_sum_first = self.basketPage.get_product_sum(product_id=self.product_id)
        product_sum_second = self.basketPage.get_product_sum(product_id=self.product_id+1)

        order_sum = self.basketPage.get_order_sum()

        self.assertEqual(int(order_sum.text[:len(order_sum.text)-1]), int(product_sum_first.text) + int(product_sum_second.text))

        remover = self.basketPage.get_product_to_remove(product_id=self.product_id)
        remover.click()

        remover = self.basketPage.get_product_to_remove(product_id=self.product_id+1)
        remover.click()

    def test_basket_selector(self):
        product_card = product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()
        go_to_basket_button.click()

        select_elem = self.basketPage.get_delivery_selector()
        selector = Select(select_elem)
        selector.select_by_index(POST_OPTION)
        option = selector.first_selected_option
        self.assertEqual(option.text, "Почта россии")

        remover = self.basketPage.get_product_to_remove(product_id=self.product_id)
        remover.click()

    def test_success_order(self):
        product_card = product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=')+1:len(current_url)])
        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()
        go_to_basket_button.click()

        confirm_order_button = self.basketPage.get_confirm_order_button()
        confirm_order_button.click()

        profile_orders_title = self.profilePage.get_profile_orders_title()
        self.assertEqual(profile_orders_title.text, 'Мои заказы')

    def tearDown(self):

        self.driver.close()
        self.driver.quit()



