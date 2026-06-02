from playwright.sync_api import sync_playwright
from src.modulos.DESAFIOS.Desafio_FlightRadar.actions.flight_radar import FlightRadar as FR
from time import sleep
def main():
    with sync_playwright() as p:
        fr = FR(p)
        fr.bm.login()
        fr.Apply_filters()
        fr.Check_Planes()
        fr.Check_Helicopters()
        sleep(15)

if __name__ == "__main__":
    main()