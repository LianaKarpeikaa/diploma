from pages.base_page import BasePage
from locators.cart_page_locators import BN_CHECKOUT


class CartPage(BasePage):

    @property
    def checkout_button(self):
        return self.wait_when_the_element_to_be_visible(BN_CHECKOUT)

    def click_on_checkout_button(self):
        self.checkout_button.click()



