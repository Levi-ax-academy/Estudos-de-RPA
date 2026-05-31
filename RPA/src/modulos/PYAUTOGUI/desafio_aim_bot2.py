import pyautogui
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        channel="chrome", 
        args=["--disable-blink-features=AutomationControlled"], 
        ignore_default_args=["--enable-automation"],
    )
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.xbitlabs.com/aim-trainer/", wait_until="load")
    time.sleep(0.5)
    maximizar = pyautogui.locateOnScreen("RPA\\src\\assets\\maximizar.png", confidence=0.7)
    pyautogui.click(maximizar)
    time.sleep(0.5)
    maximizar_jogo = pyautogui.locateOnScreen("RPA\\src\\assets\\maximizar_jogo.png", confidence=0.7)
    pyautogui.click(maximizar_jogo)
    time.sleep(0.5)
    page.click("xpath=/html/body/div[3]/div[2]")
    time.sleep(0.5)
    page.get_by_text("Start").first.click()

    time.sleep(3)
    pyautogui.FAILSAFE = True

    while(True):
        if page.locator("xpath=/html/body/div[2]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[1]/div/div/div/h3").is_visible():
            break
        try:
            blue_ball = pyautogui.locateOnScreen("RPA\\src\\assets\\blue_ball_2.png", confidence=0.75)
            pyautogui.click(blue_ball)
            print("bola azul encontrada")
    
        except:
            pyautogui.failSafeCheck()
            print("bola azul nao encontrada")
            
