from tests.pages.BasePage import BasePage
from tests.pages.AdvertPage import AdvertPage


class ProfilePage(BasePage):
    adv_btn = '.profile-content__buttons > .button'
    fav_btn = '.button:nth-of-type(2)'
    cart_btn = '.button:nth-of-type(3)'
    chat_btn = '.button:nth-of-type(4)'
    promo_btn = '.button:nth-of-type(5)'
    set_btn = '.button:nth-of-type(6)'
    archive_btn = '.profile-content-right__ads-type:nth-of-type(2)'
    delete_btn_main = '.profile-content-right__ads-type:nth-of-type(3)'
    delete_btn = '.profile-content-right__ads-type'

    advert = '.card__content'
    card_delete_cross = '.card__delete'
    modal = '#modal-1'
    buy_btn = '.card-info__card_buy'
    dialog_btn = '.chat_chats_panel'
    chat_input = '.chat_input_input'
    chat_send_btn = '.chat_input_button'
    chat_message = '.chat_history_element__user'
    

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open(self):
        self.driver.get('https://volchock.ru/profile')


    def add_to_fav(self):
        adv_page = AdvertPage(self.driver)
        adv_page.open(8)
        adv_page.get_innerhtml(adv_page.fav_btn)
        adv_page.wait_until_innerhtml_changes_after_click(adv_page.fav_btn)
        self.driver.get('https://volchock.ru/profile/favorite')

    def add_to_cart(self):
        adv_page = AdvertPage(self.driver)
        adv_page.open(8)
        adv_page.get_innerhtml(adv_page.cart_btn)
        adv_page.wait_until_innerhtml_changes_after_click(adv_page.cart_btn)
        self.driver.get('https://volchock.ru/profile/cart')
