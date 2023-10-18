from selenium import webdriver


class BasePage:
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    def __int__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title

    def take_screenshot(self):
        return self.driver.save_screenshot(self.__name__)
