import pyautogui
import base64
import requests
import time
import pyperclip
import random

def exec():
    master = "https://www.ime.usp.br/~pf/dicios/br-utf8.txt"
    req = requests.get(master)
    req = req.text
    dicionario_palavras_portugues = req.split('\n')
    pyautogui.confirm('Vamo de dale? Contexto não será páreo!')
    time.sleep(2)
    for idx, value in enumerate(dicionario_palavras_portugues):
        value=random.choice(dicionario_palavras_portugues)
        print(value)
        pyperclip.copy(value)
        pyautogui.hotkey("ctrl", "v")
        # pyautogui.write(value)
        pyautogui.press('enter')
        
        pyautogui.hotkey('ctrl', 'a')
        
        pyautogui.press('backspace')
        dicionario_palavras_portugues.remove(value)
        print("Palavras restantes: ",len(dicionario_palavras_portugues))
        time.sleep(0.18)
exec()