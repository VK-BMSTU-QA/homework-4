from page_objects.base import Page


class ApproveDeleteLevelPage(Page):
    LEVEL_SAVE_BUTTON = 'button[class="btn btn_success "]'
    LEVEL_DELETE_BUTTON = 'button[class="btn btn_primary "]'

    def cancel_delete_level(self):
        self._click_button(self.LEVEL_SAVE_BUTTON)

    def delete_level(self):
        self._click_button(self.LEVEL_SAVE_BUTTON)
