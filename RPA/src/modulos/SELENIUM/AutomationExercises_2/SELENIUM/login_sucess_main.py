#Imports Python
import logging
import time
#Imports Selenium
#Imports Pastas
from src.modulos.SELENIUM.AutomationExercises_2.SELENIUM.actions.navigation import Navigation as N
from src.modulos.SELENIUM.AutomationExercises_2.SELENIUM.actions.login_sucess import Login_User as LU
logging.basicConfig(
    level=logging.INFO, # Mostra mensagens nível INFO e superior (WARNING, ERROR)
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"  # Formato de hora curto para facilitar a leitura no terminal
)

def main():
    #Iniciar página
    navigation = N()
    login_user = LU(navigation)
    logging.info("Iniciando...")
    navigation.wait_for(type = "all")
    logging.info("Página totalmente carregada")

    login_user.login()
    login_user.delete_user()

    time.sleep(2)
    logging.info("Fechando...")
    
if __name__ == '__main__':
    main()