from pages.base_page import BasePage
from locators.checkout_page_locators import HEADER_CHECKOUT, PRODUCT_NAME
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class CheckoutPage(BasePage):

    @property
    def get_title(self):
        self.wait_when_the_element_to_be_visible(HEADER_CHECKOUT)
        title = self.driver.find_element(*HEADER_CHECKOUT)
        return title.text

    @property
    def get_title_of_product(self):
        self.wait_when_the_element_to_be_visible(PRODUCT_NAME, timeout=20)
        title = self.driver.find_element(*PRODUCT_NAME)
        return title.text






