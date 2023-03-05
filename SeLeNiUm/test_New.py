from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from unittest import TestCase
from AOS_Class import Home_Page, product_page, category_page, Sign_in_pop_up, Register_page
from prettytable import PrettyTable
from tabulate import tabulate

class Test_AOS(TestCase):
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
        self.newuser = Register_page(self.driver)

    def TestCase8(self):
        self.hp.speakers_link().click()
        sleep(2)
        self.cp.select_product_click(3)
        sleep(1)
        self.pp.add_to_cart_button().click()
        sleep(1)
        self.driver.back()
        self.cp.select_product_click(4)
        sleep(1)
        self.pp.change_quantity(2)
        self.pp.add_to_cart_button().click()

        self.driver.find_element(By.ID, "menuCart")
        self.driver.find_element(By.ID, "checkOutButton")
        self.driver.find_element(By.ID,"registration_btnundefined")

        self.newuser.new_username_input('eyaltest12')
        sleep(1)
        self.newuser.new_email_input('ewasds@gmail.com')
        sleep(1)
        self.newuser.new_password_input('Eyal12345')
        sleep(1)
        self.newuser.new_cpassword_input('Eyal12345')
        sleep(1)
        self.newuser.new_lname_input('eyal')
        sleep(1)
        self.newuser.new_fname_input('berko')
        sleep(1)
        self.newuser.new_phone_input('0524235798')
        sleep(1)
        self.newuser.new_country_input('Israel')
        sleep(1)
        self.newuser.new_state_input('Kirya')
        sleep(1)
        self.newuser.new_address_input('Mavo Lulav, 9')
        sleep(1)
        self.newuser.new_city_input('Yahud')
        sleep(1)
        self.newuser.new_postal_input('54254')
        sleep(1)
        self.newuser.check_agree().click()
        sleep(1)
        self.newuser.Register_Button().click()
        sleep(5)
        self.driver.find_element(By.ID, "next_btn")
        sleep(1)
        self.newuser.safepay_name_input("eyal12345")
        sleep(1)
        self.newuser.safepay_password_input("Eyal12345")
        sleep(1)
        self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")
        self.driver.find_element(By.ID, "menuUserSVGPath")
        self.driver.find_element(By.LINK_TEXT, "My orders")
        tracknumber = self.driver.find_element(By.ID, "trackingNumberLabel").text
        orderstracknumber = self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td:nth-of-type(1)>label.ng-binding")

        tracknumber_found = False
        for ordertrack in orderstracknumber:
            if tracknumber == ordertrack.text:
                tracknumber_found = True
                break

        if tracknumber_found == True:
            print(f"Track number {tracknumber} found in order list")
        else:
            print(f"Track number {tracknumber} not found in order list")
        assert tracknumber_found == True