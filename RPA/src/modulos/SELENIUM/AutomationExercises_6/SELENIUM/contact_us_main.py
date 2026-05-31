from src.modulos.AutomationExercises_6.SOLID.actions.navigation import Navigation as Nav
import logging

logging.basicConfig(
    level=logging.INFO, # Mostra mensagens nível INFO e superior (WARNING, ERROR)
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"  # Formato de hora curto para facilitar a leitura no terminal
)

def main():
    nav = Nav()
    nav.go_to_contact_us()
    logging.info("Página de contato acessada")
    nav.fill_email_form()
    logging.info("Formulário preenchido")
    nav.back_to_home()
    logging.info("Voltou para a página inicial")

if __name__ == "__main__":
    main()