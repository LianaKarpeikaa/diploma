from selenium.webdriver.common.by import By

CH_BOX_IN_STOCK = By.XPATH, '//*[@class="catalog-form__checkbox-text"]/*[contains(text(), "В наличии на складе")]'
CH_BOX_DJ_VINYL_TURNTABLE = By.XPATH, ('//*[@class="catalog-form__checkbox-text"]/*[contains(text(), "DJ виниловый '
                                       'проигрыватель")]')