from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VisiblePage:
    def __init__(self,driver):
        self.driver = driver
        self.username_locator = (By.NAME,"username")
        self.password_locator = (By.NAME,"password")

    def is_username_visible(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.username_locator)).is_displayed()

    def is_password_visiible(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.password_locator)).is_displayed()