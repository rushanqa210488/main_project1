import time
import allure
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.buy_product_page import Buy_product_page
from pages.finish_page import Finish_page
from pages.main_page import Main_page
from pages.select_poduct_page import Select_product_page


# @pytest.mark.run(order=2)
@allure.description("Test Select Product")
def test_select_product(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(executable_path='C:\\Users\\Рушан\\PycharmProjects\\resource\\chromedriver.exe',
                              chrome_options=options)

    print("Start Test")

    mp = Main_page(driver)
    mp.opening_homepage()
    sp = Select_product_page(driver)
    sp.select_products()
    bp = Buy_product_page(driver)
    bp.buy_product()
    f = Finish_page(driver)
    f.finish()

    print("Finish Test ")

    time.sleep(5)


# @pytest.mark.run(order=1)
# def test_select_product_1(set_group):
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#
#     driver = webdriver.Chrome(executable_path='C:\\Users\\Рушан\\PycharmProjects\\resource\\chromedriver.exe',
#                               chrome_options=options)
#
#     print("Start Test 1")
#
#     mp = Main_page(driver)
#     mp.opening_homepage()
#     sp = Select_product_page(driver)
#     sp.select_products()
#     bp = Buy_product_page(driver)
#     bp.buy_product1()
#     f = Finish_page(driver)
#     f.finish()
#
#     print("Finish Test1 ")
#
#     time.sleep(5)
