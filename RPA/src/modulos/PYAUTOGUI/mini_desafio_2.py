import pyautogui
from time import sleep
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = False
pyautogui.press("win")
pyautogui.write("paint")
pyautogui.press("enter")
pyautogui.moveTo(x=1440,y=450)
pyautogui.dragTo(x=1040,y=450,duration=0.5,button="left")
pyautogui.dragTo(x=1400,y=650,duration=0.5,button="left")
pyautogui.dragTo(x=1240,y=350,duration=0.5,button="left")
pyautogui.dragTo(x=1080,y=650,duration=0.5,button="left")
pyautogui.dragTo(x=1440,y=450,duration=0.5,button="left")

pyautogui.moveTo(x=1440,y=350)
pyautogui.dragTo(x=1040,y=350,duration=0.5,button="left")
pyautogui.dragTo(x=1040,y=650,duration=0.5,button="left")
pyautogui.dragTo(x=1440,y=650,duration=0.5,button="left")
pyautogui.dragTo(x=1440,y=350,duration=0.5,button="left")