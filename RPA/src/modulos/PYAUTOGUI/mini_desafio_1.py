import pyautogui
from time import sleep
from datetime import datetime
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = False

pyautogui.press("win")
pyautogui.write("Bloco de Notas")
pyautogui.press("enter")

agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
pyautogui.write("Relatorio automatico", interval=0.03)
pyautogui.press("enter")
pyautogui.write(f"Gerado em: {agora}", interval=0.03)
pyautogui.press("enter")
pyautogui.write("Aula de PyAutoGUI - automacao visual", interval=0.03)
pyautogui.hotkey("ctrl", "s")
sleep(1)
pyautogui.write("relatorio_pyautogui.txt")
pyautogui.press("enter")