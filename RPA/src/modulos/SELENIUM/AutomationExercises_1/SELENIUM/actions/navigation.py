#Imports Python

#Imports Selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
#Imports Pastas
from src.shared.browser import Browser as B
from src.modulos.SELENIUM.AutomationExercises_1.SELENIUM.data.data import users, selectors_text, selectors_select

class Navigation:
    def __init__(self):
        self.driver = B().browser


    def find_click (self, colector, by = By.CSS_SELECTOR):
        element = self.driver.find_element(by, colector)
        self.driver.execute_script("arguments[0].click();", element)
        return element

    def find_write (self, colector, by = By.CSS_SELECTOR, text = ''):
        element = self.driver.find_element(by, colector)
        print(element.text)
        element.send_keys(text)
        return element

    def find_select (self, colector, by = By.CSS_SELECTOR, option = ''):
        element = self.driver.find_element(by, colector)
        select = Select(element)
        select.select_by_visible_text(option)

        return element
    
    def wait_for(self, type, colector = '', by = By.CSS_SELECTOR):
        wait = WebDriverWait(self.driver, 20)
        if type == 'visibility':
            wait.until(
                EC.visibility_of_element_located((by, colector))
            )
        elif type == 'clickable':
            wait.until(
                EC.element_to_be_clickable((by, colector))
            )
        elif type == 'all':
            wait.until(
                EC.visibility_of_all_elements_located
            )
    def fill_signup_form (self, user = users[0], selector_text = selectors_text[0]):
        for u in user:    
            if u in ['name', 'email']:
                self.find_write(colector=selector_text[u], text=user[u])

    def fill_extended_signup_form (self, user = users[0], selector_text = selectors_text[0], selector_select = selectors_select[0]):
        for u in user:
            if u not in ['name', 'email', 'password']:
                if u in ['birthday', 'birthmonth', 'birthyear', 'country']:
                    self.find_select(colector=selector_select[u], option=user[u])
                elif u in ['gender', 'newsletter', 'offers', 'create_account']:
                    self.find_click(colector=user[u])
                else:
                    self.find_write(colector=selector_text[u], text=user[u])
