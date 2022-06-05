from base_page import BasePage
from navbar.static_locators import *


class NavbarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_profile_icon(self):
        profile_icon = self.get_element_by_class(avatar_icon_locator)
        profile_icon.click()

    def click_profile_link(self):
        profile_link = self.get_element_by_class(profile_link_locator)
        profile_link.click()

    def click_favourites_link(self):
        favourites_link = self.get_element_by_class(favourite_link_locator)
        favourites_link.click()

    def click_profile_reviews_link(self):
        reviews_link = self.get_element_by_class(profile_reviews_link_locator)
        reviews_link.click()

    def click_search_input(self):
        search_input = self.get_element_by_class(search_input_locator)
        search_input.click()

    def wait_result_search(self):
        return self.get_elements_by_css_selector(search_results_locator)

    def get_count_search_result(self):
        return self.wait_elements_disappear(search_results_locator)

    def fill_search_input(self, input_text):
        search_input = self.get_element_by_class(search_input_locator)
        search_input.send_keys(input_text)

    def click_on_category_search(self):
        categories_elements = self.get_elements_by_css_selector(search_categories_results_locator)
        clicked_category_name = categories_elements[0].text
        categories_elements[0].click()
        return clicked_category_name

    def click_on_product_search(self):
        product_elements = self.get_elements_by_css_selector(search_products_results_locator)
        clicked_product_name = product_elements[0].text
        product_elements[0].click()
        return clicked_product_name
