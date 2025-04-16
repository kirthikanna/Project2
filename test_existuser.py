import time

import pytest

# def test_existuser(login):
#     driver = login
#     wait = WebDriverWait(driver, 10)
#     try:
#         # Click Admin menu
#         admin_menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Admin"]')))
#         admin_menu.click()
#
#         # wait for the users page to load
#         wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='System Users']")))
#
#         username_input = wait.until(
#             EC.element_to_be_clickable((By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]')))
#         username_input.send_keys("TestUser04")
#         time.sleep(2)
#
#         search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Search "]')))
#         search_button.click()
#         time.sleep(2)
#
#         # Wait for table to load and check if user apppears
#         user_rows = driver.find_elements(By.XPATH, '//div[@role="row"]')
#         user_found = False
#         for row in user_rows:
#             cells = row.find_elements(By.XPATH,"//div[@role='cell']")
#             if cells and cells[1].text.strip() == "TestUser04":
#                 user_found = True
#                 break
#
#         assert user_found, " User 'TestUser04' not found in the search results."
#         print("New user 'TestUser04' successfully found in the user list.")
#
#     except Exception as e:
#         pytest.fail(f" Test failed due to unexpected error: {str(e)}") #clearly marks the test as failed.shows error message in the pytest summary.
from Pages.existuser_page import ExistingUserPage

def test_existuser(login):
    driver = login
    exist_user_page = ExistingUserPage(driver)

    try:
        exist_user_page.navigate_to_admin_menu()
        exist_user_page.wait_for_system_users_page()
        exist_user_page.search_user("TestUser04")

        assert exist_user_page.verify_user_in_list("TestUser04"), "User 'TestUser04' not found in the search results."
        print("New user 'TestUser04' successfully found in the user list.")
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected error: {str(e)}")










