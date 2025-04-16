#  MINI-PROJECT-02: OrangeHRM Automation Framework

##  Project Title
**Automated Testing for OrangeHRM Demo Web Application using Python Selenium, Pytest, and Page Object Model (POM)**

## Project URL
 [OrangeHRM Demo Site](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

---

## 🎯 Test Objective

This project aims to build a robust **Python Selenium automation framework** for validating the functionality of the **OrangeHRM demo CRM web application**. It simulates user actions, verifies results with assertions, and generates automated reports.

The framework includes:
- **Data-Driven Testing Framework (DDTF)** using Excel
- **Page Object Model (POM)** with **OOP principles**
- **Explicit Waits** for synchronization
- **Pytest-based HTML reporting**
- Positive and Negative test coverage
- **Keyword Driven + Hybrid Testing** style

---

##  Tools & Technologies

| Technology      | Description                                     |
|----------------|-------------------------------------------------|
| Python          | Programming Language                            |
| Selenium        | Web automation                                  |
| Pytest          | Testing Framework                               |
| POM             | Page Object Model for test structure            |
| DDT             | Data-Driven Testing via Excel                   |
| OpenPyXL        | Excel file interaction                          |
| HTML Report     | Pytest HTML plugin                              |
| Explicit Wait   | WebDriverWait + Expected Conditions             |
---
## Test Case ID	Description
TC-01	 Data-Driven Login Test (Positive/Negative) from Excel and verify using Cookies.
TC-02	 Verify Home URL is accessible.
TC-03	 Validate visibility of username & password input fields.
TC-04	 Post-login menu options visibility and clickability check (Admin, PIM, Leave, etc).
TC-05	 Create new user and validate login for the new user.
TC-06	 Verify new user record in Admin user list.

#POM Structure
capstoneproject/
│
├── Pages/
│   ├── __init__.py
│   ├── base_page.py               # Common reusable actions 
│   ├── menus_page.py              # Top/Side menus
│   ├── home_page_url.py           # Home/dashboard page 
│   ├── new_user_page.py           # Page for creating a new user
│   ├── exist_user_page.py         # Page for checking existing users
│   └── visible_page.py            # For visibility related actions/pages
│
├── Tests/
│   ├── test_home_url              # TC-02
│   ├── test_base.py               # Driver initialization fixture
│   ├── test_main.py               # Login test cases   #TC-01
│   ├── test_new_user.py           # Test for creating new user  #TC-05
│   ├── test_exist_user.py         # Test for verifying created user   #TC-06
│   ├── test_menus.py              # Test navigation and menu     #TC-04
│   └── test_visible.py            # Visibility tests   #TC-03	 
│
├── utils/
│   ├── __init__.py
│   ├── locators.py                # Store element locators (optional)
│   ├── excel_functions.py         # Excel utility functions
│   ├── file.py                    # File handling utilities
│   └── common.py                  # Common helper functions
│
├── test_data/
│   ├── test_case1.xlsx
│   
reports/
├── report1.html
├── report-2.html
├── report-3.html
├── report-4.html
├── report-5.html
└── report-6.html
├── conftest.py                    # Global fixtures

