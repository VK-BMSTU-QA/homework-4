from Base.BasePage import Page
from Common.CommonComponents import Albums, Sidebar, Tracks, Player, Topbar
from Home.HomeComponents import HomePlaylists


class HomePage(Page):
    PATH = ''

    @property
    def albums(self):
        return Albums(self.driver)

    @property
    def sidebar(self):
        return Sidebar(self.driver)

    @property
    def playlists(self):
        return HomePlaylists(self.driver)

    @property
    def tracks(self):
        return Tracks(self.driver)

    @property
    def player(self):
        return Player(self.driver)

    @property
    def topbar(self):
        return Topbar(self.driver)
