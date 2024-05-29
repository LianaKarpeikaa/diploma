from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from locators.catalog_page_locators import (BN_CATALOG_ELECTRONIC_ITEM, BN_CATALOG_AUDIO_ITEM,
                                            BN_CATALOG_VINYL_TURNTABLE_ITEM, LINK_VINYL_TURNTABLE_ITEM)


class CatalogPage(BasePage):

    @property
    def catalog_electronic_item(self):
        return self.wait_when_the_element_to_be_visible(BN_CATALOG_ELECTRONIC_ITEM)

    @property
    def catalog_audio_item(self):
        return self.wait_when_the_element_to_be_visible(BN_CATALOG_AUDIO_ITEM)

    @property
    def catalog_vinyl_turntable_item(self):
        return self.wait_when_the_element_to_be_visible(BN_CATALOG_VINYL_TURNTABLE_ITEM)

    @property
    def vinyl_turntable_item(self):
        return self.wait_when_the_element_to_be_clickable(LINK_VINYL_TURNTABLE_ITEM)

    def click_on_catalog_electronic_item(self):
        self.catalog_electronic_item.click()

    def go_to_vinyl_turntable_page(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.catalog_audio_item).perform()
        action.move_to_element(self.catalog_vinyl_turntable_item).perform()
        action.click().perform()

    def scroll_to_vinyl_turntable_item(self):
        self.scroll_to_element(LINK_VINYL_TURNTABLE_ITEM)

    def click_on_vinyl_turntable_item(self):
        self.scroll_to_vinyl_turntable_item()
        button = self.vinyl_turntable_item
        self.driver.execute_script("arguments[0].click();", button)


