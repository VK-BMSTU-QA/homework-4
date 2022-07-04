from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1,
                                  ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException])

    def get_element_by_name(self, locator):
        return self.wait.until(EC.element_to_be_clickable((By.NAME, locator)))

    def get_element_by_class(self, locator):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, locator)))

    def get_element_seen_by_selector(self, locator):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))

    def get_element_by_id(self, locator):
        return self.wait.until(EC.element_to_be_clickable((By.ID, locator)))

    def get_element_by_css_selector(self, locator):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))

    def get_elements_by_css_selector(self, locator):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        return self.driver.find_elements_by_css_selector(locator)
    
    def get_elements_by_class(self, locator):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, locator)))
        # return self.driver.find_elements_by_class_name(locator)
        return self.driver.find_elements(By.CLASS_NAME, locator)

    def wait_item_disappear(self, locator):
        return self.wait.until_not(EC.visibility_of_all_elements_located((By.CLASS_NAME, locator)))

    def wait_item_appear(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, locator)))

    def wait_elements_disappear(self, locator):
        return self.wait.until_not(EC.element_to_be_clickable((By.CLASS_NAME, locator)))

    def wait_element_staleness(self, element):
        return self.wait.until(EC.staleness_of(element))

    def wait_product_invisibility(self, locator):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, locator)))
