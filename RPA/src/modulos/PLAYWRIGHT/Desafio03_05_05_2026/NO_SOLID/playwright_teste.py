from playwright.sync_api import sync_playwright
import os
import csv
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://automationexercise.com")

    page.click("a[href='/products']")
    products = []
    products_name = page.locator(".product-overlay p")
    products_price = page.locator(".product-overlay h2")
    products_id = page.locator(".product-overlay a")
    for i in range(products_name.count()):
        products.append({
            "name" : products_name.nth(i).inner_text(),
            "price" : products_price.nth(i).inner_text(),
            "id" : products_id.nth(i).get_attribute("data-product-id")  
        })
        
# nome_arquivo = 'produtos_playwright.csv'
# pasta_atual = os.path.dirname(os.path.abspath(__file__))
# caminho_completo = os.path.join(pasta_atual, nome_arquivo)

# with open(caminho_completo, 'w', newline='', encoding='utf-8') as file:
#             writer = csv.DictWriter(file, fieldnames=["name", "price", "id"])
#             writer.writeheader()
#             writer.writerows(products) 

for i in products:
    print(i)
