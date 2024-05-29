from selenium.webdriver.common.by import By

BN_CATALOG_ELECTRONIC_ITEM = By.XPATH, ('//*[@src="https://imgproxy.onliner.by'
                                        '/Z_M8tp4JouZs9YIAycsMQMVUM0yCPWEl1mJHVp8k8_U/w:160/h:160/f:png'
                                        '/aHR0cHM6Ly9nYy5v/bmxpbmVyLmJ5L2lt/YWdlcy9jYXRhbG9n/L25hdmlnYXRpb24v'
                                        '/Y2F0ZWdvcmllcy9l/bGVrdHJvbmlrYS5w/bmc"]')
BN_CATALOG_AUDIO_ITEM = By.XPATH, '//*[contains(text(), "Аудиотехника")]'
BN_CATALOG_VINYL_TURNTABLE_ITEM = By.XPATH, '//*[@href="https://catalog.onliner.by/turntable"]'
LINK_VINYL_TURNTABLE_ITEM = By.XPATH, '//*[contains(text(), "AT-LP140XP-BK")]'
CATALOG_HEADER = By.XPATH, '//h1[@class="catalog-navigation__title"]'