import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from all_products.page import AllProductsPage
from basket.page import BasketPage
from one_product.page import OneProductPage
from profile.page import ProfilePage
from utils.utils import Utils

PRODUCT_COUNT = 2
POST_OPTION = 2


class Basket(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.product_id = 0
        self.utils = Utils(driver=self.driver)
        self.allProductsPage = AllProductsPage(self.driver)
        self.oneProductPage = OneProductPage(self.driver)
        self.basketPage = BasketPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.utils.login()

    def test_basket_product_in_cart_check(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.click_add_to_basket_button()

        self.oneProductPage.click_go_to_basket_button()

        self.basketPage.wait_product_in_basket(self.product_id)

        def finalizer():
            self.basketPage.click_on_cross_to_delete_product(self.product_id)

        finalizer()

    def test_basket_products_count_check(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.click_add_to_basket_button()

        self.oneProductPage.choose_products_count(PRODUCT_COUNT.__str__())

        self.oneProductPage.click_go_to_basket_button()

        self.assertEqual(self.basketPage.check_product_count(self.product_id), PRODUCT_COUNT)

        def finalizer():
            self.basketPage.click_on_cross_to_delete_product(self.product_id)

        finalizer()

    def test_basket_empty_notification(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.click_add_to_basket_button()

        self.oneProductPage.click_go_to_basket_button()

        self.basketPage.click_on_cross_to_delete_product(self.product_id)

        self.assertEqual(self.basketPage.wait_for_empty_basket_notification(),
                         "Ваша корзина пуста. Вернуться к покупкам")

    def test_basket_change_sum_of_one_product(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.click_add_to_basket_button()

        self.oneProductPage.click_go_to_basket_button()

        self.basketPage.choose_products_count(PRODUCT_COUNT.__str__())

        self.basketPage.click_anywhere()

        self.assertEqual(self.basketPage.get_order_sum(),
                         self.basketPage.get_product_price(self.product_id) * PRODUCT_COUNT)

        def finalizer():
            self.basketPage.click_on_cross_to_delete_product(self.product_id)

        finalizer()

    def test_basket_change_sum_many_products(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.click_add_to_basket_button()

        self.oneProductPage.click_back_to_catalog_link()

        self.allProductsPage.click_on_product_by_id(self.product_id + 1)

        self.oneProductPage.click_add_to_basket_button()

        self.oneProductPage.click_go_to_basket_button()

        self.assertEqual(self.basketPage.get_order_sum(),
                         self.basketPage.get_expected_sum(self.product_id, self.product_id + 1))

        def finalizer():
            self.basketPage.click_on_cross_to_delete_product(self.product_id)
            self.basketPage.click_on_cross_to_delete_product(self.product_id + 1)

        finalizer()

    def test_basket_selector_check(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.click_add_to_basket_button()

        self.oneProductPage.click_go_to_basket_button()

        option = self.basketPage.select_delivery_way(POST_OPTION)

        self.assertEqual(option, "Почта россии")

        def finalizer():
            self.basketPage.click_on_cross_to_delete_product(self.product_id)

        finalizer()

    def test_basket_success_order(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.click_add_to_basket_button()

        self.oneProductPage.click_go_to_basket_button()

        order_sum = self.basketPage.get_order_sum()

        self.basketPage.click_on_confirm_order_button()

        self.assertEqual(f'{order_sum} ₽', self.profilePage.get_last_sum_order())

    def tearDown(self):
        self.driver.quit()
