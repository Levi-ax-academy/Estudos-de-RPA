import pyautogui
import time

# Tempo para dar Alt+Tab e abrir o jogo
time.sleep(5)

# A MÁGICA PARA O PYAUTOGUI NÃO CRASHAR NO FPS:
# Desligamos a trava de segurança para ele não se assustar quando o mouse bater nas bordas
pyautogui.FAILSAFE = False

width, height = pyautogui.size()
centerX = width / 2
centerY = height / 2

print(f"Tela: {width}x{height} | Mira no Centro: {centerX},{centerY}")

while(True):
    try:
        reg = (int(width * 0.2), int(height * 0.2), int(width * 0.6), int(height * 0.6))
        
        target_location = pyautogui.locateOnScreen("RPA\\src\\assets\\blue_ball.png", region=reg, grayscale=True, confidence=0.6)

        if target_location:
            targetX, targetY = pyautogui.center(target_location)
            
            # Cálculo da distância relativa
            relX = int(targetX - centerX)
            relY = int(targetY - centerY)
            
            print(f"Alvo a {relX},{relY} pixels do centro. Mirando!")

            # Move o mouse usando exclusivamente o PyAutoGUI
            pyautogui.move(relX, relY, duration=0.5)
            
            # Clica usando exclusivamente o PyAutoGUI
            pyautogui.click()
            
            # Pausa pro jogo registrar o tiro
            time.sleep(0.1)

    except pyautogui.ImageNotFoundException:
        print("bola azul nao encontrada")
        time.sleep(0.1)
    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(0.1)