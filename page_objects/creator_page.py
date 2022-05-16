import time

from page_objects.base import Page


class CreatorPage(Page):
    SHARE_ACCOUNT = 'div[class="creator-page__creator-toolbox"] > button.btn.btn_default'
    ACCOUNT_SHARED = 'div[class="text-center"]'
    LEVEL_CARD = 'div[class="level-card-container"] > div[class="level-card "] > button'
    POST_CARD = 'div[class="post-container"] > div[class="post-card"] > div[class="post-card__body"] > button'
    SUBSCRIBE_BUTTON = 'div[class="payment-page__topper__about"] > button'
    POST = 'div[class="post-page"]'

    def share_account(self):
        if self._check_drawable(self.POST_CARD):
            self._click_button(self.SHARE_ACCOUNT)

    def is_account_shared(self):
        return self._get_element(self.ACCOUNT_SHARED).text

    def pick_level(self):
        self._click_button(self.LEVEL_CARD)

    def subscribe(self):
        self._click_button(self.SUBSCRIBE_BUTTON)

    def open_post(self):
        self._click_button(self.POST_CARD)
        if self._check_drawable(self.POST):
            return self._check_drawable(self.POST)
        else:
            self._click_button(self.SUBSCRIBE_BUTTON)
            return self._check_current_url('https://yoomoney.ru/')
