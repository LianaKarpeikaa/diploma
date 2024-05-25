from selenium.webdriver.common.by import By

PRIVACY_CONSENT_DIALOG = By.XPATH, '//div[@class="fc-dialog fc-choice-dialog"]'
BN_AGREE = By.XPATH, '//button[@class="fc-button fc-cta-consent fc-primary-button"]/p[@class="fc-button-label"]'
CATALOG_FORM_POPOVER = By.XPATH, '//*[@class="popover-style__container"]'
BN_ACCEPT_CATALOG_FORM_POPOVER = By.XPATH, ('//*[@class="button-style button-style_primary button-style_small-alter '
                                            'catalog-form__button"]')
