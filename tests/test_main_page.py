import allure
import pytest


class TestMainPage:
    @pytest.mark.regression
    @allure.id("2")
    @allure.severity(allure.severity_level.MINOR)
    def test_catalog_button(self, main_page):
        button = main_page.catalog_button
        assert "Каталог" == button.text

    @pytest.mark.regression
    @allure.id("3")
    @allure.severity(allure.severity_level.NORMAL)
    def test_click_on_catalog_button(self, main_page, catalog_page):
        main_page.click_on_catalog_button()
        assert "Каталог" == catalog_page.catalog_header

    @pytest.mark.regression
    @allure.id("4")
    @allure.severity(allure.severity_level.MINOR)
    def test_news_button(self, main_page):
        news_button = main_page.news_button
        assert "Новости" == news_button.text

    @pytest.mark.regression
    @allure.id("5")
    @allure.severity(allure.severity_level.MINOR)
    def test_car_hoarding_button(self, main_page):
        button = main_page.car_hoarding_button
        assert "Автобарахолка" == button.text

    @pytest.mark.regression
    @allure.id("6")
    @allure.severity(allure.severity_level.MINOR)
    def test_houses_and_flats_button(self, main_page):
        button = main_page.house_and_flats_button
        assert "Дома и квартиры" == button.text

    @allure.id("7")
    @allure.severity(allure.severity_level.MINOR)
    def test_services_button(self, main_page):
        button = main_page.services_button
        assert "Услуги" == button.text

    @pytest.mark.regression
    @allure.id("8")
    @allure.severity(allure.severity_level.MINOR)
    def test_baraholka_button(self, main_page):
        button = main_page.baraholka_button
        assert "Барахолка" == button.text

    @pytest.mark.regression
    @allure.id("9")
    @allure.severity(allure.severity_level.MINOR)
    def test_forum_button(self, main_page):
        button = main_page.forum_button
        assert "Форум" == button.text
