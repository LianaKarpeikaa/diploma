from pages.base_page import BasePage
from locators.checkout_page_locators import HEADER_CHECKOUT


class CheckoutPage(BasePage):

    @property
    def get_title(self):
        self.wait_when_the_element_to_be_visible(HEADER_CHECKOUT)
        title = self.driver.find_element(*HEADER_CHECKOUT)
        return title.text






