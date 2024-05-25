from typing import Tuple

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def wait_when_the_element_to_be_visible(self, locator: Tuple[str, str], timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_when_the_element_to_be_clickable(self, locator: Tuple[str, str], timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click(self, locator: Tuple[str, str], timeout: int = 5):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def scroll_to_element(self, locator: Tuple[str, str], timeout: int = 10):
        element = self.wait_when_the_element_to_be_visible(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
