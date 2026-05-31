#Imports Python
import logging
import time
#Imports Selenium
#Imports Pastas
from src.modulos.SELENIUM.AutomationExercises_3.SELENIUM.actions.navigation import Navigation as N

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
    
    #Preencher formulário de login
    navigation.find_click(colector = "a[href='/login']")
    navigation.wait_for(type = "visibility", colector = "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > h2")
    logging.info("'Login to your account' está visível.")
    navigation.fill_login_form()
    navigation.find_click(colector = "button[data-qa='login-button']")
    logging.info("Formulário de login preenchido e enviado")

    #Aguardar mensagem de erro de login
    error_message = navigation.wait_for(type = "visibility", colector = "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > p").text
    logging.info(f"Mensagem de erro de login visível: {error_message}")

    time.sleep(2)
    logging.info("Fechando...")
    
if __name__ == '__main__':
    main()