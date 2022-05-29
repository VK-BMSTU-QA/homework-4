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
        return int(current_url[current_url.rfind('=') + 1:len(current_url)])

    def click_add_to_basket_button(self):
        add_to_basket_button = self.oneProductPage.get_add_to_basket_button()
        add_to_basket_button.click()

    def click_go_to_basket_button(self):
        go_to_basket_button = self.oneProductPage.get_go_to_basket_button()
        go_to_basket_button.click()

    def wait_go_to_basket_button(self):
        return self.oneProductPage.get_go_to_basket_button()

    def remove_product_from_basket(self, product_id):
        remover = self.basketPage.get_product_to_remove(product_id=product_id)
        remover.click()

    def choose_products_count(self, count):
        product_count_input = self.oneProductPage.get_product_count_input()
        product_count_input.send_keys(Keys.ARROW_RIGHT)
        product_count_input.send_keys(Keys.BACK_SPACE)
        product_count_input.send_keys(count)

    def check_product_count_in_basket(self, product_id):
        product_sum = self.basketPage.get_product_sum(product_id)
        product_price = self.basketPage.get_product_price(product_id)

        return int(int(product_sum.text) / int(product_price.text))

    def click_add_favourite_button(self):
        add_favourite_button = self.oneProductPage.get_favourite_button()
        add_favourite_button.click()

    def wait_delete_from_favourite_button(self):
        return self.oneProductPage.get_favourite_button()

    def click_delete_from_favourite_button(self):
        delete_from_favourite_button = self.oneProductPage.get_favourite_button()
        delete_from_favourite_button.click()

    def click_on_profile_icon(self):
        profile_icon = self.navbarPage.get_profile_icon()
        profile_icon.click()

    def click_on_favourites_link(self):
        favourites_link = self.navbarPage.get_favourites_link()
        favourites_link.click()

    def wait_for_product_in_favourites(self, product_id):
        return self.profilePage.get_favourite_product(product_id)

    def write_review_text(self, text):
        review_text_field = self.oneProductPage.get_review_text_field()
        review_text_field.click()
        review_text_field.send_keys(text)

    def click_rating(self):
        rating_item = self.oneProductPage.get_rating_item()
        rating_item.click()

    def click_review_button(self):
        review_button = self.oneProductPage.get_add_review_button()
        review_button.click()

    def wait_for_reviews_on_page(self):
        return self.oneProductPage.get_reviews()

    def click_on_profile_reviews_link(self):
        reviews_link = self.navbarPage.get_reviews_link()
        reviews_link.click()

    def wait_review_error(self):
        return self.oneProductPage.get_review_error().text

    def wait_for_redirect_to_catalog(self):
        return self.allProductsPage.get_product_trends_title().text

    def click_on_certain_fav_product(self, product_id):
        product = self.profilePage.get_fav_product_by_id(product_id)
        product.click()

    def wait_product_review(self, product_id):
        self.profilePage.get_product_by_id(product_id)




