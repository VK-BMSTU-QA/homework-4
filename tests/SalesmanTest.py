from tests.BaseTest import BaseTest
from tests.pages.SalesmanPage import SalesmanPage


class SalesmanTest(BaseTest):
    def setUp(self):
        super(SalesmanTest, self).setUp()
        self.login()
        self.salesman_page = SalesmanPage(self.driver)
        self.salesman_page.open(2)

    def test_advert_redirect(self):
        self.salesman_page.wait_click(self.salesman_page.card)
        self.salesman_page.wait_any_redirect('ad')
        self.assertEqual(self.driver.current_url.split('/')[3], 
                        'ad',
                        'Названия страниц не совпадают')

    def test_rating_highlight(self):
        self.salesman_page.hover(self.salesman_page.star)
        star = self.salesman_page.wait_render(self.salesman_page.star)
        is_active = "star_active" in star.get_attribute("class")
        self.assertEqual(is_active, True, 'Элементы рейтинга не становятся активными при наведении')
