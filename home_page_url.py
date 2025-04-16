from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        # Locators
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.body_tag = (By.TAG_NAME, "body")

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.submit_button)).click()

    def is_dashboard_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.body_tag))
        return self.driver.current_url