import unittest

from selenium import webdriver

from navbar.utils import TestUtils

url = "https://goodvibesazot.tk"

COUNT_ELEMENTS_IN_SEARCH_DEFAULT = 9


class Search(unittest.TestCase):
    def setUp(self):
        EXE_PATH = r'C:\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=EXE_PATH)
        self.testUtils = TestUtils(self.driver)
        self.driver.get(url=url)

    def test_get_list_search(self):
        self.testUtils.click_search_input()

        elements = self.testUtils.wait_result_search()

        self.assertEqual(len(elements), COUNT_ELEMENTS_IN_SEARCH_DEFAULT)

    def test_click_on_product(self):
        self.testUtils.click_search_input()

        product_elements = self.testUtils.wait_result_products_search()

        self.assertEqual(product_elements[0].text,
                         self.testUtils.check_redirect_on_product(product_elements[0]).text)

    def test_click_on_category(self):
        self.testUtils.click_search_input()

        categories_elements = self.testUtils.wait_result_categories_search()

