#Imports Python
import logging
#Imports Selenium

#Imports Pastas

logging.basicConfig(
    level=logging.INFO, # Mostra mensagens nível INFO e superior (WARNING, ERROR)
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"  # Formato de hora curto para facilitar a leitura no terminal
)

class Register_User:
    def __init__(self, nav_instance):
        self.navigation = nav_instance
        
    def cadastrar_usuario_pt1(self):
        self.navigation.find_click(colector = "a[href='/login']")
        logging.info("Botão Login clicado")
        self.navigation.wait_for(type = "visibility", colector = "div.signup-form h2")
        logging.info("'New User Signup!' está visível")
        self.navigation.fill_signup_form()
        self.navigation.find_click(colector = "button[data-qa='signup-button']")
        logging.info("Nome e email preenchidos. Botão Signup clicado")
    
    def cadastrar_usuario_pt2(self):
        self.navigation.wait_for(type = "visibility", colector = "#form > div > div > div > div.login-form > h2 > b")
        logging.info("'Enter Account Information' está visível")
        
        self.navigation.fill_extended_signup_form()
        logging.info("Formulário de cadastro preenchido")

        self.navigation.wait_for(type = "visibility", colector = "h2[data-qa='account-created']")
        logging.info("Conta criada com sucesso")

        self.navigation.find_click(colector = "a[data-qa='continue-button']")
        logging.info("Botão Continue clicado")
    
    def deletar_usuario(self):
        self.navigation.wait_for(type = "visibility", colector = "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(10) > a > i")
        logging.info("'Logged as...' está visível")

        self.navigation.find_click(colector = "a[href='/delete_account']")
        logging.info("Botão Delete Account clicado")

        self.navigation.wait_for(type = "visibility", colector = "h2[data-qa='account-deleted']")
        logging.info("Conta deletada com sucesso")

        self.navigation.find_click(colector = "a[data-qa='continue-button']")
        logging.info("Botão Continue clicado")
    