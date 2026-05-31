#Imports Python

#Imports Selenium

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Imports Pastas
from src.shared.browser import Browser as B
from src.modulos.SELENIUM.AutomationExercises_5.SELENIUM.data.data import user, selector

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
    
    def fill_signup_form (self,user_info = user[0], colectors = selector[0]):
        for u in user_info:
            self.find_write(colector = colectors[u], text = user_info[u])

    def wait_for(self, type, colector = '', by = By.CSS_SELECTOR):
        wait = WebDriverWait(self.driver, 20)
        if type == 'visibility':
            return wait.until(
                EC.visibility_of_element_located((by, colector))
            )
        elif type == 'clickable':
            return wait.until(
                EC.element_to_be_clickable((by, colector))
            )
        elif type == 'all':
            return wait.until(
                EC.visibility_of_all_elements_located
            )