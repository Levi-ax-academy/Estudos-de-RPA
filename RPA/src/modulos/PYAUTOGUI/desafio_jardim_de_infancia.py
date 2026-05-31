import pyautogui
from time import sleep

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("paint")
pyautogui.press("enter")
sleep(0.5)
pyautogui.click(x=1000, y=105) # mudar pra cor cinza
sleep(0.5)

pyautogui.moveTo(x=150,y=260)

#fazer quadro cinza
pyautogui.dragTo(x=1850, y=260, button="left")
pyautogui.dragTo(x=1850, y=960, button="left")
pyautogui.dragTo(x=150, y=960, button="left")
pyautogui.dragTo(x=150, y=260, button="left")
pyautogui.dragTo(x=1850, y=260, button="left")

pyautogui.click(x=970, y=105) # mudar pra cor preto
sleep(0.5)
pyautogui.moveTo(x=1440,y=650)
dist = 300

#fazer corpo da casa
pyautogui.drag(dist,0,duration=0.5,button="left")
pyautogui.drag(0,dist,duration=0.5,button="left")
pyautogui.drag(-dist,0,duration=0.5,button="left")
pyautogui.drag(0,-dist,duration=0.5,button="left")
pyautogui.drag(dist,0,duration=0.5,button="left")

dist = 200
pyautogui.moveTo(x=1390,y=650)
pyautogui.drag(dist,-dist,duration=0.5,button="left")
pyautogui.drag(dist,dist,duration=0.5,button="left")
pyautogui.drag(-2*dist,0,duration=0.5,button="left")
pyautogui.drag(dist,-dist,duration=0.5,button="left")

pyautogui.click(x=383, y=117)
#pinta teto
pyautogui.click(x=1064, y=106)
sleep(0.5)
pyautogui.doubleClick(x=1570, y=500)
#pinta casa
pyautogui.click(x=1030, y=133)
sleep(0.5)
pyautogui.doubleClick(x=1570, y=700)

#fazer janelas
pyautogui.moveTo(x=1550, y=480)
pyautogui.drag(40,0,duration=0.5,button="left")
pyautogui.drag(0,60,duration=0.5,button="left")
pyautogui.drag(-40,0,duration=0.5,button="left")
pyautogui.drag(0,-60,duration=0.5,button="left")
pyautogui.drag(40,0,duration=0.5,button="left")

pyautogui.moveTo(x=1570, y=480)
pyautogui.drag(0,60,duration=0.5,button="left")
pyautogui.moveTo(x=1550, y=510)
pyautogui.drag(40,0,duration=0.5,button="left")
