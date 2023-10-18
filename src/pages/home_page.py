from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def __int__(self, driver):
        super().__init__(driver)

    def get_url(self, url):
        self.driver.get(url)

    def click_login_button(self):
        # login_button_xpath = "//span[normalize-space()='Log in']"
        login_button_css = "button[data-testid='homepage-login-button']"
        login_button = self.driver.find_element(by=By.CSS_SELECTOR, value=login_button_css)
        login_button.click()

    def enter_email(self, email):
        email_field = self.driver.find_element(by=By.ID, value="email")
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(by=By.ID, value="current-password")
        password_field.send_keys(password)

    def click_second_login(self):
        second_login_css = "button[data-testid='loginoverlay-login-button']"
        sign_in_with_email = self.driver.find_element(by=By.CSS_SELECTOR, value=second_login_css)
        sign_in_with_email.click()

