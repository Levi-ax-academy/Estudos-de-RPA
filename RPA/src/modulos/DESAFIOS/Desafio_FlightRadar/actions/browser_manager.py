from playwright.sync_api import Playwright
from RPA.src.modulos.DESAFIOS.Desafio_FlightRadar.data_assets.mock import selectors as sel
import pyautogui as pyag
import os
from dotenv import load_dotenv
class BrowserManager:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(
        headless=False,
        executable_path=r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        ignore_default_args=["--enable-automation"],
        args=["--disable-blink-features=AutomationControlled"]
        )
        
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto(sel["URL"], wait_until="domcontentloaded")
        try:
            self.page.locator(sel["AGREE_COOKIES"]).click()
            self.page.locator(sel["CLOSE_POPUP"]).click()
        except:
            print("Popups não encontrados ou já fechados.")
            
        self.page.wait_for_timeout(3000)
    
    def login(self):
        load_dotenv()
        self.email = os.getenv("EMAIL")
        self.senha = os.getenv("PASSWORD")
        self.page.locator(sel["LOGIN"]).click()
        self.page.locator(sel["GOOGLE_LOGIN"]).click()
        
        self.page.locator(sel["email_input"]).wait_for(state="visible")
        self.page.locator(sel["email_input"]).fill(self.email)
        self.page.locator(sel["email_input"]).press("Enter")
        
        self.page.locator(sel["password_input"]).wait_for(state="visible")
        self.page.locator(sel["password_input"]).fill(self.senha)
        self.page.locator(sel["password_input"]).press("Enter")
        self.context.storage_state(path="state.json")
