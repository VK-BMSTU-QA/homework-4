import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

from one_product.utils import TestUtils
from utils.utils import Utils
from selenium.webdriver.support.ui import Select
from all_products.page import AllProductsPage
from one_product.page import OneProductPage
from basket.page import BasketPage
from profile.page import ProfilePage
from navbar.page import NavbarPage


PRODUCT_COUNT = 2
POST_OPTION = 2
REVIEW_TEXT = 'Хороший товар'


class OneProduct(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.product_id = 0
        self.utils = Utils(driver=self.driver)
        self.allProductsPage = AllProductsPage(self.driver)
        self.oneProductPage = OneProductPage(self.driver)
        self.basketPage = BasketPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.navbarPage = NavbarPage(self.driver)
        self.utils.login()
        self.testUtils = TestUtils(driver=self.driver)

    def test_one_product_button_add_product(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_to_basket_button()

        go_to_basket_button = self.testUtils.wait_go_to_basket_button()

        self.assertEqual(go_to_basket_button.text, 'ПЕРЕЙТИ В КОРЗИНУ')

        def finalizer():
            self.testUtils.click_go_to_basket_button()
            self.testUtils.remove_product_from_basket(self.product_id)

        finalizer()

    def test_one_product_redirect_to_basket(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_to_basket_button()

        self.testUtils.click_go_to_basket_button()

        self.testUtils.wait_for_redirect_to_basket()

        title = self.testUtils.wait_for_redirect_to_basket()
        self.assertEqual(title, 'Корзина')

        def finalizer():
            self.testUtils.remove_product_from_basket(self.product_id)

        finalizer()

    def test_one_product_change_product_count(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_to_basket_button()

        self.testUtils.choose_products_count(PRODUCT_COUNT.__str__())

        self.testUtils.click_go_to_basket_button()

        count = self.testUtils.check_product_count_in_basket(self.product_id)

        self.assertEqual(count, PRODUCT_COUNT)

        def finalizer():
            self.testUtils.remove_product_from_basket(self.product_id)

        finalizer()

    def test_one_product_favourite_button_changes(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_favourite_button()

        delete_from_favourite_button = self.testUtils.wait_delete_from_favourite_button()

        self.assertEqual(delete_from_favourite_button.text, 'УДАЛИТЬ ИЗ ИЗБРАННОГО')

        def finalizer():
            self.testUtils.click_delete_from_favourite_button()

        finalizer()

    def test_one_product_add_favourite_product(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_add_favourite_button()

        self.testUtils.click_on_profile_icon()

        self.testUtils.click_on_favourites_link()

        self.testUtils.wait_for_product_in_favourites(self.product_id)

    def test_one_product_review_under(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.write_review_text(REVIEW_TEXT)

        self.testUtils.click_rating()

        self.testUtils.click_review_button()

        review = self.testUtils.wait_for_page_last_review()

        self.assertEqual(review, REVIEW_TEXT)

    def test_one_product_review_users(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.write_review_text(REVIEW_TEXT)

        self.testUtils.click_rating()

        self.testUtils.click_review_button()

        self.testUtils.click_on_profile_icon()

        self.testUtils.click_on_profile_reviews_link()

        review = self.testUtils.wait_for_profile_last_review()
        self.assertEqual(review, REVIEW_TEXT)

    def test_one_product_review_error_no_rating(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.write_review_text(REVIEW_TEXT)

        self.testUtils.click_review_button()

        error = self.testUtils.wait_review_error()
        self.assertEqual(error, "Нужно выбрать оценку товара и написать отзыв")

    def test_one_product_review_error_no_text(self):
        self.product_id = self.testUtils.click_on_product()

        self.testUtils.click_rating()

        self.testUtils.click_review_button()

        error = self.testUtils.wait_review_error()
        self.assertEqual(error, "Нужно выбрать оценку товара и написать отзыв")

    def test_one_product_redirect_to_catalog(self):
        self.product_id = self.testUtils.click_on_product()

        back_to_catalog_link = self.oneProductPage.get_back_to_catalog_link()
        back_to_catalog_link.click()

        title = self.testUtils.wait_for_redirect_to_catalog()
        self.assertEqual(title, 'Рекомендации')








