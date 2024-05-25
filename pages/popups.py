from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.popups_locators import (PRIVACY_CONSENT_DIALOG, BN_AGREE, CATALOG_FORM_POPOVER,
                                      BN_ACCEPT_CATALOG_FORM_POPOVER)


class Popup(BasePage):

    @property
    def privacy_consent_dialog(self):
        try:
            self.wait_when_the_element_to_be_visible(PRIVACY_CONSENT_DIALOG)
            return True
        except TimeoutException:
            return False

    @property
    def agree_button(self):
        return self.wait_when_the_element_to_be_visible(BN_AGREE)

    @property
    def catalog_form_prover(self):
        try:
            self.wait_when_the_element_to_be_visible(CATALOG_FORM_POPOVER)
            return True
        except TimeoutException:
            return False

    @property
    def accept_button(self):
        return self.wait_when_the_element_to_be_visible(BN_ACCEPT_CATALOG_FORM_POPOVER)

    def click_on_agree_button(self):
        self.click(BN_AGREE)

    def click_on_accept_button(self):
        self.click(BN_ACCEPT_CATALOG_FORM_POPOVER)

    def check_privacy_consent_dialog(self):
        if self.privacy_consent_dialog:
            self.click_on_agree_button()

    def check_catalog_form_prover(self):
        if self.catalog_form_prover:
            self.click_on_accept_button()

