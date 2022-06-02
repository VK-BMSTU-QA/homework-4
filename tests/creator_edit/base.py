import unittest


from setup.default_setup import default_setup


class BaseCreatorEditTest(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None

    def setUp(self):
        default_setup(self)

    def tearDown(self):
        self.driver.close()
