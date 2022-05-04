from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from navbar.page import NavbarPage
from profile.page import ProfilePage
from signin.page import SignInPage
from signup.page import SignUpPage
from all_products.page import AllProductsPage
from one_product.page import OneProductPage
from basket.page import BasketPage

url = "https://goodvibesazot.tk/signup"

LOGIN = '12345'
PASSWORD = '12345'
LOGIN_NO_USER = 'adasdasdasd'
PASSWORD_INCORRECT = 'sdfsdfsdfsf'
PASSWORD_SHORT = '123'

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

    def wait_for_redirect_to_basket(self):
        return self.basketPage.get_page_title().text

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

    def wait_add_favourite_button(self):
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

    def wait_for_page_last_review(self):
        return self.oneProductPage.get_review().text

    def click_on_profile_reviews_link(self):
        reviews_link = self.navbarPage.get_reviews_link()
        reviews_link.click()

    def wait_for_profile_last_review(self):
        return self.profilePage.get_review().text

    def wait_review_error(self):
        return self.oneProductPage.get_review_error().text

    def click_on_back_to_catalog_link(self):
        back_to_catalog_link = self.oneProductPage.get_back_to_catalog_link()
        back_to_catalog_link.click()

    def wait_for_redirect_to_catalog(self):
        return self.allProductsPage.get_product_trends_title().text




