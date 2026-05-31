from playwright.sync_api import sync_playwright
from RPA.src.modulos.DESAFIOS.Desafio_FlightRadar.actions.flight_radar import FlightRadar as FR
from time import sleep
def main():
    with sync_playwright() as p:
        fr = FR(p)
        fr.bm.login()
        fr.Apply_filters()
        sleep(15)
        fr.Scrap_Flight_Infos()

if __name__ == "__main__":
    main()