from src.shared.browser import Browser as B
import logging

logging.basicConfig(
    level=logging.INFO, # Mostra mensagens nível INFO e superior (WARNING, ERROR)
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"  # Formato de hora curto para facilitar a leitura no terminal
)

class VTCP:
    def __init__(self):
        self.driver = B()

    def open_test_case_pg(self):
        self.driver.wait_for(type='all')
        logging.info("Home Page carregada.")
        self.driver.find_click(colector = "a[href= '/test_cases']")
        logging.info("Btn test case clicado.")
        self.driver.wait_for(type = 'visibility', colector = "h2 > b")
        logging.info("Test cases page carregada.")

