from tests.pages.BasePage import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # открывает главную страницу сайта
    def open(self):
        self.driver.get(self.BASE_URL)

    # открывает окно логина
    def click_login(self):
        elem = self.wait_render(self.login_btn)
        elem.click()

    def click_signup(self):
        elem = self.wait_render(self.signup_btn)
        elem.click()

    def click_search(self):
        elem = self.wait_render(self.search_btn)
        elem.click()

    def click_player(self):
        elem = self.wait_render(self.player_btn)
        elem.click()

    def click_first_film_info(self):
        elem = self.wait_render(self.film_info_btn)
        elem.click()

    def click_genre_comedy(self):
        elem = self.wait_render(self.genre_comedy)
        elem.click()

    def click_popular_film(self):
        elem = self.wait_render(self.popular_film)
        elem.click()

    def click_new_film(self):
        elem = self.wait_render(self.new_film)
        elem.click()