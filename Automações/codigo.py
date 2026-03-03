

# pip install pyautogui
# pyautogui.press("win,space,command,tab,esc,etc) --> Pressionar uma tecla
# pyautogui.click("enter, x=55, y=66")
# pyautogui.hotkey("ctrl","l")
# pyautogui.write("Texto qualquer")
# pyautogui.PAUSE(0.5) - ou utilizar a lib "time";
# print(pyautogui.position()) - Pega a posição que o mouse está;
# é sempre bom utilizar um tempo de espera interessante para o site não entender que é um bot ou span.

import pyautogui
import time

def buscarMusic():
    pyautogui.press("win")
    pyautogui.write("Google")
    time.sleep(1.5)
    pyautogui.press("enter")
    time.sleep(1.5)
    pyautogui.write("YouTube")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.click(x=642, y=146)
    time.sleep(1.5)
    pyautogui.write("Lembrei de tu")
    pyautogui.press("enter")
buscarMusic()

