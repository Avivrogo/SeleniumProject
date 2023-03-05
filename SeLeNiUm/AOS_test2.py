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

    def test_open_speakers(self):
        sleep(6)
        #self.hp = Home_Page(self.driver)
        self.hp.speakers_link().click()
        sleep(2)

    def TestCase5(self):
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
        self.driver.back()
        self.cp.select_product_click(5)
        sleep(1)
        self.pp.change_quantity(3)
        self.pp.add_to_cart_button().click()
        sleep(1)
        #assert "484.97" == self.driver.find_element(By.CSS_SELECTOR, 'tfoot>tr>td>span.roboto-medium.cart-total.ng-binding')
        checkout = self.driver.find_element(By.CSS_SELECTOR, 'tfoot>tr>td>span.roboto-medium.cart-total.ng-binding').get_attribute('textContent')
        new_checkout = checkout[1:]             # remove doller
        prices = self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td:nth-of-type(3) > p.price")
        amount1 = self.driver.find_elements(By.XPATH, "//td/a/label[contains(text(), 'QTY')]")
        names = self.driver.find_elements(By.XPATH, "//td/a/h3[@class='ng-binding']")
        name1 = names[0].text
        name2 = names[1].text
        name3 = names[2].text
        price1 = prices[0].text
        price2 = prices[1].text
        price3 = prices[2].text
        new_price1 = price1[1:]
        new_price2 = price2[1:]
        new_price3 = price3[1:]
        new_amount3 = amount1[2].text[-1]
        new_amount2 = amount1[1].text[-1]
        new_amount1 = amount1[0].text[-1]
        assert float(new_price1) + float(new_price2) + float(new_price3) == float(new_checkout)
        headers = ["Name", "Amount", "Price"]
        table_data = [[name3, new_amount3, new_price1],
                      [name2, new_amount2, new_price2],
                      [name1, new_amount1, new_price3],
                      ["Checkout", " ",new_checkout]
                      ]
        print(tabulate(table_data, headers=headers))
        sleep(1)

        #third_td = self.driver.find_element(By.CSS_SELECTOR, "tbody>tr>td:nth-of-type(3)")

    def testcase1(self):
        self.hp.speakers_link().click()
        sleep(4)
        self.cp.select_product_click(3)
        sleep(2)
        self.pp.change_quantity(2)
        self.pp.add_to_cart_button().click()
        sleep(3)
        self.driver.back()
        self.cp.select_product_click(4)
        sleep(2)
        self.pp.change_quantity(3)
        self.pp.add_to_cart_button().click()

    def test_TestCase8(self):
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

        self.driver.find_element(By.ID, "menuCart").click()
        self.driver.find_element(By.XPATH, "//button[@id='checkOutButton']").click()
        self.driver.find_element(By.ID,"registration_btnundefined").click()

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
        self.driver.find_element(By.ID, "next_btn").click()
        sleep(1)
        self.newuser.safepay_name_input("eyal12345")
        sleep(1)
        self.newuser.safepay_password_input("Eyal12345")
        sleep(1)
        self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY").click()
        sleep(1)

        tracknumber = self.driver.find_element(By.CSS_SELECTOR, "#orderNumberLabel").text

        self.driver.find_element(By.ID, "menuUserSVGPath").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//label[@role='link'][normalize-space()='My orders']").click()
        sleep(1)

        print(tracknumber)
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

    def test_TestCase9(self):
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

        self.driver.find_element(By.ID, "menuCart").click()
        self.driver.find_element(By.XPATH, "//button[@id='checkOutButton']").click()

        self.newuser.neworder_login_user_input("eyaltest12")
        self.newuser.neworder_login_password_input("Eyal12345")
        self.driver.find_element(By.ID, "login_btnundefined").click()
        self.driver.find_element(By.ID, "next_btn").click()

        self.newuser.choose_mastercard()
        self.newuser.mastercard_number("123456789101")
        self.newuser.mastercard_cvv("564")
        self.newuser.mastercard_year("2030")
        self.newuser.mastercard_month("10")
        self.newuser.mastercard_cardholder_name("eyal")
        self.driver.find_element(By.ID, "pay_now_btn_ManualPayment").click()
        sleep(3)

        tracknumber = self.driver.find_element(By.CSS_SELECTOR, "#orderNumberLabel").text
        self.driver.find_element(By.ID, "menuUserSVGPath").click()
        sleep(1)
        self.driver.find_element(By.XPATH, "//label[@role='link'][normalize-space()='My orders']").click()
        sleep(1)
        sleep(1)
        orderstracknumber = self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td:nth-of-type(1)>label.ng-binding")
        tracknumber_found = False
        for ordertrack in orderstracknumber:
            if tracknumber == ordertrack.text:
                tracknumber_found = True
                break

        if tracknumber_found == True:
            print(f"Order number {tracknumber} found in order list")
        else:
            print(f"Order number {tracknumber} not found in order list")
        assert tracknumber_found == True

