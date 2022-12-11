import allure

from base.base_class import Base
from utilities.logger import Logger


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators



    # Getters


    # Actions



    # Methods
    """Метод получения URL и скриншота страницы"""

    def finish(self):
        with allure.step("Finish"):
            Logger.add_start_step(method="finish")
            self.get_current_url()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="finish")

