import requests
from bs4 import BeautifulSoup
from src.modulos.Desafio01_27_04_2026_MCeMB.SOLID.data.data import content
from src.utils.constants.constants import URL

class Navigation:
    def __init__(self, url):
        self.html = requests.get(url)
        self.soup = BeautifulSoup(self.html.content, 'html.parser')
        self.items = []

    def get_products(self, url):
        names = self.soup.select(content[0]["name"])
        prices = self.soup.select(content[0]["price"])
        ids = self.soup.select(content[0]["id"])
        hrefs = self.soup.select(content[0]["href"])

        for i in range(len(names)):
            if names[i] and prices[i] and ids[i] and hrefs[i]:
                self.items.append({
                    "name": names[i].get_text(strip=True),
                    "price": prices[i].get_text(strip=True),
                    "id": ids[i].get("data-product-id").strip(),
                    "href": url + hrefs[i].get("href").strip()
                })
        return self.items
