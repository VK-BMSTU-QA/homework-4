import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from all_products.page import AllProductsPage
from basket.page import BasketPage
from navbar.page import NavbarPage
from one_product.page import OneProductPage
from profile.page import ProfilePage
from utils.utils import Utils

PRODUCT_COUNT = 2
POST_OPTION = 2
REVIEW_TEXT = 'Хороший товар'


class OneProduct(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.product_id = 0
        self.allProductsPage = AllProductsPage(self.driver)
        self.oneProductPage = OneProductPage(self.driver)
        self.basketPage = BasketPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.navbarPage = NavbarPage(self.driver)

        self.utils = Utils(driver=self.driver)
        self.utils.login()

    def test_one_product_button_add_product(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.click_add_to_basket_button()

        self.assertEqual(self.oneProductPage.wait_go_to_basket_button().text, 'ПЕРЕЙТИ В КОРЗИНУ')

        def finalizer():
            self.oneProductPage.click_go_to_basket_button()
            self.basketPage.click_on_cross_to_delete_product(self.product_id)

        finalizer()

    def test_one_product_change_product_count(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.click_add_to_basket_button()

        self.oneProductPage.choose_products_count(PRODUCT_COUNT.__str__())

        self.oneProductPage.click_go_to_basket_button()

        self.assertEqual(self.basketPage.check_product_count(self.product_id), PRODUCT_COUNT)

        def finalizer():
            self.basketPage.click_on_cross_to_delete_product(self.product_id)

        finalizer()

    def test_one_product_favourite_button_changes(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.click_add_favourite_button()

        self.assertEqual(self.oneProductPage.wait_delete_from_favourite_button().text, 'УДАЛИТЬ ИЗ ИЗБРАННОГО')

        self.oneProductPage.click_delete_from_favourite_button()

    def test_one_product_add_favourite_product(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.click_add_favourite_button()

        self.navbarPage.click_profile_icon()

        self.navbarPage.click_favourites_link()

        self.profilePage.get_favourite_product(self.product_id)

        def finalizer():
            self.profilePage.click_on_certain_fav_product(self.product_id)
            self.oneProductPage.click_delete_from_favourite_button()

        finalizer()

    def test_one_product_review_positive(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.write_review_text(REVIEW_TEXT)

        self.oneProductPage.click_rating()

        self.oneProductPage.click_review_button()

        received_review = ''

        reviews = self.oneProductPage.wait_for_reviews_on_page()
        for review in reviews:
            if review.text == REVIEW_TEXT:
                received_review = review

        self.assertEqual(received_review.text, REVIEW_TEXT)

        self.navbarPage.click_profile_icon()

        self.navbarPage.click_profile_reviews_link()

        self.profilePage.wait_product_review(self.product_id)

    def test_one_product_review_error_no_rating(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.write_review_text(REVIEW_TEXT)

        self.oneProductPage.click_review_button()

        error = self.oneProductPage.wait_review_error()
        self.assertEqual(error, "Нужно выбрать оценку товара и написать отзыв")

    def test_one_product_review_error_no_text(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.click_rating()

        self.oneProductPage.click_review_button()

        error = self.oneProductPage.wait_review_error()
        self.assertEqual(error, "Нужно выбрать оценку товара и написать отзыв")

    def test_one_product_redirect_to_catalog(self):
        self.allProductsPage.click_on_product_card()
        self.product_id = self.oneProductPage.get_product_id()

        self.oneProductPage.click_back_to_catalog_link()

        self.assertEqual(self.allProductsPage.get_product_trends_title(), 'Рекомендации')

    def tearDown(self):
        self.driver.quit()
