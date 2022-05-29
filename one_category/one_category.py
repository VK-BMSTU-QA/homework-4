import time

from selenium import webdriver

from navbar.page import NavbarPage
from utils.utils import Utils
from profile.page import ProfilePage
from signup.page import SignUpPage
from one_category.utils import TestUtils
from one_category.page import OneCategoryPage


import unittest

url = "https://goodvibesazot.tk/signin"
CLOTHES_CATEGORY = 'Одежда'
PRICE_BORDER_LEFT = '1000'
PRICE_BORDER_RIGHT = '50000'
PRICE_MORE_THAN_MAX = '5000000'
PRICE_LESS_THAN_MIN = '10'
ORDER_DESC = 'DESC'
ORDER_ASC = 'ASC'


class OneCategory(unittest.TestCase):
    def setUp(self):
        # EXE_PATH = r'C:\chromedriver.exe'
        # self.driver = webdriver.Chrome(executable_path=EXE_PATH)
        self.driver = webdriver.Chrome()
        self.utils = Utils(driver=self.driver)
        self.profilePage = ProfilePage(self.driver)
        self.navbarPage = NavbarPage(self.driver)
        self.oneCategoryPage = OneCategoryPage(self.driver)
        self.testUtils = TestUtils(driver=self.driver)
        self.utils.login()

    def test_sorting(self):
        self.testUtils.click_on_category_list_button()
        self.testUtils.click_on_category(CLOTHES_CATEGORY)

        self.testUtils.click_on_sort_by_price_button()
        self.assertTrue(self.testUtils.check_products_order(ORDER_DESC))
        self.testUtils.click_on_sort_by_price_button()
        self.assertTrue(self.testUtils.check_products_order(ORDER_ASC))

    def test_filter_price_in_borders(self):
        self.testUtils.click_on_category_list_button()
        self.testUtils.click_on_category(CLOTHES_CATEGORY)

        self.testUtils.fill_price_from_input(PRICE_BORDER_LEFT)
        self.testUtils.fill_price_to_input(PRICE_BORDER_RIGHT)

        self.testUtils.click_anywhere()

        self.assertTrue(self.testUtils.check_products_price_filter(int(PRICE_BORDER_LEFT), int(PRICE_BORDER_RIGHT)))

    def test_filter_price_min_more_than_max(self):
        self.testUtils.click_on_category_list_button()
        self.testUtils.click_on_category(CLOTHES_CATEGORY)

        self.testUtils.fill_price_from_input(PRICE_MORE_THAN_MAX)

        self.testUtils.click_anywhere()

        self.testUtils.wait_no_products_notification()

    def test_filter_price_max_less_than_min(self):
        self.testUtils.click_on_category_list_button()
        self.testUtils.click_on_category(CLOTHES_CATEGORY)

        self.testUtils.fill_price_to_input(PRICE_LESS_THAN_MIN)

        self.testUtils.click_anywhere()

        self.testUtils.wait_no_products_notification()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
