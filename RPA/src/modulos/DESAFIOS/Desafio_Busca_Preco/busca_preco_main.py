from playwright.sync_api import sync_playwright
import csv
import os
from time import sleep
from bs4 import BeautifulSoup
import pyautogui
import requests
URL = "https://buscapreco.sefaz.am.gov.br/home"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
partial_file_path = "C:\\Users\\levi1.cavalcante\\workspace\\Estudos-de-RPA\\RPA\\src\\modulos\\DESAFIOS\\Desafio_Busca_Preco\\data"
file_path = os.path.join(partial_file_path, 'lista_de_compras.csv')
items = []
items_filtred = []
with open(file_path, newline='', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        if [cell.strip() for cell in row] == ['Item', 'Marca']:
            continue
        item_text = row[0].strip()
        if len(row) > 1:
            item_text += ' ' + row[1].strip()
        items_filtred.append(item_text)
with sync_playwright() as p: 
    browser = p.chromium.launch(
        headless=False,
        executable_path=r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        ignore_default_args=["--enable-automation"],
        args=["--disable-blink-features=AutomationControlled"]
        )
    context = browser.new_context()
    page = context.new_page()
    page.goto(URL)
    for i in range(len(items_filtred)):
        item_found = True
        item = items_filtred[i]
        page.locator("id=descricaoProd").first.fill(item)
        page.locator("id=descricaoProd").first.press("Enter")
        page.wait_for_load_state("networkidle")
        try:
            page.wait_for_selector(".tb-valor-25", timeout=10000)
        except:
            print(f"Produto '{item}' não encontrado.")
            item_found = False
            pass
        data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data")
        pyautogui.screenshot(imageFilename=os.path.join(data_dir,"preco.png"))
        sleep(2)
        precos = []
        html = page.content()
        soup_page = BeautifulSoup(html, 'html.parser')
        produtos = soup_page.select("body > main > div:nth-child(3) > div:nth-child(1)")
        if not produtos:
            produtos = soup_page.select(".row")
        for produto in produtos:
            cards = produto.select(".col.s12.m4")
            for card in cards:
                preco = card.select_one(".tb-valor-25.indigo-text.text-darken-4.padding10")
                if preco is None:
                    preco = card.select_one(".tb-valor-25")
                if preco is None:
                    continue
                text = preco.get_text(strip=True)
                precos.append(text)
        if item_found: print(precos, " - - - ", item)
        sleep(3)