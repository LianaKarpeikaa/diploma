import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.popups import Popup
from pages.filter_catalog_view import FilterCatalogView
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.onliner.by/')
    yield driver


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


@pytest.fixture(autouse=True)
def product_page(driver):
    yield ProductPage(driver)


@pytest.fixture(autouse=True)
def cart_page(driver):
    yield CartPage(driver)


@pytest.fixture(autouse=True)
def checkout_page(driver):
    yield CheckoutPage(driver)


