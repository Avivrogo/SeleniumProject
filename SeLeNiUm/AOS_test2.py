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
from AOS_Class import Home_Page, product_page, category_page, Sign_in_pop_up

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

    def test_open_speakers(self):
        sleep(6)
        #self.hp = Home_Page(self.driver)
        self.hp.speakers_link().click()
        sleep(2)

    def testcase2(self):
        #list = self.driver.find_elements(By.XPATH, "//div[@class='cell categoryRight']/ul/li")
        #list[0].click()
        self.hp.speakers_link().click()
        sleep(4)
        self.cp.select_product_click(3)
        sleep(2)
        self.pp.add_to_cart_button().click()
        sleep(3)
        self.driver.back()
        self.cp.select_product_click(4)
        sleep(2)
        self.pp.add_to_cart_button().click()
        self.driver.back()
        self.cp.select_product_click(1)
        sleep(2)
        self.pp.add_to_cart_button().click()

        # self.driver.find_element(By.XPATH, "//img[@id='20']").click()
        # hp.add_to_cart_button()
        # self.driver.find_element(By.XPATH, "//img[@id='25']").click()
        # hp.add_to_cart_button()
        # self.driver.find_element(By.XPATH, "//a[normalize-space()='SPEAKERS']").click()
        # self.driver.find_element(By.XPATH, "// img[ @ id = '24']").click()
        # hp.add_to_cart_button()



