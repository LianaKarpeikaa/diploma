import pytest


class TestMainPage:

    def test_catalog_button(self, main_page):
        button = main_page.catalog_button
        assert "Каталог" == button.text

    def test_click_on_catalog_button(self, main_page, catalog_page):
        main_page.click_on_catalog_button()
        assert "Каталог" == catalog_page.catalog_header

    def test_news_button(self, main_page):
        news_button = main_page.news_button
        assert "Новости" == news_button.text

    def test_car_hoarding_button(self, main_page):
        button = main_page.car_hoarding_button
        assert "Автобарахолка" == button.text

    def test_houses_and_flats_button(self, main_page):
        button = main_page.house_and_flats_button
        assert "Дома и квартиры" == button.text

    def test_services_button(self, main_page):
        button = main_page.services_button
        assert "Услуги" == button.text

    def test_baraholka_button(self, main_page):
        button = main_page.baraholka_button
        assert "Барахолка" == button.text

    def test_forum_button(self, main_page):
        button = main_page.forum_button
        assert "Форум" == button.text
