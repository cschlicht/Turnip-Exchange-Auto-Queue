#When on turnip exchange, and on an island that you want to get into the Queue for, it will keep clicking refresh until
#"join this queue" is availabe, and then it will immedietly press the button and join the Queue for you

import pyautogui
import cv2
import time


while True:
    pyautogui.keyDown('ctrl')
    pyautogui.press('f5')
    time.sleep(2)
    pyautogui.click()
    x = pyautogui.locateCenterOnScreen(r'C:\Users\servi\OneDrive\Documents\Side Projects\AutoQueue\Capture2.PNG', confidence = .8)
    print(x)
    if x is not None:

        pyautogui.click(1123, 556)
        pyautogui.keyUp('ctrl')
        break





