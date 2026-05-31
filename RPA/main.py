from src.modulos.SELENIUM.AutomationExercises_1.SELENIUM.user_register_main import main as main_registrar
from src.modulos.SELENIUM.AutomationExercises_2.SELENIUM.login_sucess_main import main as main_logar_sucesso
from src.modulos.SELENIUM.AutomationExercises_3.SELENIUM.login_failed_main import main as main_logar_falha
from src.modulos.SELENIUM.AutomationExercises_4.SELENIUM.logout_main import main as main_logout
from src.modulos.SELENIUM.AutomationExercises_5.SELENIUM.register_user_existing_email_main import main as main_registrar_email_existente 
from src.modulos.SELENIUM.Desafio01_27_04_2026_MCeMB.SELENIUM.mcemb_main import main as main_desafio
from src.modulos.SELENIUM.AutomationExercises_6.SELENIUM.contact_us_main import main as main_contact_us
from src.modulos.SELENIUM.AutomationExercises_7.SELENIUM.vrf_test_case_pg_main import main as main_vtcp
from src.modulos.SELENIUM.AutomationExercises_8.SELENIUM.vapapdp_main import main as main_vapapdp
from src.modulos.SELENIUM.Desafio02_04_05_2026.SELENIUM.desafio_main import main as main_desafio2
import time

print("Escolha uma opção:")
print("1 - Registrar usuário")
print("2 - Logar usuário com sucesso")
print("3 - Logar usuário com falha")
print("4 - Logout do usuário")
print("5 - Registrar usuário com email existente")
print("6 - Desafio de Web Scraping")
print("7 - Contact Us")
print("8 - Página Test cases")
print("9 - Página Products")         
print("10 - Desafio 2")
print("all - Executar todos os testes")
opcao = str(input("Opção: "))

match opcao:
    case '1':
        print("A opção 1 foi selecionada.")
        main_registrar()
    case '2':
        print("A opção 2 foi selecionada.")
        main_logar_sucesso()
    case '3':
        print("A opção 3 foi selecionada.")
        main_logar_falha()
    case '4':
        print("A opção 4 foi selecionada.")
        main_logout()
    case '5':
        print("A opção 5 foi selecionada.")                                                                                                                                                                                        
        main_registrar_email_existente()
    case '6':
        print("A opção 6 foi selecionada.")
        main_desafio()
    case '7':
        print("A opção 7 foi selecionada.") 
        main_contact_us()
    case '8':
        print("A opção 8 foi selecionada.")
        main_vtcp()
    case '9':
        print("A opção 9 foi selecionada.")
        main_vapapdp()
    case '10':
        print("A opção 10 foi selecionada.")
        main_desafio2()
    case 'all':
        main_registrar()
        time.sleep(2)
        print("Próximo.")
        main_logar_sucesso()
        time.sleep(2)
        print("Próximo.")
        main_logar_falha()
        time.sleep(2)
        print("Próximo.")
        main_logout()
        time.sleep(2)
        print("Próximo.")
        main_registrar_email_existente()
        time.sleep(2)
        print("Próximo.")
        main_desafio()
        time.sleep(2)
        print("Próximo.")
        main_contact_us()
        time.sleep(2)
        print("Próximo.")
        main_vtcp()
        time.sleep(2)
        print("Próximo.")
        main_vapapdp()
        time.sleep(2)
        print("Próximo.")
        main_desafio2()
        time.sleep(2)
        print("Acabou.")
    