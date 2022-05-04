from selenium.webdriver.common.by import By

from Base.BaseComponent import Component
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait


class SearchBar(Component):
    SEARCHBAR = '//input[@class="topbar__search-input"]'

    def click(self):
        bar = WebDriverWait(self.driver, 10, 0.1).until(lambda d: d.find_element(by=By.XPATH, value=self.SEARCHBAR))
        bar.click()
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: len(d.find_element(by=By.XPATH, value=MainLayout.LAY_CHILDREN)) == 0
        )

    def query(self, query):
        input = self.driver.find_element(by=By.XPATH, value=self.SEARCHBAR)
        input.clear()
        # Хак, потому что есть дебаунс и он срабатывает только на физ. нажатие кнопки
        input.send_keys(" ")
        input.send_keys(Keys.BACKSPACE)
        WebDriverWait(self.driver, 10, 0, 1).until(
            lambda d: len(d.find_element(by=By.XPATH, value=MainLayout.LAY_CHILDREN)) == 0
        )
        input.send_keys(query)
        WebDriverWait(self.driver, 10, 0, 1).until(
            lambda d: len(d.find_element(by=By.XPATH, value=MainLayout.LAY_CHILDREN)) != 0
        )


class MainLayout(Component):
    LAY = '//div[@class="main-layout__content"]'
    LAY_CHILDREN = LAY + "/*"
    NOT_FOUND = '//div[@class="search__content__not-found"]'

    def has_no_content(self):
        return len(self.driver.find_element(by=By.XPATH, value=self.LAY_CHILDREN)) == 0

    def not_found(self):
        return len(self.driver.find_element(by=By.XPATH, value=self.NOT_FOUND)) == 1
