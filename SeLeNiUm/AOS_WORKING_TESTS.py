from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from AOS_Class import Home_Page, product_page, category_page, Sign_in_pop_up, Register_page
from tabulate import tabulate
import pandas as pd

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
        self.newuser = Register_page(self.driver)
    def test_Case1(self):
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
        cart_amount = self.hp.cart_total_amount.text
        self.assertEqual(cart_amount, f"({quantity1 + quantity2} Items)")
        sleep(2)

    def test_Case2(self):
        product1 = "HP ROAR MINI WIRELESS SPEAKER"
        product2 = "HP ROAR PLUS WIRELESS SPEAKER"
        product3 = "HP ROAR WIRELESS SPEAKER"
        amount1 = "1"
        amount2 = "2"
        amount3 = "3"
        color1 = "RED"
        color2 = "BLUE"
        color3 = "WHITE"
        price1 = "44.99"
        price2 = "339.98"
        price3 = "254.97"
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
        products = self.driver.find_elements(By.XPATH, "//tbody//h3")
        amounts = self.driver.find_elements(By.XPATH, "//td/a/label[contains(text(), 'QTY')]")
        prices = self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td:nth-of-type(3) > p.price")
        colors = self.driver.find_elements(By.XPATH, "//label[contains(text(), 'Color:')]/span")
        assert products[0].text == product3
        assert products[1].text == product2
        assert products[2].text == product1
        assert amounts[0].text[-1] == amount3
        assert amounts[1].text[-1] == amount2
        assert amounts[2].text[-1] == amount1
        assert prices[0].text[1:] == price3
        assert prices[1].text[1:] == price2
        assert prices[2].text[1:] == price1
        assert colors[0].text == color3
        assert colors[1].text == color2
        assert colors[2].text == color1

        table_data = []
        for i in range(len(products)):
            product_name = products[i].text
            amount = amounts[i].text.split(": ")[-1]
            price = prices[i].text
            color = colors[i].text
            table_data.append([product_name, amount, color, price])

        # Calculate the final price
        total_price = sum(float(price.text.strip("$")) for price in prices)

        # Add the final price row to the table
        table_data.append(["", "", "", f"Final Price: ${total_price:.2f}"])

        # Print the table
        print(tabulate(table_data, headers=["Product Name", "Amount", "Color", "Price"]))

    def test_Case3(self):
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
        remove_button = self.driver.find_elements(By.XPATH,"//div[@class='closeDiv']//div[@class='removeProduct iconCss iconX']")
        remove_button[0].click()
        products = self.driver.find_elements(By.XPATH, "//tbody//h3")
        sleep(1)
        assert len(products) == 1
        sleep(1)
        assert "HP ROAR MINI WIRELESS SPEAKER" == products[0].text

    def test_Case4(self):
        self.hp.speakers_link().click()
        sleep(2)
        self.cp.select_product_click(3)
        sleep(1)
        self.pp.add_to_cart_button().click()
        sleep(1)
        self.driver.find_element(By.ID, "menuCart").click()
        self.driver.find_elements(By.XPATH, "// h3[contains(text(), 'SHOPPING CART')]")

    def test_Case5(self):
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
        checkout = self.driver.find_element(By.CSS_SELECTOR, 'tfoot>tr>td>span.roboto-medium.cart-total.ng-binding').get_attribute('textContent')
        new_checkout = checkout[1:]             # remove doller
        prices = self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td:nth-of-type(3) > p.price")
        amounts = self.driver.find_elements(By.XPATH, "//td/a/label[contains(text(), 'QTY')]")
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
        new_amount3 = amounts[2].text[-1]
        new_amount2 = amounts[1].text[-1]
        new_amount1 = amounts[0].text[-1]
        assert float(new_price1) + float(new_price2) + float(new_price3) == float(new_checkout)
        headers = ["Name", "Amount", "Price"]
        table_data = [[name3, new_amount3, new_price1],
                      [name2, new_amount2, new_price2],
                      [name1, new_amount1, new_price3],
                      ["Checkout", " ",new_checkout]
                      ]
        print(tabulate(table_data, headers=headers))
        sleep(1)
    def test_Case7(self):
        self.wait.until(EC.element_to_be_clickable((self.hp.tablets_link())))
        self.hp.tablets_link().click()
        sleep(4)
        self.cp.select_product_click(2)
        sleep(3)
        self.driver.back()
        self.assertEqual(self.cp.category_name().text, "TABLETS")
        sleep(2)
        self.driver.back()
        self.wait.until(EC.element_to_be_clickable((self.hp.tablets_link())))
        sleep(1)

    def test_Case8(self):
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


    def test_Case9(self):
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
        sleep(1)
        self.driver.find_element(By.ID, "menuCart").click()
        sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, "li[data-ng-mouseenter='enterCart()'] ul li label[class='center roboto-medium ng-scope']")
        print("Cart is empty")

    def test_Case10(self):
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
        site_username = self.hp.show_username().text
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
        site_username = self.hp.show_username().text
        self.assertEqual(site_username, '')


