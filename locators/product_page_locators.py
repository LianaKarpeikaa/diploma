from selenium.webdriver.common.by import By

BN_ADD_TO_CART = By.XPATH, (
    '//*[contains(text(), "В корзину")]')
BN_CART = By.XPATH, '//*[@href="https://cart.onliner.by"][@class="auth-bar__item auth-bar__item--cart"]'
