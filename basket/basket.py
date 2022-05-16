import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

from basket.utils import TestUtils
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
        self.testUtils = TestUtils(driver=self.driver)

    def test_basket(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_to_basket_button()

        self.testUtils.click_go_to_basket_button()

        self.testUtils.wait_product_in_basket(self.product_id)

        def finalizer():
            self.testUtils.remove_product_from_basket(self.product_id)

        finalizer()

    def test_basket_count(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_to_basket_button()

        self.testUtils.choose_products_count(PRODUCT_COUNT.__str__())

        self.testUtils.click_go_to_basket_button()

        count = self.testUtils.check_product_count_in_basket(self.product_id)

        self.assertEqual(count, PRODUCT_COUNT)

        def finalizer():
            self.testUtils.remove_product_from_basket(self.product_id)

        finalizer()

    def test_basket_refresh(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_to_basket_button()

        self.testUtils.click_go_to_basket_button()

        self.driver.refresh()

        self.testUtils.wait_product_in_basket(self.product_id)

        def finalizer():
            self.testUtils.remove_product_from_basket(self.product_id)

        finalizer()

    def test_basket_delete_product(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_to_basket_button()

        self.testUtils.click_go_to_basket_button()

        product_in_basket = self.testUtils.wait_product_in_basket(self.product_id)

        self.testUtils.remove_product_from_basket(self.product_id)

        self.testUtils.check_product_absence(product_in_basket)

    def test_basket_empty(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_to_basket_button()

        self.testUtils.click_go_to_basket_button()

        self.testUtils.remove_product_from_basket(self.product_id)

        empty_basket_text = self.testUtils.wait_for_empty_basket_notification()

        self.assertEqual(empty_basket_text, "Ваша корзина пуста. Вернуться к покупкам")

    def test_basket_increase_in_basket(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_to_basket_button()

        self.testUtils.click_go_to_basket_button()

        self.testUtils.choose_products_count_in_basket(PRODUCT_COUNT.__str__())

        self.testUtils.click_anywhere()

        count = self.testUtils.check_product_count_in_basket(self.product_id)
        self.assertEqual(count, PRODUCT_COUNT)

        def finalizer():
            self.testUtils.remove_product_from_basket(self.product_id)

        finalizer()

    def test_basket_change_sum_of_one_product(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_to_basket_button()

        self.testUtils.click_go_to_basket_button()

        self.testUtils.choose_products_count_in_basket(PRODUCT_COUNT.__str__())

        self.testUtils.click_anywhere()

        order_sum = self.testUtils.wait_order_sum()

        expected_sum = self.testUtils.wait_product_price(self.product_id) * PRODUCT_COUNT

        self.assertEqual(order_sum, expected_sum)

        def finalizer():
            self.testUtils.remove_product_from_basket(self.product_id)

        finalizer()

    def test_basket_change_sum_many_products(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_to_basket_button()

        self.testUtils.click_back_to_catalog_link()

        self.testUtils.click_on_product_by_id(self.product_id + 1)

        self.testUtils.click_add_to_basket_button()

        self.testUtils.click_go_to_basket_button()

        expected_sum = self.testUtils.get_expected_sum(self.product_id, self.product_id+1)

        order_sum = self.testUtils.wait_order_sum()

        self.assertEqual(order_sum, expected_sum)

        def finalizer():
            self.testUtils.remove_product_from_basket(self.product_id)
            self.testUtils.remove_product_from_basket(self.product_id+1)

        finalizer()

    def test_basket_selector(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_to_basket_button()

        self.testUtils.click_go_to_basket_button()

        option = self.testUtils.select_delivery_way(POST_OPTION)

        self.assertEqual(option, "Почта россии")

        def finalizer():
            self.testUtils.remove_product_from_basket(self.product_id)

        finalizer()

    def test_success_order(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_to_basket_button()

        self.testUtils.click_go_to_basket_button()

        order_sum = self.testUtils.wait_order_sum()

        self.testUtils.click_on_confirm_order_button()

        profile_orders_title = self.testUtils.wait_redirect_to_profile_orders()

        order_sum_last = self.testUtils.basketPage.get_last_sum_order()

        self.assertEqual(f'{order_sum} ₽', order_sum_last)
        #self.assertEqual(profile_orders_title, 'Мои заказы')

    def tearDown(self):

        self.driver.close()
        self.driver.quit()



