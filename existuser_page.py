import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExistingUserPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_admin_menu(self):
        admin_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Admin"]')))
        admin_menu.click()
        print("Clicked Admin menu")

    # wait for the users page to load
    def wait_for_system_users_page(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='System Users']")))
        print("System Users page loaded")

    def search_user(self, username):
        username_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]')))
        username_input.send_keys(username)
        time.sleep(2)
        print(f"Entered username: {username}")

        search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Search "]')))
        search_button.click()
        time.sleep(2)
        print("Clicked search button")

    def verify_user_in_list(self, username):
        user_rows = self.driver.find_elements(By.XPATH, '//div[@role="row"]')
        for row in user_rows:
            cells = row.find_elements(By.XPATH, "//div[@role='cell']")
            if cells and cells[1].text.strip() == username:
                print(f"User '{username}' found in the list")
                return True
        return False