from tests.pages.BasePage import BasePage


class AdvertPage(BasePage):
    nav_to_main = '.category__list__main:nth-of-type(1)'
    nav_to_category = '.category__list__main:nth-of-type(2)'
    nav_to_elem = '.category__list__sub'
    active_image = '.mySlides:nth-of-type(1)'
    next_btn = '.gallery__next-button'
    second_dot = '.dot:nth-of-type(2)'
    show_map = '.advertisment-detail__add-info__location__name-block__maps-label'
    ymap = '.advertisment-detail__add-info__location__map'
    modal_window = '.modal-window'

    fav_btn = '.advertisment-detail__main-info__shop__capture'
    chat_btn = '#chatBtn'
    cart_btn = '#addToCartBtn'
    edit_btn = '#editBtn'

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
        self.wait_click(self.delete_btn)
        self.wait_click(self.delete_sign)

    def clearCart(self):
        self.driver.get('https://volchock.ru/profile/cart')
        self.wait_click(self.delete_btn)
        self.wait_click(self.delete_sign)

