import allure
import pytest


class TestVinylTurntable:
    @pytest.mark.smoke
    @allure.id("1")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Scenario 1: Buy Playstation 5")
    @allure.story("As a user, I want to buy a vinyl turntable")
    @allure.feature("[JIRA-1]Feature vinyl turntable")
    def test_purchase_flow_of_vinyl_turntable(self, main_page, catalog_page, popup, filter_catalog_view, product_page,
                                              cart_page, checkout_page):
        popup.check_privacy_consent_dialog()
        main_page.click_on_catalog_button()
        popup.check_privacy_consent_dialog()
        catalog_page.click_on_catalog_electronic_item()
        catalog_page.go_to_vinyl_turntable_page()
        popup.check_catalog_form_prover()
        filter_catalog_view.select_in_stock_checkbox()
        filter_catalog_view.select_DJ_vinyl_turntable_checkbox()
        catalog_page.click_on_vinyl_turntable_item()
        product_page.click_on_add_to_cart_button()
        product_page.click_on_cart_button()
        cart_page.click_on_checkout_button()
        assert "Оформление заказа" == checkout_page.get_title, \
            f"Expected header: 'Оформление заказа', Actual: {checkout_page.get_title}"
