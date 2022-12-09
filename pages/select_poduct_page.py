import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Select_product_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_category = "//a[@href='/catalog/smesitelnye-uzly-dlya-teplogo-pola-i-kollektornye-gruppy/']"
    radio_button = "//input[@id='arrFilter_22_934352770']"
    checkbox_1 = "//input[@id='arrFilter_45_2707236321']"
    button_filter = "//input[@id='set_filter']"

    # Getters

    def get_select_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.select_category)))

    def get_radio_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.radio_button)))

    def get_checkbox_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.checkbox_1)))

    def get_button_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.button_filter)))

    # Actions

    def click_select_category(self):
        self.get_select_category().click()
        print("Click select category")

    def click_radio_button(self):
        self.get_radio_button().click()
        print("Click radio button")

    def click_checkbox_1(self):
        self.get_checkbox_1().click()
        print("Click checkbox_1")

    def click_button_filter(self):
        self.get_button_filter().click()
        print("Click button filter")



    # Methods
    """Метод выбор товара с помощью фильтра. """

    def select_products(self):
        Logger.add_start_step(method="select_products")
        self.click_select_category()
        self.scroll_window()
        self.click_radio_button()
        self.click_checkbox_1()
        self.click_button_filter()
        self.get_current_url()
        Logger.add_end_step(url=self.driver.current_url, method="select_products")
