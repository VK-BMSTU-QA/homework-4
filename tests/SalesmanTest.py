from tests.BaseTest import BaseTest
from tests.pages.SalesmanPage import SalesmanPage


class SalesmanTest(BaseTest):
    testing_salesman_id = 2
    def setUp(self):
        super(SalesmanTest, self).setUp()
        self.login()
        self.salesman_page = SalesmanPage(self.driver)
        self.salesman_page.open(self.testing_salesman_id)

    def test_adverts_are_displayed(self):
        is_grid_displayed = self.salesman_page.grid_is_not_empty()
        self.assertTrue(is_grid_displayed, "У продавца не отображается грид объявлений в профиле")

    def test_rating_highlight(self):
        self.salesman_page.hover(self.salesman_page.star)
        star = self.salesman_page.wait_render(self.salesman_page.star)
        is_active = "star_active" in star.get_attribute("class")
        self.assertTrue(is_active, 'Элементы рейтинга не становятся активными')
