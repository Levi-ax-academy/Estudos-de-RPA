import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import os
import csv
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://br.linkedin.com/")
    page.get_by_role("link", name="Entrar", exact=True).click()
    page.get_by_role("textbox", name="E-mail ou telefone").fill("levicavalcante07@gmail.com")
    page.get_by_role("textbox", name="Senha").fill("LeviJr08")
    page.get_by_role("button", name="Entrar", exact=True).click()
    page.get_by_role("link", name="Vagas, 0 nova notificação").click()
    page.get_by_test_id("typeahead-input").fill("RPA")
    page.get_by_test_id("typeahead-input").press("Enter")
    page.click("#workspace > div > div > div._604db7f0._246b1fe4.bebff295._7391903f > div > div > div:nth-child(1) > div")
    description_first_vaga = page.get_by_test_id("expandable-text-box").first.inner_text()
    time.sleep(2)
    page.click("#workspace > div > div > div._604db7f0._246b1fe4.bebff295._7391903f > div > div > div:nth-child(3) > div")
    description_second_vaga = page.get_by_test_id("expandable-text-box").first.inner_text()
    time.sleep(2)
    page.click("#workspace > div > div > div._604db7f0._246b1fe4.bebff295._7391903f > div > div > div:nth-child(5) > div")
    description_third_vaga = page.get_by_test_id("expandable-text-box").first.inner_text()
    time.sleep(2)
    # ---------------------
    nome_arquivo = 'vagas.csv'
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_completo = os.path.join(pasta_atual, nome_arquivo)

    vagas = []
    vagas.append({
           "vaga1" : description_first_vaga,
           "vaga2" : description_second_vaga,
           "vaga3" : description_third_vaga
    }) 
    with open(caminho_completo, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["vaga1", "vaga2", "vaga3"])
                writer.writeheader()
                writer.writerows(vagas)
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
