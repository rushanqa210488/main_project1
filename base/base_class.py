import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method Get Current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url  " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good Value word")

    """Method Scrolling"""

    def scroll_window(self):
        self.driver.execute_script("window.scrollTo(0, 1400)")
        print("scroll ok")

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Рушан\\Desktop\\main_project1\\screen\\' + name_screenshot)

        print("Finish screenshot ")


