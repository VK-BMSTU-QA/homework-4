from setup.default_setup import default_setup
from tests.login.base import BaseLoginTest


class LoginTest(BaseLoginTest):

    def __init__(self, methodName: str = ...):
        super(LoginTest, self).__init__(methodName)

    def setUp(self):
        super().setUp()
        default_setup(self)

    def tearDown(self):
        super().tearDown()

        self.driver.close()
