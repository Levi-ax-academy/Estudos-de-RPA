from src.shared.browser import Browser as B
from src.modulos.SELENIUM.AutomationExercises_8.SELENIUM.data.data import selectors

import logging

logging.basicConfig(
    level=logging.INFO, # Mostra mensagens nível INFO e superior (WARNING, ERROR)
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"  # Formato de hora curto para facilitar a leitura no terminal
)


class Navigation:
    def __init__(self):
        self.driver = B()

    def go_to_products(self):
        self.driver.wait_for(type='all')
        logging.info("Home page carregada com sucesso!")
        self.driver.find_click(colector=selectors['btn_products'])
        logging.info("Pagina de produtos selecionado!") 
        if self.driver.correct_url(verified_url='https://automationexercise.com/products') == False:
            self.driver.browser.close()
        self.driver.wait_for(type='visibility', colector= selectors['products_list'])
        logging.info("Lista de produtos visível!")
        
        
    def go_to_product_1(self):
        self.driver.find_click(colector= selectors['btn_view_product_1'])
        logging.info("Produto 1 selecionado!")
        if self.driver.correct_url(verified_url='https://automationexercise.com/product_details/1') == False:
            self.driver.browser.close()

        for sel in selectors:
            if sel not in ['btn_products', 'products_list', 'btn_view_product_1']:    
                self.driver.wait_for(type='visibility', colector=selectors[sel])
                logging.info(f"{sel} está visível")

        logging.info("Todos os elementos do produto 1 estão visíveis!")
        
        
