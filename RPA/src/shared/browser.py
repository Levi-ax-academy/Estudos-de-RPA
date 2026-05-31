from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import src.utils.constants.constants as C
import logging

logging.basicConfig(
    level=logging.INFO, # Mostra mensagens nível INFO e superior (WARNING, ERROR)
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"  # Formato de hora curto para facilitar a leitura no terminal
)

class Browser:
    def __init__(self, URL = C.URL):
        self.browser = webdriver.Chrome()
        self.browser.get(URL)
    def find_click (self, colector, by = By.CSS_SELECTOR):
        element = self.browser.find_element(by, colector)
        self.browser.execute_script("arguments[0].click();", element)
        return element

    def find_write (self, colector, by = By.CSS_SELECTOR, text = ''):
        element = self.browser.find_element(by, colector)
        print(element.text)
        element.send_keys(text)
        return element
    
    def find_select (self, colector, by = By.CSS_SELECTOR, option = ''):
        element = self.browser.find_element(by, colector)
        select = Select(element)
        select.select_by_visible_text(option)

        return element
    
    def wait_for(self, type, colector = '', by = By.CSS_SELECTOR):
        wait = WebDriverWait(self.browser, 5)
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
    def correct_url(self, verified_url = ''):
        self.wait_for(type='all')

        actual_url = self.browser.current_url
        if actual_url == verified_url:
            logging.info("Página correta!")
            return True
        if actual_url != verified_url: 
            logging.info("Página incorreta!")
            return False
