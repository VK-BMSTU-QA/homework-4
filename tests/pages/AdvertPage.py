from tests.pages.BasePage import BasePage


class AdvertPage(BasePage):
    nav_to_main = '.category__list__main:nth-of-type(1)'
    nav_to_category = '.category__list__main:nth-of-type(2)'
    nav_to_elem = '.category__list__sub'
    active_image = '.mySlides:nth-of-type(1)'
    second_image = '.mySlides:nth-of-type(2)'
    next_btn = '.gallery__next-button'
    second_dot = '.dot:nth-of-type(2)'
    show_map = '.advertisment-detail__add-info__location__name-block__maps-label'
    ymap = '.advertisment-detail__add-info__location__map'
    modal_window = '.modal-window'
    title = '.advertisment-detail__main-info__main__text__name'
    modal_backgroud = '.blackout'
    open_modal_btn = '#auth'

    fav_btn = '.advertisment-detail__main-info__shop__capture'
    chat_btn = '#chatBtn'
    cart_btn = '#addToCartBtn'
    edit_btn = '#editBtn'
    card = '.card__content'
    empty = '#empty'

    delete_btn = '#deleteBtn'
    delete_sign = '.card__delete'

    salesman_avatar = '.advertisment-detail__main-info__shop__salesman__avatar'
    salesman_name = '.advertisment-detail__main-info__shop__salesman__info__name'

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open(self, id):
        self.driver.get(self.advert_url(id))

    def clearFav(self):
        self.driver.get('https://volchock.ru/profile/favorite')
        if not self.is_exist(self.empty):
            card = self.wait_render(self.card)
            self.wait_click(self.delete_btn)
            self.wait_click(self.delete_sign)
            self.wait_for_delete(card)

    def clearCart(self):
        self.driver.get('https://volchock.ru/profile/cart')
        if not self.is_exist(self.empty):
            card = self.wait_render(self.card)
            self.wait_click(self.delete_btn)
            self.wait_click(self.delete_sign)
            self.wait_for_delete(card)

    def toggle_map(self):
        self.wait_click(self.show_map)

    def is_map_visible(self):
        return self.is_exist(self.ymap)

    def close_modal(self):
        self.click_at_position(self.modal_backgroud, 1, 1)

    def click_fav(self):
        self.wait_click(self.fav_btn)

    def click_cart(self):
        self.wait_click(self.cart_btn)
    
    def click_chat(self):
        self.wait_click(self.chat_btn)

    def is_modal_active(self):
        return self.is_exist(self.modal_window)

    def is_cart_btn_exist(self):
        return self.is_exist(self.cart_btn)
    
    def is_chat_btn_exist(self):
        return self.is_exist(self.cart_btn)

    def is_fav_redirect_to_profile(self):
        self.wait_click(self.fav_btn)
        return self.wait_redirect('https://volchock.ru/profile')

    def is_edit_after_click(self):
        self.wait_click(self.edit_btn)
        return self.wait_any_redirect('edit')

    def is_first_image_visible(self):
        return self.is_exist(self.active_image)

    def change_image_by_clicking_pointer(self):
        self.wait_click(self.next_btn)
    
    def change_image_by_clicking_dot(self):
        self.wait_click(self.second_dot)

    def is_redirected_to_chat(self):
        return self.wait_redirect('https://volchock.ru/profile/chat/2/8')

    def fav_btn_text(self):
        return self.get_innerhtml(self.fav_btn)

    def cart_btn_text(self):
        return self.get_innerhtml(self.cart_btn)

    def change_cart_text(self):
        self.wait_until_innerhtml_changes_after_click(self.cart_btn)

    def change_fav_text(self):
        self.wait_until_innerhtml_changes_after_click(self.fav_btn)

    def is_redirected_to_fav(self):
        return self.wait_redirect('https://volchock.ru/profile/favorite')

    def is_redirected_to_cart(self):
        return self.wait_redirect('https://volchock.ru/profile/cart')

    def check_log(self):
        return self.is_exist(self.open_modal_btn)