import pyautogui
import time

def main():
    for i in range(6):
        position = pyautogui.position()
        print(f"Posição atual do mouse: {position}")
        time.sleep(2)
if __name__ == '__main__':
    main()