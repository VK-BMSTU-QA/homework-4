from navbar.page import NavbarPage
from one_product.page import OneProductPage


class TestUtils:
    def __init__(self, driver):
        self.driver = driver
        self.navbarPage = NavbarPage(self.driver)
        self.productPage = OneProductPage(self.driver)

    def click_search_input(self):
        search_input = self.navbarPage.get_search_input()
        search_input.click()

    def wait_result_search(self):
        return self.navbarPage.get_search_result_elements()

    def wait_result_products_search(self):
        return self.navbarPage.get_search_result_products_elements()

    def wait_result_categories_search(self):
        return self.navbarPage.get_search_result_categories_elements()

    def check_redirect_on_product(self, product):
        product.click()
        return self.productPage.get_product_name()
