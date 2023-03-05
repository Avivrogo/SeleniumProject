from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from AOS_Class import PS_Home_Page, Sign_in_pop_up, Register

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
sleep(2)
list = driver.find_elements(By.XPATH, "//div[@class='cell categoryRight']/ul/li")
list[1].click()
sleep(1)
product1 = driver.find_element(By.XPATH, "//img[@id='20']")








