import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.menus_page import MenusPage
@pytest.fixture(scope="function")
def login(setup):
    """Login before running test cases"""
    driver = setup
    wait = WebDriverWait(driver,20)

    #Perform login
    wait.until(EC.visibility_of_element_located((By.NAME,"username"))).send_keys("Admin")
    wait.until(EC.visibility_of_element_located((By.NAME,"password"))).send_keys("admin123")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click()
    print("\nSuccessfully logged in")
    return driver

@pytest.mark.parametrize("menu_name",["Admin","PIM","Leave","Time","Recruitment","My Info","Performance","Dashboard"])
def test_menu_visibility(login,menu_name):
    """Test if menus are visible after login"""
    driver = login
    menu_page = MenusPage(driver)
    try:

        assert menu_page.is_menu_visible(menu_name),f"{menu_name} menu is not visible!"
        print(f"{menu_name} menu is visible")
    except Exception as e:
        print(f"visibility test failed for {menu_name}:{e}")

@pytest.mark.parametrize("menu_name",["Admin","PIM","Leave","Time","Recruitment","My Info","Performance","Dashboard"])
def test_menu_clickability(login,menu_name):
    """Test if menus are clickble after login"""
    driver = login
    menu_page = MenusPage(driver)
    try:
        menu_page.click_menu(menu_name)
        print(f"{menu_name} menu is clickable.")
    except Exception as e:
        print(f"clickability test failed for {menu_name} : {e}")

