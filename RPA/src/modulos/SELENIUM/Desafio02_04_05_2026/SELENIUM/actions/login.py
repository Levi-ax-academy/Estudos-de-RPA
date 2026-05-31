from selenium.common.exceptions import TimeoutException
from src.modulos.Desafio02_04_05_2026.SOLID.data.data import user_selectors as us, user_infos as ui, buttons_selectors as bs

class Login:
    def __init__(self, nav_instance):
        self.navigation = nav_instance

    def fill_login_form (self):
        for u in ['login-email', 'login-password']:
            self.navigation.driver.find_write(colector=us[u], text=ui[u])
        self.navigation.driver.find_click(colector=bs['login'])
        try:
            self.navigation.driver.wait_for(type='visibility', colector=bs['confirmed-login'])
            return 'success'
        except TimeoutException:
            try:
                self.navigation.driver.wait_for(type='visibility', colector=bs['failed-login'])
                return 'failed'
            except TimeoutException:
                return 'error'
    
    def delete_account(self):
        self.navigation.driver.find_click(colector=bs['delete-account'])
        self.navigation.driver.wait_for(type='visibility', colector=bs['confirmed-delete'])
        self.navigation.driver.find_click(colector=bs['login-signup'])