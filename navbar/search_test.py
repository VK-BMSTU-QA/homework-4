import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from all_products.page import AllProductsPage
from basket.page import BasketPage
from navbar.page import NavbarPage
from one_category.page import OneCategoryPage
from one_product.page import OneProductPage
from profile.page import ProfilePage
from utils.utils import Utils

COUNT_ELEMENTS_IN_SEARCH_DEFAULT = 9
SEARCH_STRING = "джи"
SEARCH_STRING_INCORRECT = "incorrect_string_for_search"


class Search(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.allProductsPage = AllProductsPage(self.driver)
        self.oneProductPage = OneProductPage(self.driver)
        self.basketPage = BasketPage(self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.navbarPage = NavbarPage(self.driver)
        self.oneCategoryPage = OneCategoryPage(self.driver)

        self.utils = Utils(driver=self.driver)
        self.utils.login()

    def test_search_get_list(self):
        self.navbarPage.click_search_input()

        self.assertEqual(len(self.navbarPage.wait_result_search()), COUNT_ELEMENTS_IN_SEARCH_DEFAULT)

    def test_search_click_on_product(self):
        self.navbarPage.click_search_input()

        clicked_product = self.navbarPage.click_on_product_search()

        self.assertEqual(clicked_product,
                         self.oneProductPage.get_product_title().text)

    def test_search_click_on_category(self):
        self.navbarPage.click_search_input()

        clicked_category = self.navbarPage.click_on_category_search()

        self.assertEqual(clicked_category, self.oneCategoryPage.get_category_name().text)

    def test_search_input_text(self):
        self.navbarPage.fill_search_input(SEARCH_STRING)

        elements = self.navbarPage.wait_result_search()

        for i in elements:
            self.assertFalse(SEARCH_STRING in i.text)

    def test_search_input_text_incorrect(self):
        self.navbarPage.fill_search_input(SEARCH_STRING_INCORRECT)

        self.assertEqual(self.navbarPage.get_count_search_result(), True)

    def tearDown(self):
        self.driver.quit()
