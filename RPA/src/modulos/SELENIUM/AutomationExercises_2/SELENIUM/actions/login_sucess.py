#Imports Python
import logging
#Imports Selenium

#Imports Pastas

logging.basicConfig(
    level=logging.INFO, # Mostra mensagens nível INFO e superior (WARNING, ERROR)
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"  # Formato de hora curto para facilitar a leitura no terminal
)

class Login_User:
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
    
    def delete_user(self):
        self.navigation.wait_for(type = "visibility", colector = "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(10) > a")
        self.navigation.find_click(colector = "a[href='/delete_account']")
        self.navigation.wait_for(type = "visibility", colector = "h2[data-qa='account-deleted']")
        logging.info("Conta deletada.")
    