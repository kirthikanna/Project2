import pytest
from Pages.home_page_url import HomePage


#Parameterizinig login credentials
@pytest.mark.parametrize("username,password",[("Admin","admin123")])

def test_home(setup,username,password):
    """ Verify whether the home URL is accessible"""
    driver = setup
    home = HomePage(driver)
    home.load()
    home.login(username, password)
    current_url = home.is_dashboard_loaded()
    #Assertion : Check if the current url matches the expected home url
    assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index", "Home URL is not working!"
    print("Home URL is working correctlyl!")

