from playwright.sync_api import Playwright
from RPA.src.modulos.DESAFIOS.Desafio_FlightRadar.data_assets.mock import images_path as ipath, selectors as sel
from RPA.src.modulos.DESAFIOS.Desafio_FlightRadar.actions.browser_manager import BrowserManager as BM
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
        self.page.locator(sel["SETTINGS"]).wait_for(state="visible", timeout=10000)
        self.page.locator(sel["SETTINGS"]).click()
        self.page.locator(sel["B_AND_W"]).wait_for(state="visible", timeout=10000)
        self.page.locator(sel["B_AND_W"]).click()
        self.page.locator(sel["CLOSE_SETTINGS"]).click()
        self.page.wait_for_timeout(3000)

    def Check_Planes_Helicopters(self):
        planes_loc = pyag.locateAllOnScreen(image=ipath["aviao"])
        print(planes_loc)
        sleep(5)
        helicopter_loc = pyag.locateAllOnScreen(image=ipath["helicoptero"])
        print(helicopter_loc)
        sleep(5)
    def Scrap_Flight_Infos(self):
        self.fly_number = self.page.locator(sel["fly_number"]).all_inner_texts()
        self.fly_code = self.page.locator(sel["fly_code"]).all_inner_texts()
        self.departure_city = self.page.locator(sel["departure_city"]).all_inner_texts()
        self.arrival_city = self.page.locator(sel["arrival_city"]).all_inner_texts()
        self.time_remaining = self.page.locator(sel["time_remaining"]).all_inner_texts()
        self.time_remaining = self.time_remaining[0].split(' in ')[1].strip()
        self.print_path = "RPA\\src\\modulos\\DESAFIOS\\Desafio_FlightRadar\\data_assets\\flight_info.png"
        pyag.screenshot(imageFilename=self.print_path,region=[40,205,425,776])
        print(self.fly_number, self.fly_code, self.departure_city, self.arrival_city, self.time_remaining)