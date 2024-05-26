from selenium.webdriver.common.by import By

BN_ADD_TO_CART = By.XPATH, (
    '//*[@class="button-style button-style_base-alter button-style_primary product-aside__button '
    'product-aside__button_narrow product-aside__button_cart button-style_expletive"]['
    '@data-shop-id="1113"]')
BN_CART = By.XPATH, '//*[@href="https://cart.onliner.by"][@class="auth-bar__item auth-bar__item--cart"]'
