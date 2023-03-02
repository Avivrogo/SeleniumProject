from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from AOS_Home_Page_Class import PS_Home_Page, Sign_in_pop_up, Register


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

homepage = PS_Home_Page(driver)
sign_in_pop_up = Sign_in_pop_up(driver)
newuser = Register(driver)
sleep(3)
homepage.account_icon().click()
sleep(3)
newuser.newaccount_Button().click()
sleep(3)
newuser.new_username_input('eyaltest12')
sleep(1)
newuser.new_email_input('ewasds@gmail.com')
sleep(1)
newuser.new_password_input('Eyal12345')
sleep(1)
newuser.new_cpassword_input('Eyal12345')
sleep(1)
newuser.new_lname_input('eyal')
sleep(1)
newuser.new_fname_input('berko')
sleep(1)
newuser.new_phone_input('0524235798')
sleep(1)
newuser.new_country_input('Israel')
sleep(1)
newuser.new_state_input('Kirya')
sleep(1)
newuser.new_address_input('Mavo Lulav, 9')
sleep(1)
newuser.new_city_input('Yahud')
sleep(1)
newuser.new_postal_input('54254')
sleep(1)
newuser.check_agree().click()
sleep(1)
newuser.Register_Button().click()
sleep(20)







