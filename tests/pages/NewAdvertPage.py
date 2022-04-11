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
        text_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.image_input)))
        text_input.send_keys(image)

    def get_input_value(self, selector):
        return self.wait_render(selector).get_attribute('value')

    def delete_images(self):
        self.driver.get('https://volchock.ru/ad/13/edit')
        self.wait_click(self.delete_image)
        self.wait_click(self.delete_image)
        self.wait_click(self.submit_btn)
        self.is_exist(self.title)
        self.wait_redirect('https://volchock.ru/ad/13')

    def input_images(self):
        for _ in range(2):
            self.driver.get('https://volchock.ru/ad/13/edit')
            self.fill_image_input(os.getcwd()+"/tests/images/test.jpeg")
            self.is_exist(self.inputed_image)
            self.wait_click(self.submit_btn)
            self.wait_redirect('https://volchock.ru/ad/13')