from src.shared.browser import Browser as B
from src.modulos.Desafio02_04_05_2026.SOLID.data.data import user_selectors as us, user_infos as ui, buttons_selectors as bs

class Navigation:
    def __init__(self):
        self.driver = B()
    
    def go_to_login_signup_page(self):
        self.driver.wait_for(type='all')
        self.driver.find_click(bs['login-signup'])
        self.driver.wait_for(type='all')
    
