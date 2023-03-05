from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from AOS_Class import Home_Page, Sign_in_pop_up, product_page, category_page

service_chrome = Service(r'C:\selenium\chromedriver.exe')

driver = webdriver.Chrome(service=service_chrome)

# Go to the URL
driver.get("https://www.advantageonlineshopping.com")

# Maximize window
driver.maximize_window()

# Timeout
driver.implicitly_wait(6)
sleep(5)

hp = Home_Page(driver)
pp = product_page(driver)
cp = category_page(driver)
si = Sign_in_pop_up(driver)

hp.account_icon().click()
sleep(1)
si.type_username_field("eyal462")
sleep(1)
si.type_password_field("Eyal12345")
sleep(1)
si.sign_in_button().click()

sleep(5)

site_username = driver.find_element(By.CSS_SELECTOR, '[id="menuUserLink"]>span').text
# prog_username = "eyal462"
if site_username == "eyal462":
    print("log in yes")
else:
    print("log in no")

# hp.speakers_link().click()
# sleep(2)
#
# cp.products_list()[3].click()
# sleep(3)
#
# pp.change_quantity(5)
# sleep(2)
#
# pp.add_to_cart_button().click()
# sleep(2)

hp.account_icon().click()
hp.account_options_list(3)


sleep(5)