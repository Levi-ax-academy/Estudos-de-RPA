import pytesseract
from playwright.sync_api import sync_playwright
from time import sleep
from PIL import Image
import os
import re # Usaremos expressões regulares para extrair apenas os números do OCR

# 1. FUNÇÃO PARA EXTRAIR O TEXTO INICIAL
def extrair_texto(caminho):
    img = Image.open(caminho).convert('RGB')
    texto_completo = pytesseract.image_to_string(img).strip() 
    img.close()
    primeira_linha = texto_completo.split('\n')[0].strip()
    return primeira_linha

print("Extraindo textos das imagens bases...")
reaction_text = extrair_texto("C:\\Users\\levic\\Documents\\Códigos - Programação\\Python\\AIX_Academy\\RPA\\src\\assets\\reaction_time.png")
wait_green_text = extrair_texto("C:\\Users\\levic\\Documents\\Códigos - Programação\\Python\\AIX_Academy\\RPA\\src\\assets\\wait_for_green.png")
click_text = extrair_texto("C:\\Users\\levic\\Documents\\Códigos - Programação\\Python\\AIX_Academy\\RPA\\src\\assets\\click.png")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://www.humanbenchmark.com/tests/reactiontime")
    
    # Espera a tela inicial e começa
    page.get_by_text(reaction_text).first.wait_for(state="visible", timeout=10000)
    page.mouse.click(960, 540)
    print("Iniciou o jogo!")

    arquivo_txt = "historico_reacao_ocr.txt"

    if not os.path.exists(arquivo_txt):
        with open(arquivo_txt, "w", encoding="utf-8") as f:
            f.write("--- HISTÓRICO DE REAÇÃO VIA OCR ---\n")

    # LOOP DAS 5 RODADAS
    for rodada in range(5):
        print(f"\n[Rodada {rodada + 1}] Esperando a tela vermelha...")
        page.get_by_text(wait_green_text).first.wait_for(state="visible", timeout=10000)
        
        print("Esperando ficar verde...")
        page.get_by_text(click_text).first.wait_for(state="visible", timeout=10000)
        
        # CLICA IMEDIATAMENTE!
        page.mouse.click(960, 540)
        
        # --- CAPTURA E OCR EM TEMPO REAL ---
        # Damos uma micro pausa de 0.2 segundos para a tela azul de pontuação renderizar completamente
        sleep(0.2)
        
        # 1. Tira um screenshot da página inteira
        caminho_screenshot = f"screenshot_rodada_{rodada+1}.png"
        page.screenshot(path=caminho_screenshot)
        
        # 2. Abre a imagem e prepara para o Tesseract
        img_score = Image.open(caminho_screenshot).convert('L') # Converte para Escala de Cinza (Melhora o OCR)
        
        # Opcional: Se o Tesseract ler muita coisa errada em volta, podemos recortar apenas o centro da tela
        # largura, altura = img_score.size
        # img_score = img_score.crop((largura*0.3, altura*0.3, largura*0.7, altura*0.6))
        
        # 3. Executa o OCR (Forçando o Tesseract a focar em palavras/números comuns)
        texto_ocr = pytesseract.image_to_string(img_score, lang='eng')
        img_score.close()
        
        # 4. Limpa o texto usando Regex para achar o padrão de milissegundos (ex: 215 ms ou apenas os números)
        numeros = re.findall(r'\d+', texto_ocr)
        
        if numeros:
            tempo_final = f"{numeros[0]} ms"
        else:
            tempo_final = "Não identificado pelo OCR"
            print(f"⚠️ Texto bruto lido pelo OCR: {texto_ocr.strip()}") # Ajuda a debugar se o OCR falhar
            
        print(f"⚡ Tempo registrado via OCR: {tempo_final}")
        
        # 5. Salva no arquivo de texto
        with open(arquivo_txt, "a", encoding="utf-8") as f:
            f.write(f"Rodada {rodada + 1}: {tempo_final}\n")
        
        # Deleta o arquivo de screenshot temporário para não entulhar sua pasta
        if os.path.exists(caminho_screenshot):
            os.remove(caminho_screenshot)
            
        # Avança para a próxima rodada
        sleep(1)
        if rodada < 4:
            page.mouse.click(960, 540)
            sleep(0.5)

    print("\n🏁 Teste finalizado! Tempos gravados via processamento visual de imagem.")
    sleep(5)