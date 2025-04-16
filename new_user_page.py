import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewUserPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)

    def go_to_add_user_form(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//span[text()="Admin"]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[text()=" Add "]'))).click()

    def select_user_role(self, role='Admin'):
        user_role_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'oxd-select-text-input')])[1]")))
        user_role_dropdown.click()
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@role='listbox']//span[text()='{role}']"))).click()

    def select_employee(self, name='James Williams David'):
        employee_name = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
        employee_name.send_keys(name)
        time.sleep(10)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']")))
        employee_name_suggestion =self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']//span[contains(text(),'{name}')]")))
        employee_name_suggestion.click()

    def select_status(self, status='Enabled'):
        status_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'oxd-select-text-input')])[2]")))
        status_dropdown.click()
        time.sleep(2)
        enabled_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='listbox']//span[text()='{status}']")))
        enabled_option.click()

    def fill_credentials(self):
        user_name = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")))
        user_name.send_keys("TestUser04")
        password =self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='password'])[1]")))
        password.send_keys("Test@123")
        confirm_password = self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='password'])[2]")))
        confirm_password.send_keys("Test@123")
    def click_save(self):
        submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Save ']")))
        submit.click()
    def verify_user_created(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div[text()='TestUser04']")))
        return True