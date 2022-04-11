from tests.pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open(self):
        self.driver.get('https://volchock.ru/newAd')

    def fill_image_input(self, image):
        text_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.image_input)))
        text_input.send_keys(image)
        