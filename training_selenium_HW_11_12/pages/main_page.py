from selenium.webdriver.common.by import By
from training_selenium_HW_11_12.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sign_up_button = lambda: self._driver.find_element(By.XPATH, "//button[text()='Sign up']")
       