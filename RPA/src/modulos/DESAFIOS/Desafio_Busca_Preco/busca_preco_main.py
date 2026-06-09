from playwright.sync_api import sync_playwright
import csv
import os
from time import sleep
import pyautogui
partial_file_path = "C:\\Users\\levi1.cavalcante\\Estudos-de-RPA\\RPA\\src\\modulos\\DESAFIOS\\Desafio_Busca_Preco\\data"
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
    page.goto("https://buscapreco.sefaz.am.gov.br/home")
    for i in range(len(items_filtred)):
        item = items_filtred[i]
        page.locator("id=descricaoProd").first.fill(item)
        page.locator("id=descricaoProd").first.press("Enter")
        page.wait_for_load_state()
        data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data")
        pyautogui.screenshot(imageFilename=os.path.join(data_dir,"preco.png"))
        sleep(2)
        precos = []
        for j in range(12):
            match j:
                case 0: k = 1
                case 1: k = 4
                case 2: k = 7
                case 3: k = 10
                case 4: k = 13
                case 5: k = 16
                case 6: k = 19
                case 7: k = 22
                case 8: k = 25
                case 9: k = 28
                case 10: k = 31
                case 11: k = 34
                case _:
                    k = None

            locator = page.locator(f"xpath=/html/body/main/div[3]/div[1]/div[{k}]/div/div[2]/p[1]")
            text = locator.inner_text()
            precos.append(text)
        print(precos)