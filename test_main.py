import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from excel_functions import ExcelReader
from locators import WebLocators
from common import Data
import time
def test_login_cookies(setup):
    driver = setup
    print("Browser opened and navigated to login page")
# Read Excel Data
    excel_reader = ExcelReader(Data().EXCEL_FILE, Data().SHEET_NUMBER)
    rows = excel_reader.row_count()

    for row in range(2, rows + 1):
        username = excel_reader.read_data(row, column_number=6)
        password = excel_reader.read_data(row, column_number=7)
        login_success = False
        cookies = None
        try:
            #  Fresh driver for each user
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get(Data().URL)
            driver.maximize_window()

            # Login using username and password
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, WebLocators().USERNAME_INPUT_BOX))).send_keys(username)

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, WebLocators().PASSWORD_INPUT_BOX))).send_keys(password)

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, WebLocators().SUBMIT_BUTTON))).click()

            # Wait for successful login
            WebDriverWait(driver, 10).until(lambda a: Data().DASHBOARD_URL in a.current_url)

            print(f" SUCCESS: Login Successful for USERNAME={username} and PASSWORD={password}")
            excel_reader.write_data(row, 8, "TEST PASSED")

            # capture cookies after successful login
            login_success = True
            cookies = driver.get_cookies()
            print(f"captured cookies for {username}: {cookies}")

        except Exception as e:
            print(f"ERROR: Initial Login failed for USERNAME={username} - {str(e)}")
            excel_reader.write_data(row, 8, "TEST FAILED")
            continue  # Skip to next user if initial login fails
        finally:
            driver.quit()
    # If login was successful, start new session and reuse cookies
            # If login was successful, test cookie-based login
        if login_success and cookies:
            try:
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                driver.get(Data().URL)
                driver.maximize_window()

                # Need to be on the domain before adding cookies
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, WebLocators().USERNAME_INPUT_BOX))
                )

                # Delete all existing cookies first
                driver.delete_all_cookies()

                # Add the captured cookies one by one
                for cookie in cookies:
                    # Ensure the cookie domain matches (sometimes needs adjustment)
                    if 'opensource-demo.orangehrmlive.com' in cookie['domain']:
                        driver.add_cookie(cookie)

                # Refresh to apply cookies
                driver.refresh()
                time.sleep(2)  # Small wait for page to reload

                # Verify login via cookies
                WebDriverWait(driver, 10).until(lambda a: Data().DASHBOARD_URL in a.current_url)
                print(f"SUCCESS: Cookie login successful for {username}")
                excel_reader.write_data(row, 8, "COOKIE TEST PASSED")

                try:
                    print("Attempting logout...")
                    # Wait for user menu to be clickable
                    user_menu = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "oxd-userdropdown-tab")))
                    driver.execute_script("arguments[0].click();", user_menu)
                    time.sleep(1)  # Give time for dropdown to open

                    # Logout button using XPATH and visible text
                    logout_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, WebLocators().LOGOUT_BUTTON)))
                    logout_button.click()

                    WebDriverWait(driver, 10).until(EC.url_contains("/auth/login"))
                    print(f"Successfully logged out")

                except Exception as e:
                    print(f"Warning: Logout failed! Exception: {e}")


            except Exception as e:
                print(f"ERROR: Cookie login failed for {username} - {str(e)}")
                excel_reader.write_data(row, 8, "COOKIE TEST FAILED")

            finally:
                driver.quit()














