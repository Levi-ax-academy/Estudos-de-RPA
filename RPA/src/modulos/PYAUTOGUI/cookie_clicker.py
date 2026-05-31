import pyautogui
import time
# from playwright.sync_api import sync_playwright
# pyautogui.MINIMUM_SLEEP = 0.5
pyautogui.FAILSAFE = True
time.sleep(1.5)
while True:
    pyautogui.click(x=330, y=507)
# with sync_playwright() as p:

#     browser = p.chromium.launch(
#         headless=False,
#         channel="chrome", 
#         args=["--disable-blink-features=AutomationControlled"], 
#         ignore_default_args=["--enable-automation"]
#     )
#     context = browser.new_context()

#     page = context.new_page()
#     page.goto("https://orteil.dashnet.org/cookieclicker/", wait_until="load")
#     page.wait_for_timeout(timeout=8000)
#     language = pyautogui.locateOnScreen('RPA\\src\\assets\\language.png', grayscale=True,confidence=0.8)
#     pyautogui.click(language, button="left")
#     page.wait_for_timeout(timeout=8000)
#     while True:
#         try:
#             cookie = pyautogui.locateOnScreen('RPA\\src\\assets\\cookie.png', grayscale=True, confidence=0.7)
#             pyautogui.click(cookie, button="left")
#             print("cookie clicado")
#             pyautogui.move(200,200)
            
#         except:
#             pyautogui.failSafeCheck()
#             print("cookie nao encontrado")
#             time.sleep(2)
