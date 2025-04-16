from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenusPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)

    def get_menu_element(self,menu_name):
        menu_xpath = f"//span[text()='{menu_name}']"
        return self.wait.until(EC.presence_of_element_located((By.XPATH, menu_xpath)))
    def is_menu_visible(self,menu_name):
        menu_element = self.get_menu_element(menu_name)
        return menu_element.is_displayed()
    def click_menu(self,menu_name):
        menu_xpath = f"//span[text()='{menu_name}']"
        menu_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, menu_xpath)))
        menu_element.click()
