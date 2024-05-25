import pytest
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.popups import Popup
from pages.filter_catalog_view import FilterCatalogView


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def catalog_page(driver):
    yield CatalogPage(driver)


@pytest.fixture(autouse=True)
def popup(driver):
    yield Popup(driver)


@pytest.fixture(autouse=True)
def filter_catalog_view(driver):
    yield FilterCatalogView(driver)


class TestVinylTurntable:

    def test_purchase_flow_of_vinyl_turntable(self, main_page, catalog_page, popup, filter_catalog_view):
        popup.check_privacy_consent_dialog()
        main_page.click_on_catalog_button()
        popup.check_privacy_consent_dialog()
        catalog_page.click_on_catalog_electronic_item()
        catalog_page.go_to_vinyl_turntable_page()
        popup.check_catalog_form_prover()
        filter_catalog_view.select_in_stock_checkbox()
        filter_catalog_view.select_DJ_vinyl_turntable_checkbox()
        catalog_page.click_on_vinyl_turntable_item()





