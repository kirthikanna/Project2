import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def login(setup): #Setup comes from conftest
    """Login before running test cases"""
    driver = setup
    wait = WebDriverWait(driver,20)

    #Perform login
    wait.until(EC.visibility_of_element_located((By.NAME,"username"))).send_keys("Admin")
    wait.until(EC.visibility_of_element_located((By.NAME,"password"))).send_keys("admin123")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()
    print("\nSuccessfully logged in")
        #wait for the dashboard to load
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"body")))
    yield driver
    driver.quit()