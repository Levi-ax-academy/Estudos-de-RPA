from RPA.src.modulos.SELENIUM.Desafio02_04_05_2026.SELENIUM.actions.login import Login as L
from RPA.src.modulos.SELENIUM.Desafio02_04_05_2026.SELENIUM.actions.signup import Signup as SU
from RPA.src.modulos.SELENIUM.Desafio02_04_05_2026.SELENIUM.actions.navigation import Navigation as N

def main():
    nav = N()
    login = L(nav_instance = nav)
    signup = SU(nav_instance = nav)

    nav.go_to_login_signup_page()
    while True:
        state_signup = signup.fill_pre_signup_form()
        
        if state_signup == 'success':
            signup.fill_extended_signup_form()
            print("Conta criada com sucesso!")
            break 
            
        elif state_signup == 'failed':
            print("E-mail já existe. Tentando fazer login e deletar a conta...")
            state_login = login.fill_login_form()
            
            if state_login == 'success':
                login.delete_account()
                print("Conta deletada. Retornando ao início do loop para cadastrar.")
                
            else:
                print("Erro crítico: Não consegui criar a conta nem fazer login.")
                break

if __name__ == "__main__":
    main()