import cv2
import easyocr
import re
import json

reader = easyocr.Reader(["pt", "en"])

# Lemos a imagem
img = cv2.imread("RPA\\src\\assets\\comprovante_pagamento.png")
if img is None:
    raise FileNotFoundError("Imagem nao encontrada: comprovante_pagamento.png")

# Apenas dobramos o tamanho para o EasyOCR enxergar as letras miúdas.
# Removemos o cv2.threshold para NÃO apagar os textos em cinza claro!
img = cv2.resize(img, None, fx=2, fy=2)

print("Analisando imagem com EasyOCR...")
resultado = reader.readtext(img)

# Coletamos todo o texto em uma lista simples e juntamos com quebras de linha
textos = [item[1] for item in resultado]
texto_completo = "\n".join(textos)

print("\nTexto Extraído da Imagem:")
print("=" * 50)
print(texto_completo)
print("=" * 50)

# --- MELHORIAS NOS REGEX ---

# 1. Valor: Aceita números, pontos, vírgulas E espaços no meio (ex: "R$ 61 20")
valor = re.search(r"R\$\s?[\d\.,\s]+", texto_completo)

# 2. Data: Captura o formato extenso (ex: "15 de Janeiro de 2023" ou "15 de janeiro de 2023")
data = re.search(r"\d{1,2}\s+de\s+[A-Za-z]+\s+de\s+\d{4}", texto_completo, re.IGNORECASE)

# 3. Protocolo/Autenticação: Captura o formato UUID longo (blocos alfanuméricos com hífens ou espaços)
protocolo = re.search(r"[a-zA-Z0-9]{8}[-\s]+[a-zA-Z0-9]{4}[-\s]+[a-zA-Z0-9]{4}[-\s]+[a-zA-Z0-9]{4}[-\s]+[a-zA-Z0-9]{12}", texto_completo)

# Monta o dicionário limpando os espaços extras que o regex possa ter pego
dados = {
    "valor": valor.group().strip() if valor else None,
    "data": data.group().strip() if data else None,
    "protocolo": protocolo.group().strip() if protocolo else None,
    "texto_completo": texto_completo
}

with open("resultado_ocr.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print("\nJSON gerado com sucesso:")
print(json.dumps(dados, ensure_ascii=False, indent=4))
print("\nTexto Extraído da Imagem:")
print("=" * 50)
print(texto_completo)
print("=" * 50)

# ==========================================
# 1. FUNÇÃO DE LIMPEZA (SANITIZAÇÃO)
# ==========================================
def limpar_valor_financeiro(texto_bruto):
    if not texto_bruto:
        return None
        
    # Remove as letras 'R', '$', 'S' e espaços nas bordas
    numero_sujo = re.sub(r"[R\$S]", "", texto_bruto).strip()
    
    # Remove espaços internos (ex: "61 20" vira "6120")
    numero_sujo = numero_sujo.replace(" ", "")
    
    # Se o OCR não leu a vírgula (ex: "6120"), nós forçamos a divisão por 100 -> 61.20
    if "," not in numero_sujo and "." not in numero_sujo:
        try:
            return float(numero_sujo) / 100
        except ValueError:
            return None
            
    # Se ele leu a vírgula (ex: "61,20"), trocamos por ponto e convertemos
    numero_sujo = numero_sujo.replace(",", ".")
    try:
        return float(numero_sujo)
    except ValueError:
        return None

# ==========================================
# 2. BUSCA POR ÂNCORA (REGEX INTELIGENTE)
# ==========================================
# Em vez de adivinhar o formato, nós procuramos a palavra "Valor" e pegamos a linha de baixo!
valor_match = re.search(r"Valor\n(R[\$S]\s?[\d\.,\s]+)", texto_completo, re.IGNORECASE)

# A data nós mantemos, pois já deu certo!
data_match = re.search(r"\d{1,2}\s+de\s+[A-Za-z]+\s+de\s+\d{4}", texto_completo, re.IGNORECASE)

# Para o protocolo, achamos o título "Código de Autenticação" e pegamos TUDO da linha de baixo
protocolo_match = re.search(r"Código de Autenticação\n(.+)", texto_completo)

# ==========================================
# 3. APLICAÇÃO DA LIMPEZA E CRIAÇÃO DO JSON
# ==========================================
dados = {
    # Aqui nós chamamos a nossa função mágica para o valor!
    "valor_limpo": limpar_valor_financeiro(valor_match.group(1)) if valor_match else None,
    "valor_bruto": valor_match.group(1).strip() if valor_match else None,
    
    # Correção rápida caso o OCR leia "Janciro"
    "data": data_match.group().strip().replace("Janciro", "Janeiro") if data_match else None,
    
    "protocolo": protocolo_match.group(1).strip() if protocolo_match else None
}

with open("resultado_ocr.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print("\nJSON gerado com sucesso:")
print(json.dumps(dados, ensure_ascii=False, indent=4))