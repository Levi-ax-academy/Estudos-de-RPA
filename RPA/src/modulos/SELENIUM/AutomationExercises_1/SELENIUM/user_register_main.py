#Imports Python
import logging
import time
#Imports Selenium
#Imports Pastas

from src.modulos.SELENIUM.AutomationExercises_1.SELENIUM.actions.navigation import Navigation as N
from src.modulos.SELENIUM.AutomationExercises_1.SELENIUM.actions.register_user import Register_User as RU

logging.basicConfig(
    level=logging.INFO, # Mostra mensagens nível INFO e superior (WARNING, ERROR)
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"  # Formato de hora curto para facilitar a leitura no terminal
)

def main():
    #Iniciar página
    navigation = N()
    register_user = RU(navigation)
    logging.info("Iniciando...")
    navigation.wait_for(type = "all")
    logging.info("Página totalmente carregada")
    
    #Fazer cadastro
    register_user.cadastrar_usuario_pt1()

    #Preencher formulário de cadastro
    register_user.cadastrar_usuario_pt2()
    
    #Deletar Conta
    register_user.deletar_usuario()

    time.sleep(2)
    logging.info("Fechando...")

if __name__ == '__main__':
    main()