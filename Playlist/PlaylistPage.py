from Base.BasePage import Page
from Common.CommonComponents import Topbar
from Playlist.PlaylistComponents import PlaylistEditWindow, PlaylistImage, PlaylistPageControls, PlaylistTextBlock
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PlaylistPage(Page):
    PATH = "playlist/289"

    @property
    def controls(self):
        return PlaylistPageControls(self.driver)

    @property
    def playlist_image(self):
        return PlaylistImage(self.driver)

    @property
    def topbar(self):
        return Topbar(self.driver)

    @property
    def text_block(self):
        return PlaylistTextBlock(self.driver)

    @property
    def edit_window(self):
        return PlaylistEditWindow(self.driver)

    def open(self):
        super().open()
        WebDriverWait(self.driver, 10, 0.1).until(
            EC.presence_of_element_located((By.CLASS_NAME, "playlist__description-title"))
        )
