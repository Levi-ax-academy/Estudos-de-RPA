import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import os
import csv
def test_extracao_vagas_linkedin():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()
        if os.path.exists("state.json"):
            context.set_storage_state("state.json")

        page.goto("https://br.linkedin.com/")
        
        if not os.path.exists("state.json"):
            page.get_by_role("link", name="Entrar", exact=True).click()
            page.locator("[type='email']").first.fill("levicavalcante07@gmail.com")
            page.locator("[type='password']").fill("LeviJr08")
            page.get_by_role("button", name="Entrar", exact=True).click()
            context.storage_state(path="state.json")
        vaga_escolhida = "Torneiro mecânico"
        pais_escolhido = "Brasil"
        page.goto("https://www.linkedin.com/jobs/")
        page.get_by_test_id("typeahead-input").fill(vaga_escolhida)
        page.get_by_test_id("typeahead-input").press("Enter")
        page.get_by_role("radio", name="Filtrar Vagas").click()
        time.sleep(4)

        page.locator("//*[@id='workspace']/div/header/div/div[1]/div").click()
        time.sleep(4)
        page.locator("[aria-label='Limpar localidade']").click()
        time.sleep(4)
        page.locator("[aria-label='Localidade']").fill(pais_escolhido)
        time.sleep(4)
        page.keyboard.press("Tab")
        time.sleep(2)
        page.keyboard.press("Tab")
        time.sleep(2)
        page.keyboard.press("Tab")
        time.sleep(2)
        page.keyboard.press("Enter")
        time.sleep(2)
        vagas = page.locator("[data-testid='lazy-column']").get_by_role('button')
        # time.sleep(20)
        total_vagas = vagas.count()
        print(total_vagas)
        vagas_salvas = []
        index_xpath = 1 

        for i in range(total_vagas):
            try:
                meu_xpath = f"xpath=//*[@id='workspace']/div/div/div[1]/div/div/div[{index_xpath}]"
                alvo = page.locator(meu_xpath)
                
                if alvo.count() == 0:
                    print(f"➡️ LinkedIn resetou a lista na vaga {i}! Voltando o XPath pro 1...")
                    index_xpath = 1 
                    meu_xpath = f"xpath=//*[@id='workspace']/div/div/div[1]/div/div/div[{index_xpath}]"
                    alvo = page.locator(meu_xpath)
                
                alvo.click(force=True)            
                page.wait_for_timeout(1500) 
                
                descricao_completa = page.get_by_test_id("expandable-text-box").first.inner_text()
                titulo_vaga = vagas.nth(i).inner_text()
                
                if "salário" in descricao_completa.lower() or "salario" in descricao_completa.lower():
                    print(f"✅ VAGA ENCONTRADA: {titulo_vaga}")
        
                    vagas_salvas.append({
                        "titulo": titulo_vaga,
                        "descricao": descricao_completa
                    })
                
                index_xpath += 1
                    
            except Exception as e:
                print(f"Erro na vaga {i}: {e}")
                index_xpath += 1 
                continue

test_extracao_vagas_linkedin()