from tests.pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class NewAdvertPage(BasePage):
    name_div = '.new-advert__name'
    name_input = '.new-advert__name > .text-input__input'
    price_div = '.new-advert__price'
    price_input = '.new-advert__price> .text-input__input'
    addres_div = '.new-advert__location'
    image_input = '#image_upload'
    text_area = '.textarea__textarea'
    inputed_image = '.image-uploader__image__img-container'
    delete_image = '.image-uploader__image__cross'
    clickable_map = '#YMapsID > ymaps > ymaps > ymaps > ymaps'
    submit_btn = '#newAdForm'
    cancel_btn = '.button-container > button'
    title = '.advertisment-detail__main-info__main__text__name'

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open(self):
        self.driver.get('https://volchock.ru/newAd')

    def fill_image_input(self, image):
        text_input = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.image_input)))
        text_input.send_keys(image)

    def get_input_value(self, selector):
        self.wait_until_text_in_attribute(selector, 'value', 'sometext')
        return self.wait_render(selector).get_attribute('value')

    def delete_images(self):
        self.driver.get('https://volchock.ru/ad/13/edit')
        self.wait_click(self.delete_image)
        self.wait_click(self.delete_image)
        self.wait_click(self.submit_btn)
        self.is_exist(self.title)
        self.wait_redirect('https://volchock.ru/ad/13')

    def input_images(self):
        for i in range(2):
            self.driver.get('https://volchock.ru/ad/13/edit')
            self.fill_image_input(os.getcwd()+f'/tests/images/test{i}.jpeg')
            self.wait_click(self.submit_btn)
            self.wait_visible(self.title)

    def change_advert_title(self, value):
        self.fill_input(self.name_input, value)

    def submit_changes(self):
        self.wait_click(self.submit_btn)
        self.wait_redirect('https://volchock.ru/ad/13')

    def cancel_changes(self):
        self.wait_click(self.cancel_btn)
        self.wait_redirect('https://volchock.ru/ad/13')

    def set_title_to_default(self):
        self.driver.get('https://volchock.ru/ad/13/edit')
        self.wait_render(self.name_input).clear()
        self.fill_input(self.name_input, 'Тест')
        self.submit_changes()

    def press_sumbit_button(self):
        self.wait_click(self.submit_btn)

    def is_error_in_title_input(self):
        name_div = self.wait_render(self.name_div)
        return "text-input_wrong" in name_div.get_attribute("class")

    def change_price_value(self, value):
        self.fill_input(self.price_input, value)

    def is_error_in_price_input(self):
        price_div = self.wait_render(self.price_div)
        return "text-input_wrong" in price_div.get_attribute("class")
    
    def is_error_in_addres_input(self):
        adr_div = self.wait_visible(self.addres_div)
        return "text-input_wrong" in adr_div.get_attribute("class")
    
    def clear_price_input(self):
        self.wait_render(self.price_input).clear()

    def is_image_exist(self):
        return self.is_exist(self.inputed_image)

    def delete_added_image(self):
        self.wait_click(self.delete_image)

    def click_map(self):
         self.wait_click(self.clickable_map)

    def is_redirected_to_updrage_page(self):
        return self.wait_any_redirect('upgrade')

    def fill_description(self, value):
        self.fill_input(self.text_area, value)