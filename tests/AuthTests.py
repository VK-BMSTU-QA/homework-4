from tests.BaseTest import BaseTest
from tests.pages.MainPage import MainPage


class SignUpTest(BaseTest):
    def setUp(self):
        # подготавливаем окружение, открываем страницу
        # переходим на страницу логина
        super(SignUpTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        #self.main_page.click_login()

    def tearDown(self):
        pass

    def test_log_empty_email(self):
        print("abcd")
        pass