from tests.BaseTest import BaseTest
from tests.pages.PromotionPage import PromotionPage


class PromotionTest(BaseTest):
    def setUp(self):
        super(PromotionTest, self).setUp()
        self.login()
        self.promotion_page = PromotionPage(self.driver)
        self.promotion_page.open(31)

    def test_redirect_profile(self):
        self.promotion_page.wait_click(self.promotion_page.profile_btn)
        is_profile = self.promotion_page.wait_redirect('https://volchock.ru/profile')
        self.assertEqual(is_profile, True, 'Редирект в профиль не произошел')

    def test_redirect_promote(self):
        self.promotion_page.wait_click(self.promotion_page.promote_btn)
        self.promotion_page.wait_any_redirect('yoomoney')
        is_yoomoney = (len(list(filter(lambda x: x == 'yoomoney.ru', self.driver.current_url.split('/')))) > 0)
        self.assertEqual(is_yoomoney, True, 'Редирект в сторонний сервис не произошел')
