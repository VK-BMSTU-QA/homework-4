import unittest

from page_objects.login import LoginPage
from setup.default_setup import default_setup


class BaseLoginTest(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def setUp(self):
        default_setup(self)

    def tearDown(self):
        self.driver.close()
