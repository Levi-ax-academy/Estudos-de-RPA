#Imports Python
import logging
import time
#Imports Selenium
#Imports Pastas
from src.modulos.AutomationExercises_5.SOLID.actions.navigation import Navigation as N

logging.basicConfig(
    level=logging.INFO, # Mostra mensagens nível INFO e superior (WARNING, ERROR)
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"  # Formato de hora curto para facilitar a leitura no terminal
)

def main():
    #Iniciar página
    navigation = N()
    logging.info("Iniciando...")
    navigation.wait_for(type = "all")
    logging.info("Página totalmente carregada")

    navigation.find_click(colector = "a[href='/login']")
    navigation.wait_for(type = "visibility", colector = "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > h2")
    logging.info("'Login to your account' está visível.")
    navigation.fill_signup_form()
    logging.info("Formulário de registro preenchido.")
    navigation.find_click(colector = "button[data-qa='signup-button']")
    logging.info("Botão de registro clicado.")

    error_message = navigation.wait_for(type = "visibility", colector = "#form > div > div > div:nth-child(3) > div > form > p").text
    logging.info(f"Mensagem de erro visível: '{error_message}'")
    
    time.sleep(2)
    logging.info("Fechando...")
    
if __name__ == '__main__':
    main()