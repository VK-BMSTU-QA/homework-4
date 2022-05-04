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
from navbar.page import NavbarPage


PRODUCT_COUNT = 2
POST_OPTION = 2
REVIEW_TEXT = 'Хороший товар'


class OneProduct(unittest.TestCase):
    def setUp(self):
        EXE_PATH = r'C:\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=EXE_PATH)
        self.product_id = 0
        self.utils = Utils(driver=self.driver)
        self.allProductsPage = AllProductsPage(self.driver)
        self.oneProductPage = OneProductPage(self.driver)
        self.basketPage = BasketPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.navbarPage = NavbarPage(self.driver)
        self.utils.login()

    def test_one_product_button_add_product(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=') + 1:len(current_url)])

        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()

        self.assertEqual(go_to_basket_button.text, 'ПЕРЕЙТИ В КОРЗИНУ')

        go_to_basket_button.click()
        remover = self.basketPage.get_product_to_remove(product_id=self.product_id)
        remover.click()

    def test_one_product_redirect_to_basket(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=') + 1:len(current_url)])

        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()
        go_to_basket_button.click()

        title = self.basketPage.get_page_title()
        self.assertEqual(title.text, 'Корзина')

        remover = self.basketPage.get_product_to_remove(product_id=self.product_id)
        remover.click()

    def test_one_product_change_product_count(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()
        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=') + 1:len(current_url)])

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

    def test_one_product_favourite_button_changes(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=') + 1:len(current_url)])

        add_favourite_button = self.oneProductPage.get_favourite_button()
        add_favourite_button.click()

        delete_from_favourite_button = self.oneProductPage.get_favourite_button()

        self.assertEqual(delete_from_favourite_button.text, 'УДАЛИТЬ ИЗ ИЗБРАННОГО')

        delete_from_favourite_button.click()

    def test_one_product_add_favourite_product(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=') + 1:len(current_url)])

        add_favourite_button = self.oneProductPage.get_favourite_button()
        add_favourite_button.click()

        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

        favourites_link = self.navbarPage.get_favourites_link()
        favourites_link.click()

        product = self.profilePage.get_favourite_product(self.product_id)

    def test_one_product_review_under(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=') + 1:len(current_url)])

        review_text_field = self.oneProductPage.get_review_text_field()
        review_text_field.click()
        review_text_field.send_keys(REVIEW_TEXT)

        rating_item = self.oneProductPage.get_rating_item()
        rating_item.click()

        review_button = self.oneProductPage.get_add_review_button()
        review_button.click()

        review = self.oneProductPage.get_review()
        self.assertEqual(review.text, REVIEW_TEXT)

    def test_one_product_review_users(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=') + 1:len(current_url)])

        review_text_field = self.oneProductPage.get_review_text_field()
        review_text_field.click()
        review_text_field.send_keys(REVIEW_TEXT)

        rating_item = self.oneProductPage.get_rating_item()
        rating_item.click()

        review_button = self.oneProductPage.get_add_review_button()
        review_button.click()

        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

        reviews_link = self.navbarPage.get_reviews_link()
        reviews_link.click()

        review = self.profilePage.get_review()
        self.assertEqual(review.text, REVIEW_TEXT)

    def test_one_product_review_error_no_rating(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=') + 1:len(current_url)])

        review_text_field = self.oneProductPage.get_review_text_field()
        review_text_field.click()
        review_text_field.send_keys(REVIEW_TEXT)

        review_button = self.oneProductPage.get_add_review_button()
        review_button.click()

        error = self.oneProductPage.get_review_error()
        self.assertEqual(error.text, "Нужно выбрать оценку товара и написать отзыв")

    def test_one_product_review_error_no_text(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=') + 1:len(current_url)])

        rating_item = self.oneProductPage.get_rating_item()
        rating_item.click()

        review_button = self.oneProductPage.get_add_review_button()
        review_button.click()

        error = self.oneProductPage.get_review_error()
        self.assertEqual(error.text, "Нужно выбрать оценку товара и написать отзыв")

    def test_one_product_redirect_to_catalog(self):
        product_card = self.allProductsPage.get_product_card()
        product_card.click()

        one_product = self.oneProductPage.get_product_card()
        current_url = self.driver.current_url
        self.product_id = int(current_url[current_url.rfind('=') + 1:len(current_url)])

        back_to_catalog_link = self.oneProductPage.get_back_to_catalog_link()
        back_to_catalog_link.click()

        title = self.allProductsPage.get_product_trends_title()
        self.assertEqual(title.text, 'Рекомендации')








