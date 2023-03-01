from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from AOS_Home_Page_Class import PS_Home_Page, Sign_in_pop_up


service_chrome = Service(r"C:\selenium1\chromedriver.exe")

# Create a Chrome browser object
driver = webdriver.Chrome(service=service_chrome)

# Go to the URL
driver.get("https://www.advantageonlineshopping.com")

# Maximize the window
driver.maximize_window()

# In case an element is not found on the page, will try again for 10 seconds
# before we get an error message
driver.implicitly_wait(10)

sleep(6)

homepage = PS_Home_Page(driver)
sign_in_pop_up = Sign_in_pop_up(driver)
homepage.account_icon().click()
sleep(2)
sign_in_pop_up.type_username_field("eyal462")
sleep(2)
sign_in_pop_up.type_password_field("Eyal12345")
sleep(2)
sign_in_pop_up.sign_in_button().click()
sleep(2)









