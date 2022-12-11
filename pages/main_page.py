import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):
    url = 'https://www.xn-----elcjb0blled5a.xn--p1ai/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    main_word = "//div[@class='sidebar_menu_ttl']"
    elements_by_otoplenie = "ul[class*=sidebar_menu]>li"

    # Getters

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.main_word)))

    def get_elements_by_otoplenie(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, self.elements_by_otoplenie)))

    # Actions

    # Methods
    """Метод проверки текста со страницы.  """

    def opening_homepage(self):
        with allure.step("Opening Homepage"):
            Logger.add_start_step(method="opening_homepage")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.assert_word(self.get_main_word(), 'КАТАЛОГ ТОВАРОВ')
            Logger.add_end_step(url=self.driver.current_url, method="opening_homepage")

    """Метод прохождения по основным вкладкам страницы."""

    def check_main_tabs(self):
        with allure.step("Check Main Tabs"):
            Logger.add_start_step(method="check_main_tabs")
            for indx in range(14):
                self.get_elements_by_otoplenie()[indx].click()
                time.sleep(2)
                self.driver.back()
                self.driver.execute_script("window.scrollTo(0, 400)")
            print("Check main tabs")
            self.get_current_url()
            Logger.add_end_step(url=self.driver.current_url, method="check_main_tabs")
