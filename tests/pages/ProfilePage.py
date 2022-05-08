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
    empty = '.profile-content-right__empty-ads'

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

    def press_delete(self):
        self.wait_click(self.delete_btn_main)
        return self.is_exist(self.card_delete_cross)

    def press_delete_not_main(self):
        self.wait_click(self.delete_btn)
        return self.is_exist(self.card_delete_cross)

    def press_delete_cross(self):
        self.wait_click(self.card_delete_cross)

    def is_profile_modal_exist(self):
        return self.is_exist(self.modal)

    def is_advert_exist(self):
        return not self.is_exist(self.empty)
        
    def click_buy_button(self):
        self.wait_render(self.advert)
        self.wait_click(self.buy_btn)
    
    def click_chat(self):
        self.wait_click(self.dialog_btn)
        return self.wait_redirect('https://volchock.ru/profile/chat/2/8')

    def send_chat_message(self, value):
        self.fill_input(self.chat_input, value)
        self.wait_click(self.chat_send_btn)

    def is_message_send(self):
        return self.is_exist(self.chat_message)
    
    def get_avatar_in_profile(self):
        return self.get_avatar_src(self.avatar_image)
    
    def get_avatar_in_navbar(self):
        return self.get_avatar_src(self.navbar_image)

    def is_error_in_new_password(self):
        new_div = self.wait_render(self.new_password_div)
        return "text-input_wrong" in new_div.get_attribute("class")

    def is_error_in_old_password(self):
        return self.wait_until_text_in_attribute(self.old_password_div, "class", "text-input_wrong")

    def click_change_password(self):
        self.wait_click(self.change_password_btn)

    def fill_new_password(self, value):
        self.fill_input(self.new_password_input, value)
    
    def fill_old_password(self, value):
        self.fill_input(self.old_password_input, value)

    def is_password_changed(self):
        return self.wait_until_text_in_attribute(self.new_password_div, "class", "text-input_correct")

    def fill_name(self, value):
         self.fill_input(self.name_input, value)

    def fill_surnname(self, value):
         self.fill_input(self.surname_input, value)
        
    def is_error_in_name(self):
        name_div = self.wait_render(self.name_div)
        return "text-input_wrong" in name_div.get_attribute("class")

    def is_error_in_surname(self):
        surname_div = self.wait_render(self.surname_div)
        return "text-input_wrong" in surname_div.get_attribute("class")

    def click_change_info(self):
        self.wait_click(self.change_info_btn)

    def is_name_changed(self):
        return self.wait_until_text_in_attribute(self.name_div, "class", "text-input_correct")

    def get_name_from_profile(self):
        return self.get_innerhtml(self.username)

    def get_name_from_navbar(self):
        return self.get_innerhtml(self.navbar_username)

    def fill_phone(self, value):
        self.fill_input(self.phone_input, value)

    def is_phone_changed(self):
        return self.wait_until_text_in_attribute(self.phone_div, "class", "text-input_correct")