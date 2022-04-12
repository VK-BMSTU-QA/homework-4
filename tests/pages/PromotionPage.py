from tests.pages.BasePage import BasePage


class PromotionPage(BasePage):
    profile_btn = '.button-minor'
    promote_btn = '.payment__btn'

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def open(self, id):
        self.driver.get(self.promotion_url(id))
