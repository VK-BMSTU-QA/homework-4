from all_products.static_locators import *
from base_page import BasePage


class AllProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_product_trends_title(self):
        return self.get_element_by_css_selector(trends_title_locator).text

    def click_on_product_card(self):
        product_card = self.get_element_by_class(product_card_locator)
        product_card.click()

    def click_on_product_by_id(self, product_id):
        product_card = self.get_element_by_css_selector(f'div[href="/product?id={product_id}"]')
        product_card.click()

    def click_on_category_list_button(self):
        category_list_button = self.get_element_by_class(category_list_button_locator)
        category_list_button.click()

    def click_on_category(self, category_name):
        all_categories = self.get_elements_by_css_selector(category_list_locator)
        category_need = ''
        for category in all_categories:
            if category.text == category_name:
                category_need = category
                break

        category_need.click()
