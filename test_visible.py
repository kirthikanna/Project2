import pytest
from Pages.visible_page import VisiblePage

def test_visiblity(setup):
    """Test to check if username and password fields are visible"""

    driver = setup
    page = VisiblePage(driver)

    print("\nChecking if username and password fields are visible...")  # Print message


    #Assertions
    assert page.is_username_visible(),"username field is not visible!"
    assert page.is_password_visiible(),"password field is not visible!"
    print("\n✅ Test Passed: Username and password fields are visible.")  # Print message
