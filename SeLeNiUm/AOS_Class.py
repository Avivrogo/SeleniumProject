from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Account details:
# username: eyal462
# password: Eyal12345

class Home_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def site_logo(self):
        return self.driver.find_element(By.CLASS_NAME, 'logo')

    def account_icon(self):
        return self.driver.find_element(By.ID, 'menuUserLink')

    def account_options_list(self, option: int):
        lista = self.driver.find_elements(By.XPATH, "//div[@id='loginMiniTitle']/label")
        return lista[option - 1].click()

    def show_username(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[id="menuUserLink"]>span')
    def cart_icon(self):
        return self.driver.find_element(By.ID, 'shoppingCartLink')

    def cart_total_amount(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'tfoot>tr>td>span>label')

    def speakers_link(self):
        return self.driver.find_element(By.ID, 'speakersImg')

    def tablets_link(self):
        return self.driver.find_element(By.ID, 'tabletsImg')

    def laptops_link(self):
        return self.driver.find_element(By.ID, 'laptopsImg')

    def headphones_link(self):
        return self.driver.find_element(By.ID, 'headphonesImg')

    def mice_link(self):
        return self.driver.find_element(By.ID, 'miceImg')


class Sign_in_pop_up:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def username_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='username']")

    def type_username_field(self, username: str):
        self.username_field().send_keys(username)

    def password_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    def type_password_field(self, password: str):
        self.password_field().send_keys(password)

    def sign_in_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'button[id="sign_in_btnundefined"]')

    def create_new_account_link(self):
        return self.driver.find_element(By.CLASS_NAME, 'create-new-account ng-scope')

    def forgot_password_link(self):
        return self.driver.find_element(By.CLASS_NAME, 'forgot-Passwowd ng-scope')

    def remember_me_checkbox(self):
        return self.driver.find_element(By.CLASS_NAME, 'remember_me')


class Register_page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def newaccount_Button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.create-new-account.ng-scope')

    def Register_Button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#register_btnundefined')

    def new_username(self):
        return self.driver.find_element(By.NAME, 'usernameRegisterPage')

    def new_username_input(self, username):
        self.new_username().send_keys(username)

    def new_email(self):
        return self.driver.find_element(By.NAME, 'emailRegisterPage')

    def new_email_input(self, email):
        self.new_email().send_keys(email)

    def new_password(self):
        return self.driver.find_elements(By.NAME, 'passwordRegisterPage')

    def new_password_input(self, password):
        self.new_password()[0].send_keys(password)  # new password

    def new_cpassword(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name='confirm_passwordRegisterPage']")

    def new_cpassword_input(self, cpassword):
        self.new_cpassword().send_keys(cpassword)  # confirm new password

    def new_lname(self):
        return self.driver.find_element(By.NAME, 'last_nameRegisterPage')

    def new_lname_input(self, lname):
        self.new_lname().send_keys(lname)

    def new_fname(self):
        return self.driver.find_element(By.NAME, 'first_nameRegisterPage')

    def new_fname_input(self, fname):
        self.new_fname().send_keys(fname)

    def new_phone(self):
        return self.driver.find_element(By.NAME, 'phone_numberRegisterPage')

    def new_phone_input(self, phone):
        self.new_phone().send_keys(phone)

    def new_country(self):
        return self.driver.find_element(By.NAME, 'countryListboxRegisterPage')

    def new_country_input(self, country):
        country_listbox = self.new_country()
        for option in country_listbox.find_elements(By.TAG_NAME, 'option'):
            if country in option.text:
                option.click()  # select() in earlier versions of webdriver
                break

    def new_state(self):
        return self.driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage')

    def new_state_input(self, state):
        self.new_state().send_keys(state)

    def new_address(self):
        return self.driver.find_element(By.NAME, 'addressRegisterPage')

    def new_address_input(self, address):
        self.new_address().send_keys(address)

    def new_city(self):
        return self.driver.find_element(By.NAME, 'cityRegisterPage')

    def new_city_input(self, city):
        self.new_city().send_keys(city)

    def new_postal(self):
        return self.driver.find_element(By.NAME, 'postal_codeRegisterPage')

    def new_postal_input(self, postal):
        self.new_postal().send_keys(postal)

    def check_agree(self):

        return self.driver.find_element(By.CSS_SELECTOR, "input[name='i_agree']")

    def safepay_name(self):
        return self.driver.find_element(By.NAME, "safepay_username")

    def safepay_name_input(self, name):
        self.safepay_name().send_keys(name)

    def safepay_password(self):
        return self.driver.find_element(By.NAME, "safepay_password")

    def safepay_password_input(self, password):
        self.safepay_password().send_keys(password)

    def neworder_login_user(self):
        return self.driver.find_element(By.XPATH, "//input[@name='usernameInOrderPayment']")

    def neworder_login_user_input(self, user):
        self.neworder_login_user().send_keys(user)

    def neworder_login_password(self):
        return self.driver.find_element(By.XPATH, "//input[@name='passwordInOrderPayment']")

    def neworder_login_password_input(self, password):
        self.neworder_login_password().send_keys(password)

    def choose_mastercard(self):
        self.driver.find_element(By.XPATH, "//input[@name='masterCredit']").click()

    def mastercard_number(self, number):
        self.driver.find_element(By.NAME, "card_number").send_keys(number)

    def mastercard_cvv(self, cvv):
        self.driver.find_element(By.NAME, "cvv_number").send_keys(cvv)

    def mastercard_month(self, month):
        month_dropdown = self.driver.find_element(By.NAME, "mmListbox")
        for option in month_dropdown.find_elements(By.TAG_NAME, 'option'):
            if month in option.text:
                option.click()
                break

    def mastercard_year(self, year):
        year_dropdown = self.driver.find_element(By.NAME, "yyyyListbox")
        for option in year_dropdown.find_elements(By.TAG_NAME, 'option'):
            if year in option.text:
                option.click()
                break

    def mastercard_cardholder_name(self, name):
        self.driver.find_element(By.NAME, "cardholder_name").send_keys(name)
class category_page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def products_list(self):
        return self.driver.find_elements(By.XPATH, "//div[@class='cell categoryRight']/ul/li")

    def select_product_click(self, product_num: int):
        self.products_list()[product_num - 1].click()

    def category_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='categoryTitle roboto-regular sticky ng-binding']")


class product_page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action_chains = ActionChains(self.driver)

    def add_to_cart_button(self):
        return self.driver.find_element(By.NAME, "save_to_cart")

    def quantity_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name = "quantity"]')

    def plus_quantity_button(self):
        return self.driver.find_element(By.CLASS_NAME, 'plus')

    def plus_quantity_click(self, quantity: str):
        for i in range(quantity - 1):
            self.plus_quantity_button().click()

    def change_quantity(self, quantity: str):
        self.action_chains.move_to_element(self.quantity_field()).click().send_keys(quantity).perform()
        # self.quantity_field().clear().send_keys(quantity)

    def colors(self):
        return self.driver.find_elements(By.XPATH, '//div[@ng-show="firstImageToShow"]//span')

    def color_choose(self, color_num: int):
        self.colors()[color_num + 1].click()

class shopping_cart_page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action_chains = ActionChains(self.driver)

    def edit_link(self, product_num_by_order_in_cart: int):
        return self.driver.find_element(By.XPATH, f'//tbody/tr[{product_num_by_order_in_cart}]/td[6]/span[1]/a[1]')

    def product_amount(self, product_num_by_order_in_cart: int):
        return self.driver.find_element(By.XPATH, f'//tbody[1]/tr[{product_num_by_order_in_cart}]/td[5]')

    def page_title(self):
        return self.driver.find_element(By.CLASS_NAME, 'roboto-regular center sticky fixedImportant ng-binding')

