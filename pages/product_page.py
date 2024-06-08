from pages.base_page import BasePage
from locators.product_page_locators import BN_ADD_TO_CART, BN_CART


class ProductPage(BasePage):

    @property
    def add_to_cart_button(self):
        return self.wait_when_the_element_to_be_visible(BN_ADD_TO_CART)

    @property
    def cart_button(self):
        return self.wait_when_the_element_to_be_visible(BN_CART)

    def click_on_add_to_cart_button(self):
        self.add_to_cart_button.click()

    def click_on_cart_button(self):
        self.cart_button.click()


