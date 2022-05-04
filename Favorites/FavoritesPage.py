from Base.BasePage import Page
from Common.CommonComponents import Player, Tracks
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FavoritesPage(Page):
    PATH = "favorites"

    @property
    def track_list(self):
        return Tracks(self.driver)

    @property
    def player(self):
        return Player(self.driver)

    def open(self):
        super().open()
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "favorites__description-title"))
        )
