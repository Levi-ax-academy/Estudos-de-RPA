import pyautogui
from time import sleep
# pyautogui.PAUSE = 0.5
pyautogui.press("win")
sleep(1)
pyautogui.write("paint")
sleep(1)
pyautogui.press("enter")
sleep(1)

pyautogui.moveTo(x=1040,y=350)
sleep(1)
distance = 300
while distance > 0:
    pyautogui.drag(distance,0,duration=0.5,button="left")
    distance -= 10
    pyautogui.drag(0,distance,duration=0.5,button="left")
    pyautogui.drag(-distance,0,duration=0.5,button="left")
    distance -= 10
    pyautogui.drag(0,-distance,duration=0.5,button="left")