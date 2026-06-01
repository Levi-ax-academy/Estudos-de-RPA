from playwright.sync_api import Playwright
from src.modulos.DESAFIOS.Desafio_FlightRadar.data_assets.mock import images_path as ipath, selectors as sel
from src.modulos.DESAFIOS.Desafio_FlightRadar.actions.browser_manager import BrowserManager as BM
import pyautogui as pyag
import os
import csv
from dotenv import load_dotenv
from time import sleep
class FlightRadar:
    def __init__(self, playwright: Playwright):
        self.bm = BM(playwright)
        self.page = self.bm.page
    def Apply_filters(self):
        self.page.locator(sel["SETTINGS"]).wait_for(state="visible")
        self.page.locator(sel["SETTINGS"]).click()
        self.page.locator(sel["B_AND_W"]).wait_for(state="visible", timeout=10000)
        self.page.locator(sel["B_AND_W"]).click()
        self.page.locator(sel["CLOSE_SETTINGS"]).click()
        self.page.wait_for_timeout(3000)

    def Check_Planes_Helicopters(self):
        data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data_assets")
        for i in range(5):
            planes_center = pyag.locateCenterOnScreen(image=ipath["aviao"], confidence=0.5, region=(25,120,1180,880))
            print(f"Avião encontrado no centro: {planes_center}")
            if planes_center:
                pyag.moveTo(planes_center[0], planes_center[1], duration=0.2)
                pyag.click()
            else:
                print("Avião não encontrado!")
                continue
            sleep(5)
            print_path = os.path.join(data_dir, f"avioes{i}.png")
            pyag.screenshot(imageFilename=print_path)
            self.page.locator(sel["close_flight_info"]).click()
            sleep(5)
            helicopter_center = pyag.locateCenterOnScreen(image=ipath["helicoptero"], confidence=0.5, region=(25,120,1180,880))
            print(f"Helicóptero encontrado no centro: {helicopter_center}")
            if helicopter_center:
                pyag.moveTo(helicopter_center[0], helicopter_center[1], duration=0.2)
                pyag.click()
            else:
                print("Helicóptero não encontrado!")
                continue
            sleep(5)
            print_path = os.path.join(data_dir, f"helicopteros{i}.png")
            pyag.screenshot(imageFilename=print_path)
            self.page.locator(sel["close_flight_info"]).click()
            sleep(5)
        
    def Scrap_Flight_Infos(self):
        data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data_assets")
        self.fly_number = self.page.locator(sel["fly_number"]).all_inner_texts()
        self.fly_code = self.page.locator(sel["fly_code"]).all_inner_texts()
        self.departure_city = self.page.locator(sel["departure_city"]).all_inner_texts()
        self.arrival_city = self.page.locator(sel["arrival_city"]).all_inner_texts()
        self.time_remaining = self.page.locator(sel["time_remaining"]).all_inner_texts()
        self.time_remaining = self.time_remaining[0].split(' in ')[1].strip()
        self.print_path = os.path.join(data_dir, "flight_info.png")
        pyag.screenshot(imageFilename=self.print_path,region=[40,205,425,776])
        print(self.fly_number, self.fly_code, self.departure_city, self.arrival_city, self.time_remaining)