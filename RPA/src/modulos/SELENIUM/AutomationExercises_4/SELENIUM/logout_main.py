#Imports Python
import logging
import time
#Imports Selenium
#Imports Pastas
from src.modulos.AutomationExercises_4.SOLID.actions.navigation import Navigation as N
from src.modulos.AutomationExercises_4.SOLID.actions.logout import Logout_User as LU

logging.basicConfig(
    level=logging.INFO, # Mostra mensagens nível INFO e superior (WARNING, ERROR)
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"  # Formato de hora curto para facilitar a leitura no terminal
)

def main():
    #Iniciar página
    navigation = N()
    logout_user = LU(navigation)
    logging.info("Iniciando...")
    navigation.wait_for(type = "all")
    logging.info("Página totalmente carregada")
    
    logout_user.login()
    
    logout_user.logout()
    
    time.sleep(2)
    logging.info("Fechando...")
    
if __name__ == '__main__':
    main()