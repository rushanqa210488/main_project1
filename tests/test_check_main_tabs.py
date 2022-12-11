import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.finish_page import Finish_page
from pages.main_page import Main_page



@allure.description("Test Check Main Tabs")
def test_check_main_tabs(set_up, set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(executable_path='C:\\Users\\Рушан\\PycharmProjects\\resource\\chromedriver.exe',
                              chrome_options=options)

    print("Start Test")

    mp = Main_page(driver)
    mp.opening_homepage()
    mp.check_main_tabs()
    f = Finish_page(driver)
    f.finish()



    time.sleep(5)

