from selenium.webdriver.common.by import By

HEADER_CHECKOUT = By.XPATH, ('//*[@class="cart-form__title cart-form__title_base cart-form__title_nocondensed '
                             'cart-form__title_condensed-other"]')
PRODUCT_NAME = By.XPATH, ('//*[@class="cart-form__description cart-form__description_primary cart-form__description_base cart-form__description_condensed-complementary cart-form__description_nonadaptive"]//*[@class="cart-form__description-part cart-form__description-part_1"]')