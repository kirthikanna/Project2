import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def setup():
    """Initialize the webdriver and return driver instance"""

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    print("\nBrowser opened and navigated to login page")
    yield driver
    driver.quit()
    print("\nBrowser closed")

@pytest.fixture(scope="function")
def login(setup):
    driver = setup
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("admin123")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    return driver
