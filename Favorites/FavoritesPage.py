import selenium.common.exceptions

from Base.BasePage import Page
from Common.CommonComponents import Player, Tracks
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.utils import CHECK_FREQ, TIMEOUT


class FavoritesPage(Page):
    PATH = "favorites"
    DESCR_TITLE = "favorites__description-title"

    @property
    def track_list(self):
        return Tracks(self.driver)

    @property
    def player(self):
        return Player(self.driver)

    def _check_opened(self):
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.DESCR_TITLE))
        )

    def open(self):
        super().open()
        self._check_opened()

    def is_open(self):
        try:
            self._check_opened()
        except selenium.common.exceptions.TimeoutException:
            return False
        return True
