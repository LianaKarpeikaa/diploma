from selenium.webdriver.common.by import By

BN_CATALOG = By.XPATH, '//a[@href="https://catalog.onliner.by"]/span[@class="b-main-navigation__text"]'
BN_NEWS = By.XPATH, '//a[@href="https://www.onliner.by"]/*[@class="b-main-navigation__text"]'
BN_CAR_HOARDING = By.XPATH, '//a[@href="https://ab.onliner.by"]/*[@class="b-main-navigation__text"]'
BN_HOUSES_AND_FLATS = By.XPATH, '//a[@href="https://r.onliner.by/pk"]/*[@class="b-main-navigation__text"]'
BN_SERVICES = By.XPATH, '//a[@href="https://s.onliner.by/tasks"]/*[@class="b-main-navigation__text"]'
BN_BARAHOLKA = By.XPATH, '//a[@href="https://baraholka.onliner.by/"]/*[@class="b-main-navigation__text"]'
BN_FORUM = By.XPATH, '//a[@href="https://forum.onliner.by/"]/*[@class="b-main-navigation__text"]'