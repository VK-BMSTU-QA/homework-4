from Base.BasePage import Page
from Common.CommonComponents import Albums, Player, Tracks
from Search.SearchComponents import MainLayout, SearchBar


class SearchPage(Page):
    path = "search"

    @property
    def search_bar(self):
        return SearchBar(self.driver)

    @property
    def main_layout(self):
        return MainLayout(self.driver)

    @property
    def tracks(self):
        return Tracks(self.driver)

    @property
    def albums(self):
        return Albums(self.driver)

    @property
    def player(self):
        return Player(self.driver)
