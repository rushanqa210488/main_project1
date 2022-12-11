import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Buy_product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_product = "//a[@class='cat_select_item'][2]"
    button_description = "//div[@id='bx_3966226736_16017']"
    button_cart = "//a[@class='blue_btn']"
    button_checkout = "//div[@class='bx_ordercart_order_pay_center']"

    button_description1 = "//div[@id='bx_3966226736_16019']"


    # Getters

    def get_select_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.select_product)))

    def get_button_description(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.button_description)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.button_cart)))


    def get_button_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.button_checkout)))


    def get_button_description1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, self.button_description1)))



    # Actions

    def click_select_product(self):
        self.get_select_product().click()
        print("Click select product")

    def click_button_description(self):
        self.get_button_description().click()
        print("Click button description")

    def click_button_description1(self):
        self.get_button_description1().click()
        print("Click button description1")

    def click_button_cart(self):
        self.get_button_cart().click()
        print("Click button cart")

    def click_button_checkout(self):
        self.get_button_checkout().click()
        print("Click button_checkout")



    # Methods

    """Метод выбора продукта 1 и переход в корзину"""

    def buy_product(self):
        with allure.step("Buy Product"):
            Logger.add_start_step(method="buy_product")
            self.click_select_product()
            self.click_button_description()
            self.click_button_cart()
            self.click_button_checkout()
            Logger.add_end_step(url=self.driver.current_url, method="buy_product")


    """Метод выбора продукта 2 и переход в корзину"""

    def buy_product1(self):
        Logger.add_start_step(method="buy_product1")
        self.click_select_product()
        self.click_button_description1()
        self.click_button_cart()
        self.click_button_checkout()
        Logger.add_end_step(url=self.driver.current_url, method="buy_product1")


