from tests.pages.BasePage import BasePage
from tests.pages.AdvertPage import AdvertPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

    image_input = '.profile-content__settings__image-loader__input'
    avatar_image = '.profile-content__avatar__image'
    navbar_image = '.mini-profile__avatar'

    old_password_div = '#settingOldPassword'
    old_password_input = '#settingOldPassword > .text-input__input'
    new_password_div = '#settingPassword'
    new_password_input = '#settingPassword > .text-input__input'
    change_password_btn = '#settings__change-password'

    name_div = '#settingName'
    name_input = '#settingName > .text-input__input'
    surname_div = '#settingSurname'
    surname_input = '#settingSurname > .text-input__input'
    phone_div = '#settingPhone'
    phone_input = '#settingPhone > .text-input__input'
    change_info_btn = '#settings__change-info'

    username = '.profile-content__username'
    navbar_username = '.mini-profile__capture'

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

    def fill_image_input(self, image):
        img_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.image_input)))
        img_input.send_keys(image)

    def get_avatar_src(self, selector):
        return self.wait_render(selector).get_attribute('src')

    def reset_pass(self, password):
        self.driver.get('https://volchock.ru/profile/settings')
        self.fill_input(self.old_password_input, 'password1')
        self.fill_input(self.new_password_input, password)
        self.wait_click(self.change_password_btn)
        self.is_exist(self.card_delete_cross)

    def reset_info(self):
        self.fill_input(self.name_input, 'test')
        self.fill_input(self.surname_input, 'kek')
        self.wait_click(self.change_info_btn)
        self.is_exist(self.card_delete_cross)
