import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class OrangeHRMUI:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    def login(self, username, password):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # self.driver.maximize_window()

        try:
            # Adding explicit waits
            username_field = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            username_field.send_keys(username)

            password_field = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
            password_field.send_keys(password)

            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            login_button.click()

            # Check for login success
            error_message = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]"))
            )
            print("Error Message:", error_message.text)
        except Exception as e:
            print("Login is successful")

    def navigate_to_admin_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        return self.driver.title

    def validate_options(self, options):
        print("\n *** Header Validation Results ***")
        for option_text, option_xpath in options:
            self.validate_option(option_text, option_xpath)

    def validate_option(self, option_text, option_xpath):
        try:
            option_element = self.find_element_wait(By.XPATH, option_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", option_element)
            self.find_element_wait(By.XPATH, option_xpath)
            print(f"{option_text} option is present")
        except Exception as e:
            print(f"{option_text} option is NOT present: {e}")

    def validate_menu_options(self, menu_options):
        print("\n *** Main menu validation results ***")
        for option_text, option_xpath in menu_options:
            self.validate_option(option_text, option_xpath)

    def click_forgot_password(self):
        try:
            forgot_password_link = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"))
            )
            forgot_password_link.click()
            print("Clicked on 'Forgot your password?' link")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def enter_username_for_reset(self, username):
        try:
            username_for_reset = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
            )
            username_for_reset.send_keys(username)
            print(f"Entered username '{username}' for password reset")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def click_reset_password_button(self):
        try:
            reset_password_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )
            reset_password_button.click()
            time.sleep(5)
            print("Clicked on 'Reset Password' button")
            print("Password reset process initiated successfully")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def find_element_wait(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))

    def close_browser(self):
        self.driver.quit()
        print("Browser closed successfully")

    def logout(self):
        try:
            profile_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//p[@class='oxd-userdropdown-name']"))
            )
            profile_icon.click()
            time.sleep(5)

            logout_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Logout']"))
            )
            logout_button.click()
            time.sleep(5)
            print("Logged out successfully")

        except Exception as e:
            print(f"Failed to log out: {e}")

