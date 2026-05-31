from src.shared.browser import Browser as B
from src.modulos.AutomationExercises_6.SOLID.data.data import selectors

class Navigation:
    def __init__(self):
        self.driver = B()
                 
    def go_to_contact_us(self):
        self.driver.wait_for(type='all')
        self.driver.find_click( colector= selectors['contact_us'])
        self.driver.wait_for(type='visibility', colector= selectors['contact_title'])

    def fill_email_form(self):

        self.driver.find_write(colector=selectors['name_input'], text="Lesvis")
        self.driver.find_write(colector=selectors['email_input'], text="lesviscavalcants@gmail.com")
        self.driver.find_write(colector=selectors['subject_input'], text="Teste de automação")
        self.driver.find_write(colector=selectors['message_input'], text="Olá, este é um teste de automação utilizando o framework RPA Framework e aplicando os princípios SOLID.")
        self.driver.find_click(colector=selectors['submit_button'])
        self.driver.browser.switch_to.alert.accept()

    def back_to_home(self):
        self.driver.wait_for(type='visibility', colector=selectors['success_message'])
        self.driver.find_click(colector=selectors['btn_home'])
        self.driver.wait_for(type='all')
