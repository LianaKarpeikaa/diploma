from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.filter_catalog_view_locators import CH_BOX_IN_STOCK, CH_BOX_DJ_VINYL_TURNTABLE


class FilterCatalogView(BasePage):

    @property
    def filter_in_stock_checkbox(self):
        return self.wait_when_the_element_to_be_clickable(CH_BOX_IN_STOCK)

    @property
    def filter_DJ_vinyl_turntable_checkbox(self):
        return self.wait_when_the_element_to_be_clickable(CH_BOX_DJ_VINYL_TURNTABLE)

    def scroll_to_in_stock_checkbox(self):
        self.scroll_to_element(CH_BOX_IN_STOCK)

    def scroll_to_DJ_vinyl_turntable_checkbox(self):
        self.scroll_to_element(CH_BOX_DJ_VINYL_TURNTABLE)

    def select_in_stock_checkbox(self):
        self.scroll_to_in_stock_checkbox()
        checkbox = self.filter_in_stock_checkbox
        self.driver.execute_script("arguments[0].click();", checkbox)

    def select_DJ_vinyl_turntable_checkbox(self):
        self.scroll_to_DJ_vinyl_turntable_checkbox()
        checkbox = self.filter_DJ_vinyl_turntable_checkbox
        self.driver.execute_script("arguments[0].click();", checkbox)



