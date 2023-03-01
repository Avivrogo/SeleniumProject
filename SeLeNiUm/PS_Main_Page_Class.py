nimals_sidebar_list

class PS_Home_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def animals_sidebar_list(self):
        sidebar = self.driver.find_element(By.ID, 'SidebarContent')
        return sidebar.find_elements(By.TAG_NAME, 'a')

    def animal_category_click(self, animal_type: int):
        self.animals_sidebar_list()[animal_type -1].click()

    def site_logo(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#LogoContent img')
