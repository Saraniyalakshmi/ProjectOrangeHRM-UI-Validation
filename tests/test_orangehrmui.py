import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from orangehrm.orangehrmui import OrangeHRMUI

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def orangehrmui(driver):
    return OrangeHRMUI(driver)

def test_login(orangehrmui):
    orangehrmui.login("Admin", "admin123")

def test_navigate_to_admin_page(orangehrmui):
     result = orangehrmui.navigate_to_admin_page();
     assert "OrangeHRM" in result

def test_validate_options(orangehrmui):
    options = [
        ("User Management", "//span[text()='User Management ']"),
        ("Job", "//span[text()='Job ']"),
        ("Organization", "//span[text()='Organization ']"),
        ("Qualifications", "//span[text()='Qualifications ']"),
        ("Configuration", "//span[text()='Configuration ']"),
        ("Corporate Branding", "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]"),
        ("Nationalities", "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]")
    ]
    orangehrmui.validate_options(options)


def test_menu_options(orangehrmui):
    menu_options = [
        ("Admin", "//span[text()='Admin']"),
        ("PIM", "//span[text()='PIM']"),
        ("Leave", "//span[text()='Leave']"),
        ("Time", "//span[text()='Time']"),
        ("Recruitment", "//span[text()='Recruitment']"),
        ("My Info", "//span[text()='My Info']"),
        ("Performance", "//span[text()='Performance']"),
        ("Dashboard", "//span[text()='Dashboard']"),
        ("Directory", "//span[text()='Directory']"),
        ("Maintenance", "//span[text()='Maintenance']"),
        ("Buzz", "//span[text()='Buzz']")
    ]
    orangehrmui.validate_options(menu_options)

def test_forgot_password(orangehrmui):
    orangehrmui.logout()
    orangehrmui.click_forgot_password()
    orangehrmui.enter_username_for_reset("Admin")  # Replace "Admin" with the desired username
    orangehrmui.click_reset_password_button()
