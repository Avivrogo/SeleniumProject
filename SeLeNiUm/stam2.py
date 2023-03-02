from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from AOS_Class import PS_Home_Page, Sign_in_pop_up

service_chrome = Service(r'C:\selenium\chromedriver.exe')

driver = webdriver.Chrome(service=service_chrome)

# Go to the URL
driver.get("https://www.advantageonlineshopping.com")

# Maximize window
driver.maximize_window()

# Timeout
driver.implicitly_wait(10)
sleep(5)

driver.find_element(By.ID, 'menuUserLink').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("eyal462")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("Eyal12345")
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'button[id="sign_in_btnundefined"]').click()
sleep(1)








