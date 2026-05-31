import time
from selenium.common.exceptions import TimeoutException
from src.modulos.Desafio02_04_05_2026.SOLID.data.data import user_selectors as us, user_infos as ui, buttons_selectors as bs

class Signup:
    def __init__(self, nav_instance):
        self.navigation = nav_instance

    def fill_pre_signup_form(self):
        for user in ui:
            if user in ['name', 'signup-email']:
                self.navigation.driver.find_write(colector=us[user], text= ui[user])
        self.navigation.driver.find_click(colector=bs['signup'])
        try:
            self.navigation.driver.wait_for(type='visibility', colector=bs['sucess-pre-signup'])
            return 'success'
            
        except TimeoutException:
            try:
                self.navigation.driver.wait_for(type='visibility', colector=bs['failed-pre-signup'])
                return 'failed'
            except TimeoutException:
                print("Nem sucesso, nem falha encontrados!")
                return 'error'

   
    def fill_extended_signup_form (self):
        for u in ui:
            if u not in ['name', 'signup-email', 'login-email', 'login-password']:
                if u in ['birth-day', 'birth-month', 'birth-year', 'country']:
                    self.navigation.driver.find_select(colector=us[u], option=ui[u])
                elif u in ['gender', 'newsletter', 'offers']:
                    self.navigation.driver.find_click(colector=us[u])
                else:
                    self.navigation.driver.find_write(colector=us[u], text=ui[u])
        self.navigation.driver.find_click(colector=bs['create-account'])
        self.navigation.driver.wait_for(type='all')
        self.navigation.driver.find_click(colector=bs['continue-created-account'])
