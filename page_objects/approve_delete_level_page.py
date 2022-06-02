from page_objects.base import Page


class ApproveDeleteLevelPage(Page):
    LEVEL_CANCEL_BUTTON = 'div[class="confirm-component__button-box"] > button[class="btn btn_success "]'
    LEVEL_DELETE_BUTTON = 'div[class="confirm-component__button-box"] > button[class="btn btn_primary "]'

    def cancel_delete_level(self):
        self._click_button(self.LEVEL_CANCEL_BUTTON)

    def delete_level(self):
        self._click_button(self.LEVEL_DELETE_BUTTON)
