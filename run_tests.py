# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest

def expected_true():
    return True

class TestSimple(unittest.TestCase):

    def test_expected_true(self):
        self.assertEqual(expected_true(), True)
    
    def test_selenium_fake(self):
        driver = webdriver.Chrome()
        driver.get("http://www.python.org")
        assert "Pythonnnnn" in driver.title

if __name__ == '__main__':
    unittest.main()
