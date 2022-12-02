

from base.base_class import Base


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
        self.get_current_url()
        self.get_screenshot()
