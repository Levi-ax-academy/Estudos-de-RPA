from playwright.sync_api import Playwright
from src.modulos.DESAFIOS.Desafio_FlightRadar.data_assets.mock import selectors as sel
import pyautogui as pyag
import os
from dotenv import load_dotenv
from time import sleep
class BrowserManager:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(
        headless=False,
        executable_path=r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        ignore_default_args=["--enable-automation"],
        args=["--disable-blink-features=AutomationControlled"]
        )
        
        self.context = self.browser.new_context()
        if os.path.exists("state.json"):
            self.context.set_storage_state("state.json")

        self.page = self.context.new_page()
        self.page.goto(sel["URL"], wait_until="domcontentloaded")
        try:
            self.page.locator(sel["AGREE_COOKIES"]).is_visible(timeout=5000)
            self.page.locator(sel["AGREE_COOKIES"]).click(timeout=5000)
            self.page.locator(sel["CLOSE_POPUP"]).is_visible(timeout=5000)
            self.page.get_by_role("button", name="Close").click()
        except:
            print("Popups não encontrados ou já fechados.")
            
        self.page.wait_for_timeout(3000)
    
    def login(self):
        if os.path.exists("state.json"):
            print("Sessão já autenticada. Pulando login.")
            pass
        if not os.path.exists("state.json"):
            load_dotenv()
            self.email = os.getenv("EMAIL")
            self.senha = os.getenv("PASSWORD")
            self.page.locator(sel["LOGIN"]).click()        
            self.page.locator(sel["email_input"]).wait_for(state="visible")
            self.page.locator(sel["email_input"]).fill(self.email)
            self.page.locator(sel["password_input"]).fill(self.senha)
            self.page.locator(sel["password_input"]).press("Enter")
            sleep(10)
            self.context.storage_state(path="state.json")
    
    def navigate_on_screen(self, attempts):
        match attempts:
            case 9:
                pyag.dragTo(250, 250, duration=0.5)
            case 19:
                pyag.dragTo(350, 350, duration=0.5)
            case 29:
                pyag.dragTo(450, 450, duration=0.5) 
            case 39:
                pyag.dragTo(550, 550, duration=0.5)
            case 49:
                pyag.dragTo(650, 650, duration=0.5)
            case 59:
                pyag.dragTo(750, 750, duration=0.5)
            case default:
                print("Tentativa não reconhecida.")
                return