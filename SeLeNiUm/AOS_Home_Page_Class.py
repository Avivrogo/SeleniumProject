from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Account details:
# username: eyal462
#password: Eyal12345

class PS_Home_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def site_logo(self):
        return self.driver.find_element(By.CLASS_NAME, 'logo')

    def account_icon(self):
        return self.driver.find_element(By.ID, 'menuUserLink')

    def speakers_link(self):
        return self.driver.find_element(By.ID, 'speakersImg')

    def tablets_link(self):
        return self.driver.find_element(By.ID, 'tabletsImg')

    def laptops_link(self):
        return self.driver.find_element(By.ID, 'laptopsImg')

    def headphones_link(self):
        return self.driver.find_element(By.ID, 'headphonesImg')

    def mice_link(self):
        return self.driver.find_element(By.ID, 'miceImg')




class Sign_in_pop_up:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def username_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='username']")

    def type_username_field(self, username: str):
        self.username_field().send_keys(username)

    def password_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    def type_password_field(self, password: str):
        self.password_field().send_keys(password)

    def sign_in_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'button[id="sign_in_btnundefined"]')

    def create_new_account_link(self):
        return self.driver.find_element(By.CLASS_NAME, 'create-new-account ng-scope')

    def forgot_password_link(self):
        return self.driver.find_element(By.CLASS_NAME, 'forgot-Passwowd ng-scope')

    def remember_me_checkbox(self):
        return self.driver.find_element(By.CLASS_NAME, 'remember_me')


class register_page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)