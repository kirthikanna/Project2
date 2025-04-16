import pytest
from Pages.new_user_page import NewUserPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_create_newuser(login):
    driver = login
    page = NewUserPage(driver)

    print("Navigating to Add User Form")
    page.go_to_add_user_form()

    print("Selecting User Role")
    page.select_user_role()

    print("Selecting Employee")
    page.select_employee('James Williams David')

    print("Selecting Status")
    page.select_status('Enabled')

    print("Filling username and password")
    page.fill_credentials()

    print("Saving the new user")
    page.click_save()

    print("Verifying user creation")
    assert page.verify_user_created()
    print("\n New User 'TestUser04' created successfully.")

def test_new_user_login(setup):
    driver = setup
    wait = WebDriverWait(driver,20)
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("TestUser04")
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("Test@123")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    print("\nSuccessfully logged in with new user.")

