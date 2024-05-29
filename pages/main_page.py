from pages.base_page import BasePage
from locators.main_page_locators import (BN_CATALOG, BN_NEWS, BN_CAR_HOARDING, BN_HOUSES_AND_FLATS, BN_SERVICES,
                                         BN_BARAHOLKA, BN_FORUM)


class MainPage(BasePage):

    @property
    def catalog_button(self):
        return self.wait_when_the_element_to_be_visible(BN_CATALOG)

    @property
    def news_button(self):
        return self.wait_when_the_element_to_be_visible(BN_NEWS)

    @property
    def car_hoarding_button(self):
        return self.wait_when_the_element_to_be_visible(BN_CAR_HOARDING)

    @property
    def house_and_flats_button(self):
        return self.wait_when_the_element_to_be_visible(BN_HOUSES_AND_FLATS)

    @property
    def services_button(self):
        return self.wait_when_the_element_to_be_visible(BN_SERVICES)

    @property
    def baraholka_button(self):
        return self.wait_when_the_element_to_be_visible(BN_BARAHOLKA)

    @property
    def forum_button(self):
        return self.wait_when_the_element_to_be_visible(BN_FORUM)

    def click_on_catalog_button(self):
        self.catalog_button.click()

    def click_on_news_button(self):
        self.news_button.click()

    def click_on_car_hoarding_button(self):
        self.car_hoarding_button.click()

    def click_house_and_flats_button(self):
        self.house_and_flats_button.click()

    def click_on_services_button(self):
        self.services_button.click()

    def click_on_baraholka_button_button(self):
        self.news_button.click()

    def click_on_forum_button(self):
        self.forum_button.click()

