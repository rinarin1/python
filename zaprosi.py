import pyautogui as pg
import keyboard as kb
import time
g=input('Введите запрос')
if g == 'поиск':
    zapros=input('Введите запрос')
    pg.click(268,745)
    pg.hotkey('ctrl', 'e')
    kb.write(zapros)
    pg.press ('enter')
if g == 'текст':
    pg.hotkey('win' , 'r')
    time.sleep(3)
    pg.write ('notepad')
    pg.press ('enter')
if g == 'выход':
    pg.hotkey('alt', 'f4')
    pg.press('enter')
