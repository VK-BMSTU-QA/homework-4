from tests.pages.BasePage import BasePage


class MainPage(BasePage):
    new_advert_btn = '.new-advert-capture-container'
    open_modal_btn = '#auth'
    header_profile = '.mini-profile__capture'
    search_input = '.search__input'
    search_btn = '.search__button'
    lang_btn = '.lang-box'
    input_err = '.text-input_wrong'
    categories = '.root__category-container'
    category_href = '.root__category__content-categories-card-title'
    card = '.card__content'
    search_input = '.search__input'
    search_btn = '.search__button'
    empty = '#empty'
    lang_btn = '.lang-box'
    modal_window = '.modal-window'
    new_adv_btn = '.new-advert-capture-container'
    expand_menu = '.expand-menu__content'

    profile_link = '.expand-menu__sublabel:nth-of-type(1)'
    fav_link = '.expand-menu__sublabel:nth-of-type(2)'
    setting_link = '.expand-menu__sublabel:nth-of-type(3)'
    logout_btn = '#logout'

    login_email_div = '#logEmail'
    login_email_input = '#logEmail > .text-input__input'
    login_password_div = '#logPassword'
    login_password_input = '#logPassword > .text-input__input'
    login_btn = '#logButton'

    swith_to_reg_btn = '#overlay-sign-up'
    reg_email_div = '#regEmail'
    reg_email_input = '#regEmail > .text-input__input'
    reg_name_div = '#regName'
    reg_name_input = '#regName > .text-input__input'
    reg_surname_div = '#regSurname'
    reg_surname_input = '#regSurname > .text-input__input'
    reg_password_div = '#regPassword'
    reg_password_input = '#regPassword > .text-input__input'
    reg_reppassword_div = '#regRepPassword'
    reg_reppassword_input = '#regRepPassword > .text-input__input'
    reg_btn = '#regButton'

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open(self):
        self.driver.get(self.BASE_URL)

    def click_login(self):
        elem = self.wait_render(self.open_modal_btn)
        elem.click()

    def click_new_adv(self):
        elem = self.wait_render(self.new_advert_btn)
        elem.click()
