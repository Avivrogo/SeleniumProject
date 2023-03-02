from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from AOS_Class import Home_Page, product_page, category_page, Sign_in_pop_up

class Test_AOS(unittest.TestCase):
    def setUp(self):
        self.service = service_chrome = Service(r"C:\selenium1\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)
        self.wait = WebDriverWait(self.driver, 10)
        self.action_chains = ActionChains(self.driver)
        self.driver.get("https://www.advantageonlineshopping.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.hp = Home_Page(self.driver)
        self.pp = product_page(self.driver)
        self.cp = category_page(self.driver)
        self.si = Sign_in_pop_up(self.driver)

    def testcase1(self):
        # choose quantities for test
        quantity1 = 4
        quantity2 = 2
        # wait for category to be clickable than click on speakers
        self.wait.until(EC.element_to_be_clickable((self.hp.speakers_link())))
        self.hp.speakers_link().click()
        sleep(4)
        self.cp.select_product_click(3)
        sleep(2)
        self.pp.change_quantity(str(quantity1))
        sleep(2)
        self.pp.add_to_cart_button().click()
        sleep(2)
        self.driver.back()
        sleep(3)
        self.cp.select_product_click(4)
        sleep(3)
        self.pp.change_quantity(str(quantity2))
        sleep(2)
        self.pp.add_to_cart_button().click()
        sleep(1)
        cart_amount = self.driver.find_element(By.CSS_SELECTOR, 'tfoot>tr>td>span>label').text
        self.assertEqual(cart_amount, f"({quantity1 + quantity2} Items)")
        sleep(2)

    def testcase10(self):
        username = 'eyal462'
        password = 'Eyal12345'
        # wait to site to open properly
        self.wait.until(EC.element_to_be_clickable((self.hp.account_icon())))
        # click on account icon
        self.hp.account_icon().click()
        sleep(1)
        # fill in account details to log in
        self.si.type_username_field("eyal462")
        sleep(1)
        self.si.type_password_field("Eyal12345")
        sleep(1)
        self.si.sign_in_button().click()
        sleep(4)
        # check if account actually logged in bi checking if his username next to the account icon
        site_username = self.driver.find_element(By.CSS_SELECTOR, '[id="menuUserLink"]>span').text
        self.assertEqual(site_username, username)
        # if site_username == username:
        #     print("log in test yes")
        # else:
        #     print("log in test no")
        sleep(2)
        # log out
        self.hp.account_icon().click()
        self.hp.account_options_list(3)
        sleep(1)
        site_username = self.driver.find_element(By.CSS_SELECTOR, '[id="menuUserLink"]>span').text
        self.assertEqual(site_username, '')



