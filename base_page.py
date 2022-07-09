from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1,
                                  ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                      StaleElementReferenceException])

    def get_element_by_name(self, locator):
        return self.wait.until(EC.element_to_be_clickable((By.NAME, locator)))

    def get_element_by_class(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, locator)))
            # return self.driver.find_element(By.CLASS_NAME, locator)
        except UnexpectedAlertPresentException:
            return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, locator)))
            # return self.driver.find_element(By.CLASS_NAME, locator)

    def get_elements_by_class(self, locator):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, locator)))
        return self.driver.find_elements(By.CLASS_NAME, locator)

    def wait_item_disappear(self, locator):
        return self.wait.until_not(EC.visibility_of_all_elements_located((By.CLASS_NAME, locator)))

    def wait_for_text_to_appear(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, locator), text))
