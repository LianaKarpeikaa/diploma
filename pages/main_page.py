from pages.base_page import BasePage
from locators.main_page_locators import BN_CATALOG


class MainPage(BasePage):

    @property
    def catalog_button(self):
        return self.wait_when_the_element_to_be_visible(BN_CATALOG)

    def click_on_catalog_button(self):
        self.catalog_button.click()

