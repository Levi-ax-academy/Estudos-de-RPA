#Imports Python
import logging
#Imports Selenium

#Imports Pastas

logging.basicConfig(
    level=logging.INFO, # Mostra mensagens nível INFO e superior (WARNING, ERROR)
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"  # Formato de hora curto para facilitar a leitura no terminal
)

class Logout_User:
    def __init__(self, nav_instance):
        self.navigation = nav_instance
    
    def login (self):
        self.navigation.find_click(colector = "a[href='/login']")
        self.navigation.wait_for(type = "visibility", colector = "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > h2")
        logging.info("'Login to your account' está visível.")
        self.navigation.fill_login_form()
        logging.info("Formulário de login preenchido.")
        self.navigation.find_click(colector = "button[data-qa='login-button']")
        logging.info("Botão de login clicado.")
    
    def logout(self):
        self.navigation.wait_for(type = "visibility", colector = "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(10) > a")
        self.navigation.find_click(colector = "a[href='/logout']")
        current_url = self.navigation.driver.current_url
        if current_url == "https://automationexercise.com/login":
                logging.info("Logout bem-sucedido. URL atual: " + current_url)
        logging.info("Usuário desconectado.")
    