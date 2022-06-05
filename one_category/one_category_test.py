import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from all_products.page import AllProductsPage
from navbar.page import NavbarPage
from one_category.page import OneCategoryPage
from profile.page import ProfilePage
from utils.utils import Utils

url = "https://goodvibesazot.tk/signin"
CLOTHES_CATEGORY = 'Одежда'
PRICE_BORDER_LEFT = '4000'
PRICE_BORDER_RIGHT = '50000'
PRICE_MORE_THAN_MAX = '5000000'
PRICE_LESS_THAN_MIN = '10'
ORDER_DESC = 'DESC'
ORDER_ASC = 'ASC'


class OneCategory(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.utils = Utils(driver=self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.navbarPage = NavbarPage(self.driver)
        self.oneCategoryPage = OneCategoryPage(self.driver)
        self.allProductsPage = AllProductsPage(self.driver)
        self.utils.login()

    def test_category_sorting_by_price(self):
        self.allProductsPage.click_on_category_list_button()
        self.allProductsPage.click_on_category(CLOTHES_CATEGORY)

        self.oneCategoryPage.click_on_sort_by_price_button()
        self.assertTrue(self.oneCategoryPage.check_products_order(ORDER_DESC))
        self.oneCategoryPage.click_on_sort_by_price_button()
        self.assertTrue(self.oneCategoryPage.check_products_order(ORDER_ASC))

    def test_category_filter_price_in_borders(self):
        self.allProductsPage.click_on_category_list_button()
        self.allProductsPage.click_on_category(CLOTHES_CATEGORY)

        self.oneCategoryPage.fill_price_from_input(PRICE_BORDER_LEFT)
        self.oneCategoryPage.fill_price_to_input(PRICE_BORDER_RIGHT)

        self.oneCategoryPage.click_anywhere()

        self.assertTrue(self.oneCategoryPage.check_products_price_filter(PRICE_BORDER_LEFT, PRICE_BORDER_RIGHT))

    def test_category_filter_price_min_more_than_max(self):
        self.allProductsPage.click_on_category_list_button()
        self.allProductsPage.click_on_category(CLOTHES_CATEGORY)

        self.oneCategoryPage.fill_price_from_input(PRICE_MORE_THAN_MAX)

        self.oneCategoryPage.click_anywhere()

        self.oneCategoryPage.wait_no_products_notification()

    def test_category_filter_price_max_less_than_min(self):
        self.allProductsPage.click_on_category_list_button()
        self.allProductsPage.click_on_category(CLOTHES_CATEGORY)

        self.oneCategoryPage.fill_price_to_input(PRICE_LESS_THAN_MIN)

        self.oneCategoryPage.click_anywhere()

        self.oneCategoryPage.wait_no_products_notification()

    def tearDown(self):
        self.driver.quit()
