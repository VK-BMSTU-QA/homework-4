from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

TIMEOUT = 100
CHECK_FREQ = 0.5


def has_element(driver, xpath):
    try:
        WebDriverWait(driver, TIMEOUT, CHECK_FREQ).until(lambda d: d.find_element(by=By.XPATH, value=xpath))
    except NoSuchElementException:
        return False
    return True


def element_attribute_not_to_include(locator, attribute_):
    """An expectation for checking if the given attribute is not included in the
    specified element.
    locator, attribute
    """

    def _predicate(driver):
        try:
            element_attribute = driver.find_element(*locator).get_attribute(attribute_)
            return element_attribute is None
        except InvalidSelectorException as e:
            raise e
        except StaleElementReferenceException:
            return False

    return _predicate
