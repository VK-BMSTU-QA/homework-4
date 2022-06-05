from selenium.webdriver import Keys

from base_page import BasePage


class OneProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_product_id(self):
        self.get_element_by_class('slider-preview__picture')
        current_url = self.driver.current_url
        return int(current_url[current_url.rfind('=') + 1:len(current_url)])

    def click_add_to_basket_button(self):
        add_to_basket_button = self.get_element_by_class('info-card-btn__cart')
        add_to_basket_button.click()

    def click_go_to_basket_button(self):
        go_to_basket_button = self.get_element_by_class('info-card-btn__wrap')
        go_to_basket_button.click()

    def wait_go_to_basket_button(self):
        return self.get_element_by_class('info-card-btn__wrap')

    def choose_products_count(self, count):
        product_count_input = self.get_element_by_class('product-page-spinner__count')
        product_count_input.send_keys(Keys.ARROW_RIGHT)
        product_count_input.send_keys(Keys.BACK_SPACE)
        product_count_input.send_keys(count)

    def click_add_favourite_button(self):
        add_favourite_button = self.get_element_by_class('info-favorite-btn__favorite')
        add_favourite_button.click()

    def wait_delete_from_favourite_button(self):
        return self.get_element_by_class('info-favorite-btn__favorite')

    def click_delete_from_favourite_button(self):
        delete_from_favourite_button = self.get_element_by_class('info-favorite-btn__favorite')
        delete_from_favourite_button.click()

    def write_review_text(self, text):
        review_text_field = self.get_element_by_class('add-comment-text')
        review_text_field.click()
        review_text_field.send_keys(text)

    def click_rating(self):
        rating_item = self.get_element_by_class('rating__items')
        rating_item.click()

    def click_review_button(self):
        review_button = self.get_element_by_class('add-comment-btn')
        review_button.click()

    def wait_for_reviews_on_page(self):
        return self.get_elements_by_css_selector('.feedback__content')

    def wait_review_error(self):
        return self.get_element_by_class('new-comment-alert-label').text

    def click_back_to_catalog_link(self):
        back_to_catalog_link = self.get_element_by_class('back-to-result__link')
        back_to_catalog_link.click()

    def get_product_title(self):
        return self.get_element_by_class('info-card__name')